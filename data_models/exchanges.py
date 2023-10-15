from pydantic import BaseModel

def Exchanges(BaseModel):
    """NOTE: updated is in unix timestamp"""
    id: str 
    name: str 
    rank: int 
    percent_total_volume: float 
    volume_usd: float 
    trading_pairs: int 
    socket: bool
    exchange_url: str 
    updated: int 