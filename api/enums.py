from enum import Enum


class DataDomains(Enum):
    ASSETS = "assets"
    RATES = "rates"
    EXCHANGES = "exchanges"
    MARKETS = "markets"
    CANDLES = "candles"


def is_valid_enum_domain(input_string: str) -> bool:
    """
    function that checks if a given string is the name
    of a DataDomains enum member
    :param input_string: name of string to validate against
    :returns: bool
    """
    for domain in DataDomains:
        if input_string.upper() == domain.name:
            return True
    return False
