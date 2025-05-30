import requests

def get_random_joke():
    url = "https://v2.jokeapi.dev/joke/Any?lang=es"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data.get("type") == "single":
            return data.get("joke")
        elif data.get("type") == "twopart":
            return f"{data.get('setup')} ... {data.get('delivery')}"
        else:
            return "No se pudo obtener un chiste en este momento."
    except Exception as e:
        return "Error al conectar con la API de chistes."
