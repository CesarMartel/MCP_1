import vertexai
from vertexai.generative_models import GenerativeModel

PROJECT_ID = "stone-poetry-473315-a9"
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

model = GenerativeModel("gemini-2.5-flash")

tema = "Perú"
prompt = f"""
Genera 3 datos curiosos y sorprendentes sobre {tema}.
Respóndeme solo con una lista sencilla, cada dato en una frase clara y breve.
Sin introducciones ni explicaciones adicionales.
"""

response = model.generate_content(prompt)

print("Datos curiosos de Perú:\n")
print(response.text.strip())
