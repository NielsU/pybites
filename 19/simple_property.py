from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name: str, expires: datetime):
        self._name = name
        self._expires = expires

    @property
    def expired(self) -> bool:
        return self._expires < NOW
