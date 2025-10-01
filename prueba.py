# Paso 1: Bibliotecas y Configuración
import vertexai
from vertexai.generative_models import GenerativeModel

# Reemplaza con los datos de tu proyecto de Google Cloud
# Asegúrate de haber instalado 'google-cloud-aiplatform'
PROJECT_ID = "stone-poetry-473315-a9" # <--- ¡IMPORTANTE! Reemplaza esto con tu ID de proyecto real
LOCATION = "us-central1"
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

# Paso 2: M (Modelo) - Selección del Cerebro Experto
modelo = GenerativeModel("gemini-2.5-flash")

# Paso 3: C (Contexto) - Definición de los Datos
tema = "Creacion de Prompts correctos" #colocar un tema cualquiera

contexto = f""" 
quiero hacer prompts para elaborar distintos proyectos lo 
mas rapido posible.
"""

# Paso 4: P (Petición) - Construcción del Prompt
prompt = f"""
actua como un experto en la elaboracion de prompts, detalla cuales 
son los pasos para hacer uno, que necesito, etc. 
"""

# Paso 5: Ejecución y Resultado
# Se envía la petición al modelo.
respuesta = modelo.generate_content(contexto)

print(respuesta.text)
