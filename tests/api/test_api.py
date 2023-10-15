# import pytest
# from api.main import get_api_url, BASE_URL


# def test_get_api_url():
#     valid_domain = "asset"
#     invalid_domain = "fake domain"
#     generated_api_url = get_api_url(valid_domain)

#     with pytest.raises(ValueError):
#         get_api_url(invalid_domain)

#     assert generated_api_url == f"{BASE_URL}/{valid_domain}"
