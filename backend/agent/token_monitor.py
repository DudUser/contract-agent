from datetime import datetime
from typing import Optional


def log_token_usage(
    *,
    user_id: str,
    operation: str,
    model: str,
    prompt_tokens: int,
    completion_tokens: int,
    total_tokens: int
):
    """
    Registra uso de tokens da OpenAI.
    Pode ser adaptado para banco, redis ou observabilidade.
    """

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "operation": operation,
        "model": model,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": total_tokens,
    }

    # MVP: log em arquivo
    with open("logs/token_usage.log", "a", encoding="utf-8") as f:
        f.write(str(log_entry) + "\n")