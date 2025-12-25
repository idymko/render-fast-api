
import pytest
import json
import warnings 

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.anyio
async def test_post() -> None:
    data = {
            "name": "Dima",
            "tags": "tag",
            "item_id": 1
            }
    r = client.post("/items/", json=data) # Using json parameter instead of manual dumps
    assert r.status_code == 200
    response_data = r.json()
    assert response_data["name"] == data["name"]
    assert response_data["item_id"] == data["item_id"]

@pytest.mark.anyio
async def test_get_path() -> None:
    
    r = client.get("/items/1")
    assert r.status_code == 200
    assert r.json() == {"fetch": f"Fetched: Dima with qty of 1"}

@pytest.mark.anyio
async def test_get_query() -> None:
    
    r = client.get("/items/1?count=3")
    assert r.status_code == 200
    assert r.json() == {"fetch": f"Fetched: Dima with qty of 3"}
