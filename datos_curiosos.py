import vertexai
from vertexai.generative_models import GenerativeModel

def conectar_vertexai(project_id, location):
    # Inicializa la conexión con Vertex AI de forma segura.
    try:
        vertexai.init(project=project_id, location=location)
    except Exception as e:
        print(f"Error al inicializar Vertex AI: {e}")
        exit(1)

def generar_dato_curioso(model_name, tema):
    try:
        model = GenerativeModel(model_name=model_name)

        prompt = (
            f"Actúa como un historiador y antropólogo experto en la cultura de {tema}. "
            f"Sorpréndeme con un dato fascinante y poco conocido sobre su historia, "
            f"cultura o geografía. El dato debe ser conciso, "
            f"verificable y fácil de entender para el público general."
        )

        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al generar el contenido desde la API: {e}"

def main():
    PROJECT_ID = "stone-poetry-473315-a9"
    LOCATION = "us-central1"
    MODEL_NAME = "gemini-2.5-flash"
    
    # 🌟 TEMA CAMBIADO AQUÍ 🌟
    TEMA_SELECCIONADO = "Antigua Roma"

    conectar_vertexai(PROJECT_ID, LOCATION)
    dato_curioso = generar_dato_curioso(MODEL_NAME, TEMA_SELECCIONADO)

    print(f"Dato Curioso sobre: {TEMA_SELECCIONADO}")
    print(dato_curioso)

if __name__ == '__main__':
    main()