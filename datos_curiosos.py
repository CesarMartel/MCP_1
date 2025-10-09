import vertexai
from vertexai.generative_models import GenerativeModel

PROJECTO_ID = "stone-poetry-473315-a9"
LOCATION = "us-central1"

vertexai.init(project=PROJECTO_ID, location=LOCATION)

modelo = GenerativeModel("gemini-2.5-flash")

tema_principal = "Pandas gigantes"


contexto_formateado = f"""
- Tema a Explicar: {tema_principal}

"""
plantilla_prompt = """
Contexto:
{contexto_formateado}

Instrucciones:
Eres un creador de datos curiosos. Tu tarea es generar un dato curioso, sorprendente y entretenido sobre el tema proporcionado.

Requisitos:
- El dato debe ser verídico pero poco conocido
- Debe ser breve (1-2 párrafos máximo)
- Debe ser interesante para el público general
- Incluye un detalle sorprendente que la mayoría de personas desconozca

Genera exactamente UN dato curioso sobre el tema proporcionado.
"""
prompt_final = plantilla_prompt.format(contexto_formateado=contexto_formateado)


respuesta = modelo.generate_content(prompt_final)

print(respuesta.text)

