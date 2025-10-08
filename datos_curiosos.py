import vertexai
from vertexai.generative_models import GenerativeModel
def conectar_vertexai(project_id, location):
    try:
        vertexai.init(project=project_id, location=location)
    except Exception as e:
        print(f"Error al inicializar Vertex AI: {e}")
        exit(1)
def generar_dato_curioso(model_name, tema):
    try:
        model = GenerativeModel(model_name=model_name)
        prompt = (
            f"Eres un historiador y antropólogo experto en la cultura de {tema}. "
            "Proporciona un dato curioso, poco conocido y verificable sobre su historia, cultura o geografía. "
            "La respuesta debe estar en español claro. Responde exclusivamente en formato JSON válido con las siguientes claves:\n"
            "- titulo: una frase corta (máx. 10 palabras) que resuma el dato;\n"
            "- resumen: una versión muy breve (1-2 líneas) del dato;\n"
            "- detalle: explicación concisa pero completa (máx. 6-8 frases) con contexto histórico o cultural;\n"
            "- fuentes: una lista (array) con 1-3 referencias verificables (URL o nombre de libro/artículo);\n"
            "- fecha_estimada: si aplica, una fecha o periodo aproximado;\n"
            "Instrucciones adicionales: sé preciso, evita especulaciones, y no incluyas texto fuera del JSON. "
            "Si la información no es verificable, indica claramente en el campo 'fuentes' que requiere verificación. "
            "No agregues comentarios ni explicaciones adicionales fuera del JSON."
        )
        response = model.generate_content(prompt)
        text = getattr(response, 'text', None) or getattr(response, 'content', None) or str(response)
        return text
    except Exception as e:
        return f"Error al generar el contenido desde la API: {e}"
def main():
    PROJECT_ID = "stone-poetry-473315-a9"
    LOCATION = "us-central1"
    MODEL_NAME = "gemini-2.5-flash"
    TEMA_SELECCIONADO = "Perú"
    conectar_vertexai(PROJECT_ID, LOCATION)
    dato_curioso = generar_dato_curioso(MODEL_NAME, TEMA_SELECCIONADO)
    print(f"Dato Curioso sobre: {TEMA_SELECCIONADO}")
    print(dato_curioso)
if __name__ == '__main__':
    main()
