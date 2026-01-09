from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from extractor.pdf_reader import extract_text_from_pdf
from agent.summarizer import summarize_contract_ai, AIQuotaExceeded
from agent.validator import validate_summary_for_advice_terms
from agent.comparer import compare_contracts_ai
from db.database import init_db
from db.models import save_history, list_history
from typing import Dict
from io import BytesIO

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

app = FastAPI()


@app.on_event("startup")
def startup():
    init_db()


async def process_pdf(file: UploadFile, language_mode: str) -> str:
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Apenas PDFs são aceitos.")

    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="Arquivo muito grande.")

    file_like = BytesIO(contents)
    text = extract_text_from_pdf(file_like)

    summary = summarize_contract_ai(
        text,
        language_mode=language_mode
    )

    validate_summary_for_advice_terms(summary)
    return summary


@app.post("/contracts/upload")
async def upload_contract(
    file: UploadFile = File(...),
    language_mode: str = Form("tecnico")
) -> Dict[str, str]:
    try:
        summary = await process_pdf(file, language_mode)
        save_history("single", summary)
        return {"summary": summary}

    except AIQuotaExceeded:
        raise HTTPException(
            status_code=503,
            detail="Serviço de IA temporariamente indisponível."
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/contracts/compare")
async def compare_contracts_api(
    file_a: UploadFile = File(...),
    file_b: UploadFile = File(...),
    language_mode: str = Form("tecnico")
) -> Dict[str, str]:
    try:
        summary_a = await process_pdf(file_a, language_mode)
        summary_b = await process_pdf(file_b, language_mode)

        comparison = compare_contracts_ai(summary_a, summary_b)
        save_history("compare", comparison)

        return {"comparison": comparison}

    except AIQuotaExceeded:
        raise HTTPException(
            status_code=503,
            detail="Serviço de IA temporariamente indisponível."
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/history")
def get_history(limit: int = 20) -> Dict[str, list]:
    return {"history": list_history(limit)}
