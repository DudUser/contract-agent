from extractor.pdf_reader import extract_text_from_pdf
from agent.summarizer import summarize_contract_ai, AIQuotaExceeded
from agent.validator import validate_summary_for_advice_terms
from logs.logger import log_event
from pathlib import Path

INPUT_FILE = Path("input/contrato.pdf")
OUTPUT_FILE = Path("output/resumo.txt")
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

def save_summary(summary: str, output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(summary)

def process_contract(input_file: Path, output_file: Path) -> None:
    if not input_file.exists() or not input_file.suffix.lower() == ".pdf":
        raise ValueError("Arquivo inválido ou não encontrado.")
    if input_file.stat().st_size > MAX_FILE_SIZE:
        raise ValueError("Arquivo muito grande.")

    log_event("Execução iniciada")
    
    contract_text = extract_text_from_pdf(input_file.open("rb"))
    summary = summarize_contract_ai(contract_text)
    validate_summary_for_advice_terms(summary)

    save_summary(summary, output_file)
    log_event(f"Resumo salvo com sucesso em '{output_file}'")
    print("✅ Resumo gerado com sucesso!")

def main() -> None:
    try:
        process_contract(INPUT_FILE, OUTPUT_FILE)
    except AIQuotaExceeded:
        log_event("Limite da IA atingido")
        print("❌ Limite da IA atingido. Tente novamente mais tarde.")
    except Exception as e:
        log_event(f"ERRO: {str(e)}")
        print("❌ Erro ao processar contrato:", e)

if __name__ == "__main__":
    main()