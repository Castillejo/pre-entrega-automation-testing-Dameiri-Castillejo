import requests
import json
import pytest

# --- CONFIGURACIÓN ---
@pytest.fixture(scope="session")
def base_url():
    """Define la URL base para todas las pruebas."""
    # JSONPlaceholder NO requiere autenticación.
    url = "https://jsonplaceholder.typicode.com"
    print(f"\n [SETUP] URL base configurada: {url}")
    return url


# --- CASOS DE PRUEBA ---

@pytest.mark.get
def test_get_list_posts(base_url):
    """
    Prueba el endpoint GET /posts.
    Verifica que retorna 200 OK, es una lista y contiene al menos 100 posts.
    """
    print("\n Ejecutando prueba: test_get_list_posts")

    url = f"{base_url}/posts"
    print(f" Solicitando: {url}")

    response = requests.get(url)
    print(f"Código de estado recibido: {response.status_code}")

    assert response.status_code == 200

    data = response.json()
    print(f"Total de posts recibidos: {len(data)}")

    assert isinstance(data, list)
    assert len(data) == 100

    first_post = data[0]
    print(f"Primer post: {first_post}")

    assert "userId" in first_post
    assert "title" in first_post
    assert isinstance(first_post["id"], int)


@pytest.mark.post
def test_post_create_post(base_url):
    """
    Prueba el endpoint POST /posts para crear un nuevo recurso.
    Verifica que retorna 201 Created y que los datos se reflejan.
    """
    print("\n Ejecutando prueba: test_post_create_post")

    url = f"{base_url}/posts"
    payload = {
        "title": "Nuevo Post Automatizado",
        "body": "Este es el cuerpo del post creado por Pytest.",
        "userId": 99
    }
    print(f"Enviando POST a {url} con datos: {payload}")

    response = requests.post(url, json=payload)
    print(f"Código de estado recibido: {response.status_code}")

    assert response.status_code == 201

    data = response.json()
    print(f"Respuesta recibida: {data}")

    assert data["title"] == payload["title"]
    assert data["userId"] == payload["userId"]

    assert "id" in data
    assert data["id"] == 101
    print("Post creado exitosamente (simulado)")


@pytest.mark.delete
def test_delete_post(base_url):
    """
    Prueba el endpoint DELETE /posts/{id} para eliminar un recurso.
    Verifica que retorna 200 OK (comportamiento de JSONPlaceholder para DELETE exitoso).
    """
    print("\n Ejecutando prueba: test_delete_post")

    post_id_to_delete = 1
    url = f"{base_url}/posts/{post_id_to_delete}"
    print(f"Enviando DELETE a {url}")

    response = requests.delete(url)
    print(f"Código de estado recibido: {response.status_code}")

    assert response.status_code == 200

    data = response.json()
    print(f" Respuesta: {data}")
    assert data == {}

    print("Post eliminado (simulación correcta)")


@pytest.mark.error
def test_error_not_found(base_url):
    """
    Prueba de validación de error:
    Verifica que al intentar obtener un recurso que no existe retorna 404 Not Found.
    """
    print("\n Ejecutando prueba: test_error_not_found")

    non_existent_id = 999999
    url = f"{base_url}/posts/{non_existent_id}"
    print(f"Solicitando recurso inexistente: {url}")

    response = requests.get(url)
    print(f"Código de estado recibido: {response.status_code}")

    assert response.status_code == 404

    data = response.json()
    print(f" Respuesta: {data}")
    assert data == {}

    print("Validación de error 404 exitosa")


@pytest.mark.flow
def test_chained_flow_create_get_delete_simulation(base_url):
    """
    Flujo Encadenado CORREGIDO para JSONPlaceholder:
    1. POST (Validar creación simulada).
    2. DELETE (Usar el ID simulado para validar que la eliminación simulada funciona).
    """
    print("\n Ejecutando prueba: test_chained_flow_create_get_delete_simulation")

    # 1. POST (Crear Recurso)
    post_url = f"{base_url}/posts"
    payload = {"title": "Post Encadenado", "userId": 1}
    print(f"Enviando POST a {post_url} con datos: {payload}")

    post_response = requests.post(post_url, json=payload)
    print(f"Código POST recibido: {post_response.status_code}")

    assert post_response.status_code == 201

    created_data = post_response.json()
    created_id = created_data.get("id")
    print(f"Post creado con ID simulado: {created_id}")

    assert created_id == 101

    # 2. DELETE (Eliminar el Recurso Creado [Simulado])
    delete_url = f"{base_url}/posts/{created_id}"
    print(f"Enviando DELETE a {delete_url}")

    delete_response = requests.delete(delete_url)
    print(f"Código DELETE recibido: {delete_response.status_code}")

    assert delete_response.status_code == 200
    print("Flujo POST → DELETE completado exitosamente (simulado)")
