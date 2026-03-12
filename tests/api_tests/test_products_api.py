import requests


def test_get_products_api():

    url = "https://dummyjson.com/products"

    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()

    assert "products" in data

    assert len(data["products"]) > 0