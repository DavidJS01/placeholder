from pydantic import BaseModel


class Assets(BaseModel):
    id: str
    rank: int
    symbol: str
    name: str
    supply: float
    max_supply: float
    market_cap_usd: float
    price_usd: float
    change_percent_last_24_hours: float
