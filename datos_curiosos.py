from google.cloud import aiplatform
import vertexai
from vertexai.generative_models import GenerativeModel

# Configuración 
PROJECT_ID = "stone-poetry-473315-a9"
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

# Contexto
contexto_para_usar = "Egipto"

#  Modelo 
modelo = GenerativeModel("gemini-2.0-flash") 

# Prompt
plantilla_prompt = """
Actúa como un experto en datos curiosos y divulgación científica.
Tu tarea es generar un dato curioso, breve y sorprendente sobre el siguiente tema.

Tema:
---
{contexto_para_usar}
---

Misión:
Genera un único dato curioso que sea interesante, educativo y verificable.
Evita repetir información muy común o genérica.
"""

prompt_final = plantilla_prompt.format(contexto_para_usar=contexto_para_usar)

# Llamar al modelo y mostrar el resultado
respuesta = modelo.generate_content(prompt_final)

print(respuesta.text)