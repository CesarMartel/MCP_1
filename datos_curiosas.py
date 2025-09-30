# Paso 1: Bibliotecas y Configuración
import vertexai
from vertexai.generative_models import GenerativeModel

# Reemplaza con los datos de tu proyecto de Google Cloud
# Asegúrate de haber instalado 'google-cloud-aiplatform'
PROJECT_ID = "stone-poetry-473315-a9"  # <--- ¡IMPORTANTE! Reemplaza esto con tu ID de proyecto real
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

# ---

# Paso 2: M (Modelo) - Selección del Cerebro Experto
modelo = GenerativeModel("gemini-2.5-flash")

# ---

# Paso 3: C (Contexto) - Definición de los Datos
tema_principal = "Programación"

contexto_formateado = f"""
- Tema a Explicar: {tema_principal}
"""
# ---

# Paso 4: P (Petición) - Construcción del Prompt
plantilla_prompt = f"""
Actúa como un desarrollador senior y explique brevemente sobre {tema_principal}.
"""

prompt_final = plantilla_prompt.format(contexto_para_usar=contexto_formateado)

# ---

# Paso 5: Ejecución y Resultado
# Se envía la petición al modelo.
respuesta = modelo.generate_content(prompt_final)

# Se imprime ÚNICAMENTE la respuesta final de la IA.
print(respuesta.text)