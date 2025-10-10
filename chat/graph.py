import vertexai
from vertexai.generative_models import GenerativeModel
from django.conf import settings

# Inicializar Vertex AI
vertexai.init(project=settings.PROJECT_ID, location=settings.LOCATION)

PRIMARY_MODEL = "gemini-1.5-flash"
FALLBACK_MODEL = "gemini-2.5-flash"

def generar_respuesta(mensaje_usuario: str) -> str:
    prompt = (
        f"El usuario dice: '{mensaje_usuario}'.\n"
        "Responde de forma natural, breve (máx. 3 frases), en español, "
        "y con un tono amigable tipo chatbot."
    )

    last_error = None
    for model_name in (PRIMARY_MODEL, FALLBACK_MODEL):
        try:
            model = GenerativeModel(model_name)
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            last_error = e
    return f"[Error al generar respuesta: {last_error}]"
