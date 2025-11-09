import pytest
import requests
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000/api"
meals = []

def test_create_meal():
  new_meal_data = {
    "name": "Pão",
    "description": "Pão Integral",
    "datetime": datetime.now().isoformat(),
    "is_diet": True
  }
  
  response = requests.post(f"{BASE_URL}/meals", json=new_meal_data)
  assert response.status_code == 201

  response_json = response.json()

  assert "id" in response_json
  assert response_json["name"] == "Pão"

  meals.append(response_json["id"])

def test_get_all_meals():
  response = requests.get(f"{BASE_URL}/meals")
  assert response.status_code == 200
  response_json = response.json()
  assert isinstance(response_json, list)

  if len(response_json) > 0:
    first_meal = response_json[0]
    assert "id" in first_meal
    assert "name" in first_meal
    assert "description" in first_meal
    assert "datetime" in first_meal
    assert "is_diet" in first_meal

def test_get_meal_by_id():
  response = requests.get(f"{BASE_URL}/meals/1")
  assert response.status_code == 200
  response_json = response.json()
  
  assert "id" in response_json
  assert "name" in response_json
  assert "description" in response_json
  assert "datetime" in response_json
  assert "is_diet" in response_json

def test_update_meal():
  if meals:
    meal_id = meals[0]
    payload = {
      "name": "Pão Atualizado",
      "description": "Pão Integral Atualizado",
      "datetime": datetime.now().isoformat(),
      "is_diet": False
    }
    response = requests.put(f"{BASE_URL}/meals/{meal_id}", json=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json

    response = requests.get(f"{BASE_URL}/meals/{meal_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["name"] == payload["name"]
    assert response_json["description"] == payload["description"]
    assert response_json["datetime"] == payload["datetime"]
    assert response_json["is_diet"] == payload["is_diet"]

def test_delete_meal():
  if meals:
    meal_id = meals[0]
    response = requests.delete(f"{BASE_URL}/meals/{meal_id}")
    assert response.status_code == 200

    response = requests.get(f"{BASE_URL}/meals/{meal_id}")
    assert response.status_code == 404

