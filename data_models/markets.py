from pydantic import BaseModel
from typing import Optional

def Markets(BaseModel):
    exchange_id: str 
    base_symbol: str 
    quote_symbol: str 
    base_id: str 
    quote_id: str 
    asset_symbol: str 
    asset_id: str 
    limit: Optional[int]
    offset: Optional[int]