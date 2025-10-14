import os
from google.cloud import aiplatform
import vertexai 
from typing import Optional # Importamos esto por si acaso, para evitar errores de tipo.

# --- IMPORTACIONES NECESARIAS PARA VERSIONES ANTIGUAS ---
# Usamos las clases que SÍ existen en tu versión (preview)
from vertexai.preview.generative_models import GenerativeModel 
from vertexai.preview.generative_models import Content # Usaremos Content en lugar de la configuración.

# --- 1. CONFIGURACIÓN Y AUTENTICACIÓN JSON ---
SERVICE_ACCOUNT_PATH = r"C:\Users\Alonso Rojas\Documents\GIT\stone-poetry-473315-a9-9d05006d70af.json" 
PROJECT_ID = "stone-poetry-473315-a9" 
REGION = "us-central1"

try:
    # Autenticación explícita usando el archivo JSON
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_PATH
    
    vertexai.init(project=PROJECT_ID, location=REGION)
    # Inicializamos el modelo para la llamada a la API
    model = GenerativeModel("gemini-2.5-flash")
    
except Exception as e:
    print("Error: Fallo en la inicialización de Vertex AI.")
    print(f"Detalle: {e}")
    exit()

# --- 2. C (Contexto) y P (Petición) ---
TEMA_CONTEXTO = "el gato doméstico" 

PETICION = f"""
Genera un dato curioso y **sorprendente** sobre {TEMA_CONTEXTO}. 
El dato debe ser un solo párrafo corto, no más de dos frases. 
Empieza directamente con el dato sin ninguna introducción como '¿Sabías que...'
"""

# --- 3. M (Modelo) y Ejecución ---
# En versiones antiguas, a veces se define la configuración con un objeto 'contents' más complejo.
# Para simplificar, simplemente no pasaremos el objeto de configuración, ya que es opcional.

print(f"--- 🐙 Buscando Dato Curioso sobre: {TEMA_CONTEXTO.upper()} ---")

try:
    # Llamada a la API (Sin objeto GenerateContentConfig)
    response = model.generate_content(
        contents=PETICION,
        # La temperatura es opcional y podemos omitir el config si da problemas.
    )

    # --- 4. Resultado ---
    print("\n💡 Dato Curioso:")
    print("==========================================")
    print(response.text.strip())
    print("==========================================")
    
except Exception as e:
    print(f"\nError al generar el contenido con la IA: {e}")