# --- IMPORTACIONES REQUERIDAS ---
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig
from google.api_core.exceptions import GoogleAPICallError
import sys # Necesario para manejar argumentos de línea de comandos y sys.exit()

# --- VARIABLES REQUERIDAS ---
# Usa tu ID de proyecto real (usamos el valor que proporcionaste)
PROJECT_ID = "stone-poetry-473315-a9"
LOCATION = "us-central1"

def generar_dato_curioso(entidad):
    

    MODELO = 'gemini-2.5-flash' 
    
    try:
        # 1. Inicialización de Vertex AI 
        vertexai.init(project=PROJECT_ID, location=LOCATION)

        # 2. Cargar el modelo
        model = GenerativeModel(model_name=MODELO)
        
        # --- CONTEXTO (C) ---
        # El contexto debe ir fusionado en el prompt, ya que system_instruction falla.
        CONTEXTO_SISTEMA = (
            "Eres un experto en trivialidades y datos sorprendentes. "
            "Tu única tarea es generar un dato MUY curioso, poco conocido y "
            "sorprendente sobre el tema que se te pide. La respuesta debe ser "
            "solo el dato curioso, sin introducciones, saludos, títulos, "
            "preguntas ni explicaciones adicionales. Debe ser conciso y directo."
        )
        
        # Definición de la configuración de generación (sintaxis antigua)
        generacion_configuracion = GenerationConfig(
            temperature=0.7 
        )

        # --- PETICIÓN (P) ---
        PETICION_FINAL = f"{CONTEXTO_SISTEMA}\n\nGenera un dato curioso y sorprendente sobre: {entidad}"

        # Llamada a la API (solo con contents y generation_config como argumento de keyword)
        response = model.generate_content(
            contents=PETICION_FINAL, 
            generation_config=generacion_configuracion # <-- Este es el argumento clave en versiones antiguas
        )

        return response.text.strip()

    except GoogleAPICallError as e:
        # Si falla con este error, verifica tu autenticación GAC (gcloud auth application-default login)
        return f"❌ Error de Vertex AI. Verifica tu autenticación y permisos en el proyecto. Detalles: {e}"
    except Exception as e:
        return f"❌ Ocurrió un error inesperado: {e}"
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python datos_curiosos_estricto.py \"<Animal/País/Personaje Histórico>\"")
        print("\nEjemplo:")
        print("  python datos_curiosos_estricto.py \"Gatos\"")
        sys.exit(1)
    
    entidad_entrada = " ".join(sys.argv[1:])
    
    print("-" * 50)
    print(f"✨ Buscando un dato curioso sobre: {entidad_entrada}")
    print(f" usando Proyecto: {PROJECT_ID} en Ubicación: {LOCATION}")
    print("-" * 50)
    
    dato = generar_dato_curioso(entidad_entrada)
    
    print("\n💡 DATO CURIOSO:")
    print(dato)
    print("-" * 50)