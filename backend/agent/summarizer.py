from openai import OpenAI, RateLimitError, APIError, Timeout
from agent.prompt import build_summary_prompt
from agent.ai_client import call_with_retry
from agent.token_monitor import log_token_usage

client = OpenAI()

class AIQuotaExceeded(Exception):
    pass

DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_TEMPERATURE = 0.2


def summarize_contract_ai(
    text: str,
    language_mode: str = "tecnico",
    model: str = DEFAULT_MODEL,
    temperature: float = DEFAULT_TEMPERATURE
) -> str:


    messages = [
        {"role": "system", "content": build_summary_prompt(language_mode)},
        {"role": "user", "content": text}
    ]

    try:
        response = call_with_retry(
            lambda: client.chat.completions.create(
                model=model,
                temperature=temperature,
                messages=messages
            )
        )

        # ✅ CAPTURA DE USO DE TOKENS
        usage = response.usage

        log_token_usage(
            operation="summarize_contract",
            model=model,
            prompt_tokens=usage.prompt_tokens,
            completion_tokens=usage.completion_tokens,
            total_tokens=usage.total_tokens
        )

        return response.choices[0].message.content

    except RateLimitError:
        raise AIQuotaExceeded("Limite de uso da IA atingido")

    except (APIError, Timeout) as e:
        raise RuntimeError(f"Erro ao chamar API: {e}")