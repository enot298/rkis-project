"""Точка интеграции с REST API (контракт v1). Пока без запросов.

Реальные вызовы (вход, список заказов и т. д.) будут добавлены на этапе Э8,
когда на сервере появятся эндпоинты (этап Э7).
"""
import config


class ApiClient:
    def __init__(self, base_url: str = config.API_BASE_URL, timeout: int = config.REQUEST_TIMEOUT_S):
        self.base_url = base_url
        self.timeout = timeout
        self.token = None  # JWT после входа

    def url(self, path: str) -> str:
        """Собрать полный адрес: url('/orders/') -> http://.../v1/orders/."""
        return self.base_url + "/" + path.lstrip("/")
