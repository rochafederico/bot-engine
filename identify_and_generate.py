import json
import os

async def identify_and_generate(skill: str, message: str, request_context: dict):
    try:
        response_file = f"responses/{skill}.json"
        if not os.path.exists(response_file):
            raise FileNotFoundError(f"No se encontró el archivo {response_file}")
        with open(response_file, "r", encoding="utf-8") as f:
            data = json.load(f)

            if data:
                # Navegar la nueva estructura
                output = data.get("response", {}).get("output", {})
                generic = output.get("generic", [])
                intents = output.get("intents", [])

                # Actualizar el contexto con el session_id
                context = data.get("response", {}).get("context", {})

                return intents or "unknown", generic or "No tengo respuesta para ese mensaje.", context or "unknown"
            else:
                return "unknown", "No tengo respuesta para ese mensaje."
    except Exception as e:
        raise e