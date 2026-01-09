from PyPDF2 import PdfReader
from logs.logger import log_event
from typing import BinaryIO

def extract_text_from_pdf(file_obj: BinaryIO) -> str:
    """
    Recebe um arquivo PDF em memória (UploadFile.file ou BytesIO)
    e retorna todo o texto extraído.

    Args:
        file_obj (BinaryIO): Arquivo PDF em memória.

    Returns:
        str: Texto completo extraído do PDF.

    Raises:
        ValueError: Se o PDF não puder ser lido.
    """
    log_event("Iniciando leitura do PDF em memória")

    try:
        reader = PdfReader(file_obj)
    except Exception as e:
        raise ValueError(f"Erro ao ler PDF: {e}")

    texts = []
    for page_number, page in enumerate(reader.pages, start=1):
        try:
            page_text = page.extract_text()
            if page_text:
                texts.append(page_text)
        except Exception as e:
            log_event(f"Erro ao processar página {page_number}: {e}")

    log_event(f"Extração de texto concluída: {len(texts)} páginas processadas")
    return "\n".join(texts)