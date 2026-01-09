import time
from openai import RateLimitError

def call_with_retry(callable_fn, max_retries: int = 3, base_delay: int = 2):
    """
    Executa uma chamada à API da OpenAI com retry automático
    em caso de RateLimitError (HTTP 429).

    :param callable_fn: função que executa a chamada à API
    :param max_retries: número máximo de tentativas
    :param base_delay: tempo base de espera (segundos)
    """
    for attempt in range(max_retries):
        try:
            return callable_fn()
        except RateLimitError:
            if attempt >= max_retries - 1:
                raise

            wait_time = base_delay * (attempt + 1)
            time.sleep(wait_time)
