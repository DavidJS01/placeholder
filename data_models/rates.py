from pydantic import BaseModel


class Rates(BaseModel):
    id: str
    symbol: str
    currency_symbol: str
    rate_usd: float
    currency_type: str
