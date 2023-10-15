import requests
from enums import DataDomains, is_valid_enum_domain


class CoincapAPI:
    def __init__(self):
        self.base_url = "https://api.coincap.io/v2"

    def get_api_url(self, url_suffix: str) -> str:
        """
        function that given an input string returns an
        api url
        """
        if is_valid_enum_domain(url_suffix):
            return f"{self.base_url}/{url_suffix}"
        raise ValueError(
            f"The given domain `{url_suffix}` is not a valid data domain of {DataDomains._member_names_}"
        )

    def get_api_response(self, api_url) -> dict:
        print(api_url)
        return requests.request("GET", api_url, headers={}, data={}).json()


class AssetsAPI(CoincapAPI):
    def __init__(self):
        super().__init__()
        self.url_suffix = "assets"
        self.url = self.get_api_url(self.url_suffix)

    def get_all_assets(self):
        return self.get_api_response(self.url)

    def get_asset_by_id(self, id: str) -> dict:
        """example id: bitcoin"""
        return self.get_api_response(f"{self.url}/{id}")

    def get_asset_by_market(self, id: str) -> dict:
        return self.get_api_response(f"{self.url}/{id}/markets")


class RatesAPI(CoincapAPI):
    def __init__(self):
        super().__init__()
        self.url_suffix = "rates"
        self.url = self.get_api_url(self.url_suffix)

    def get_all_rates(self):
        return self.get_api_response(self.url)

    def get_rate_by_id(self, id: str) -> dict:
        """example id: bitcoin"""
        return self.get_api_response(f"{self.url}/{id}")


class MarketsAPI(CoincapAPI):
    def __init__(self):
        super().__init__()
        self.url_suffix = "markets"
        self.url = self.get_api_url(self.url_suffix)

    def get_all_markets(self):
        return self.get_api_response(self.url)


class ExchangesAPI(CoincapAPI):
    def __init__(self):
        super().__init__()
        self.url_suffix = "exchanges"
        self.url = self.get_api_url(self.url_suffix)

    def get_all_exchanges(self):
        return self.get_api_response(self.url)

    def get_exchanges_by_id(self, id: str):
        return self.get_api_response(f"{self.url}/{id}")


if __name__ == "__main__":
    api = CoincapAPI()
    apis = ExchangesAPI()
    # x = apis.get_asset_by_id("bitcoin")
    # x = apis.get_all_rates()
    y = apis.get("kraken")

    print(y)
