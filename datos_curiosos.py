import vertexai
from vertexai.generative_models import GenerativeModel

PROYECT_ID = "stone-poetry-473315-a9"
LOCATION = "us-central1"

vertexai.init(project=PROYECT_ID, location=LOCATION)

modelo = GenerativeModel("gemini-2.5-flash")

tema_principal = "datos curiosos sobre el espacio"
concepto = "planetas del sistema solar y sus características únicas"

contexto = f"Tema a explicar: {tema_principal} relacionados con {concepto}."

prompt = f"""
Eres un experto en astronomía y divulgación científica. 
Tu tarea es crear una lista de 5 datos curiosos sobre {tema_principal} relacionados con {concepto}.
Cada dato debe ser breve, interesante y fácil de entender para un público general.
Asegúrate de que los datos sean variados y cubran diferentes aspectos del tema.
Preséntalos en una lista numerada.
Contexto adicional: {contexto}
"""

respuesta = modelo.generate_content(prompt_final := prompt)

print(respuesta.text)
