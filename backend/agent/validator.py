from typing import List

FORBIDDEN_TERMS: List[str] = [
    "aconselho",
    "recomendo",
    "garanto",
    "deve aceitar",
    "é vantajoso",
    "é desvantajoso"
]

def validate_summary_for_advice_terms(summary_text: str, forbidden_terms: List[str] = FORBIDDEN_TERMS) -> None:
    """
    Valida se o resumo contém termos que configuram aconselhamento.

    Args:
        summary_text (str): Texto do resumo a ser validado.
        forbidden_terms (List[str]): Lista de termos proibidos.

    Raises:
        ValueError: Se algum termo proibido for encontrado no resumo.
    """
    summary_lower = summary_text.lower()
    detected_terms = [term for term in forbidden_terms if term in summary_lower]

    if detected_terms:
        terms_str = ", ".join(detected_terms)
        raise ValueError(f"Conteúdo inválido detectado (aconselhamento): {terms_str}")
