import json
from pathlib import Path

def get_productos_json(json_file="data_productos.json"):
    """
    Carga un archivo JSON con los productos y devuelve una lista de tuplas
    (nombre, precio, descripcion) para usar en @pytest.mark.parametrize.
    """
    # Ruta absoluta al archivo en /data/
    json_path = Path(__file__).parent.parent / "data" / json_file

    # Leer archivo JSON
    with open(json_path, "r", encoding="utf-8") as file:
        productos = json.load(file)

    # Convertir a lista de tuplas para parametrización
    casos = [(p["nombre"], p["precio"], p["descripcion"]) for p in productos]

    return casos
