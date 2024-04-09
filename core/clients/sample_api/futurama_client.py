import httpx

from core.clients.sample_api.futurama_dtos import Info


class FuturamaClient:
    _BASE_URL = "https://api.sampleapis.com"

    def get_show_info(self) -> Info | None:
        resp = httpx.get(f"{self._BASE_URL}/futurama/info")
        resp.raise_for_status()
        return Info(**resp.json()[0])
