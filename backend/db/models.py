from typing import List, Dict
from db.database import get_connection

def save_history(mode: str, result: str) -> None:
    """
    Salva um registro de histórico no banco.

    Args:
        mode (str): Tipo de operação ou modo.
        result (str): Resultado da operação.
    """
    try:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO history (mode, result) VALUES (?, ?)",
                (mode, result)
            )
    except Exception as e:
        # Aqui você pode logar o erro ou tratar conforme necessidade
        raise RuntimeError(f"Erro ao salvar histórico: {e}")

def list_history(limit: int = 20) -> List[Dict[str, str]]:
    """
    Retorna os últimos registros do histórico.

    Args:
        limit (int): Número máximo de registros retornados.

    Returns:
        List[Dict[str, str]]: Lista de registros do histórico.
    """
    try:
        with get_connection() as conn:
            cursor = conn.execute(
                "SELECT id, mode, result, created_at FROM history ORDER BY id DESC LIMIT ?",
                (limit,)
            )
            rows = cursor.fetchall()

        # Usando destructuring para mais clareza
        return [
            {"id": r[0], "mode": r[1], "result": r[2], "created_at": r[3]}
            for r in rows
        ]
    except Exception as e:
        raise RuntimeError(f"Erro ao listar histórico: {e}")
