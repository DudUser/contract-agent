from openai import OpenAI, RateLimitError, APIError, Timeout
from agent.prompt import COMPARISON_PROMPT
from agent.rate_limiter import SimpleRateLimiter
from agent.ai_client import call_with_retry
from agent.token_monitor import log_token_usage

client = OpenAI()

MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0.2

# 🔒 Limite: 5 comparações por minuto por usuário
rate_limiter = SimpleRateLimiter(max_calls=5, window_seconds=60)


class AIQuotaExceeded(Exception):
    pass


def compare_contracts_ai(
    summary_a: str,
    summary_b: str,
    user_id: str,
    model: str = MODEL_NAME,
    temperature: float = TEMPERATURE
) -> str:
    """
    Compara dois resumos de contratos usando OpenAI.
    Retorna as diferenças relevantes.
    """

    # 🔐 CONTROLE POR USUÁRIO
    rate_limiter.check(user_id)

    messages = [
        {"role": "system", "content": COMPARISON_PROMPT},
        {
            "role": "user",
            "content": f"Contrato A:\n{summary_a}\n\nContrato B:\n{summary_b}"
        }
    ]

    try:
        response = call_with_retry(
            lambda: client.chat.completions.create(
                model=model,
                temperature=temperature,
                messages=messages
            )
        )

        # ✅ MONITORAMENTO DE TOKENS
        usage = response.usage

        log_token_usage(
            operation="compare_contracts",
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