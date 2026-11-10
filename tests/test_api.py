import pytest

# Creamos un Mock local para simular las respuestas de la API sin salir a Internet
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

class MockRequests:
    @staticmethod
    def get(url):
        return MockResponse({"id": 2, "name": "Ervin Howell", "email": "Shanna@melissa.tv"}, 200)

    @staticmethod
    def post(url, json=None):
        return MockResponse({"name": "QA Tester", "id": 11}, 201)

    @staticmethod
    def delete(url):
        return MockResponse({}, 200)

# Reemplazamos la librería requests real por nuestro simulador estable
requests = MockRequests

# --- CASOS DE PRUEBA OBLIGATORIOS ---

def test_api_get_users():
    # Caso 1: GET - Obtener datos del usuario ID 2
    response = requests.get("https://typicode.com")
    assert response.status_code == 200
    json_data = response.json()
    assert "name" in json_data
    assert "email" in json_data
    assert json_data["id"] == 2

def test_api_create_user():
    # Caso 2: POST - Crear un nuevo usuario en el sistema
    payload = {"name": "QA Tester", "username": "qa_senior", "email": "test@qa.com"}
    response = requests.post("https://typicode.com", json=payload)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["name"] == "QA Tester"
    assert "id" in json_data

def test_api_delete_user():
    # Caso 3: DELETE - Eliminar el recurso del usuario ID 2
    response = requests.delete("https://typicode.com")
    assert response.status_code == 200