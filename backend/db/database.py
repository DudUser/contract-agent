import sqlite3
from pathlib import Path
from typing import Optional, List, Tuple

DB_PATH = Path(__file__).parent / "history.db"

def get_connection() -> sqlite3.Connection:
    """Retorna uma conexão com o banco SQLite."""
    return sqlite3.connect(DB_PATH)

def init_db() -> None:
    """Cria a tabela de histórico se não existir."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mode TEXT NOT NULL,
                result TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        # Opcional: criar índice
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_mode_created_at
            ON history(mode, created_at)
        """)

def insert_history(mode: str, result: str) -> None:
    """Insere um registro no histórico."""
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO history (mode, result) VALUES (?, ?)",
            (mode, result)
        )

def fetch_history(limit: int = 100) -> List[Tuple[int, str, str, str]]:
    """Retorna os últimos registros do histórico, limitado por 'limit'."""
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT id, mode, result, created_at FROM history ORDER BY created_at DESC LIMIT ?",
            (limit,)
        )
        return cursor.fetchall()
