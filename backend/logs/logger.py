import logging
from pathlib import Path

LOG_FILE = Path("logs/run.log")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)  # garante pasta existente

# Configuração global do logger
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)

def log_event(message: str, level: str = "info"):
    """
    Registra um evento no log.

    Args:
        message (str): Mensagem a ser logada.
        level (str): Nível de log ('info', 'warning', 'error').
    """
    level = level.lower()
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    else:
        logging.info(message)  # fallback