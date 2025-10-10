# Paso 1: Bibliotecas y Configuración
import vertexai
from vertexai.generative_models import GenerativeModel

# Reemplaza con los datos de tu proyecto de Google Cloud
PROJECT_ID = "stone-poetry-473315-a9"
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

# Paso 2: M (Modelo) - Selección del Cerebro Experto
modelo = GenerativeModel("gemini-2.5-flash")

# Paso 3: C (Contexto) - Definición de los Datos
tema_principal = "Animales del Océano"
animales_interesantes = [
    "Pulpo",
    "Caballito de mar",
    "Ballena azul",
    "Tiburón blanco"
]

contexto_formateado = f"""
- Tema Principal: {tema_principal}
- Animales a Incluir: {', '.join(animales_interesantes)}
"""

# Paso 4: P (Petición) - Construcción del Prompt
plantilla_prompt = """
Actúa como un biólogo marino y divulgador científico entusiasta.

Tu tarea es compartir datos curiosos y fascinantes sobre animales marinos.

Usa la siguiente información para tu explicación:
---
{contexto_para_usar}
---

Misión: Comparte 3-4 datos sorprendentes y poco conocidos sobre estos animales del océano. 
Incluye comportamientos únicos, habilidades especiales o características extraordinarias 
que hacen a estas criaturas realmente asombrosas.

Formato:
- Un dato curioso por animal
- Explicación breve pero impactante
- Lenguaje accesible para todo público
- Tonos: asombroso y educativo
"""

prompt_final = plantilla_prompt.format(contexto_para_usar=contexto_formateado)

# Paso 5: Ejecución y Resultado

# Se envía la petición al modelo.
respuesta = modelo.generate_content(prompt_final)

print(respuesta.text)