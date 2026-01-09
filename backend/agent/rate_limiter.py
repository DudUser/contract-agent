import time
from collections import defaultdict, deque

class RateLimitExceeded(Exception):
    pass


class SimpleRateLimiter:
    def __init__(self, max_calls: int, window_seconds: int):
        self.max_calls = max_calls
        self.window = window_seconds
        self.calls = defaultdict(deque)

    def check(self, key: str):
        now = time.time()
        window_start = now - self.window
        q = self.calls[key]

        # remove chamadas antigas
        while q and q[0] < window_start:
            q.popleft()

        if len(q) >= self.max_calls:
            raise RateLimitExceeded(
                f"Limite de {self.max_calls} chamadas em {self.window}s atingido"
            )

        q.append(now)
