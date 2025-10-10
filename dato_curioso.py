import vertexai
from vertexai.generative_models import GenerativeModel

# Paso 1: Configuración básica
PROJECT_ID = "stone-poetry-473315-a9"
LOCATION = "us-central1"

# Paso 2: Modelos
PRIMARY_MODEL = "gemini-1.5-flash"
FALLBACK_MODEL = "gemini-2.5-flash"

# Paso 3: Tema obligatorio
try:
	while True:
		_user_input = input("Tema (animal/país/personaje) [obligatorio]: ").strip().lower()
		if _user_input in ("animal", "país", "pais", "personaje"):
			tema = _user_input.replace("pais", "país")
			break
		print("Por favor, ingresa 'animal', 'país' o 'personaje'.")
except Exception:
	raise RuntimeError("Entrada interactiva no disponible: ejecuta en una terminal e ingresa un tema.")

# Paso 4: Prompt base
prompt = (
	f"M (Modelo): Usa '{PRIMARY_MODEL}' si está disponible.\n"
	f"C (Contexto): El tema es '{tema}'. Puede ser un animal, país o personaje histórico.\n"
	"P (Petición): Devuelve UN solo dato curioso, sorprendente y verificable sobre el tema. "
	"Responde en 1 a 3 frases, en español, sin listas."
)

# --- Decoración consola ---
RESET = "\033[0m"; BOLD = "\033[1m"; CYAN = "\033[36m"
GREEN = "\033[32m"; YELLOW = "\033[33m"; GRAY = "\033[90m"
USE_COLORS = True
def c(t, col): return f"{col}{t}{RESET}" if USE_COLORS else t

def banner(t): line = "="*(len(t)+6); print(c(line,CYAN)); print(c(f"== {t} ==",CYAN)); print(c(line,CYAN))
def print_section(t,b): print(c(f"\n{t}",BOLD)); print(c(b,GRAY))
def _wrap_text(txt,w):
	lines=[]; 
	for raw in txt.splitlines():
		line=raw.strip()
		while len(line)>w:
			cut=line.rfind(" ",0,w)
			if cut==-1: cut=w
			lines.append(line[:cut]); line=line[cut:].lstrip()
		if line: lines.append(line)
	return lines or [""]
def print_box(title, content):
	max_width=96; wrapped=_wrap_text(content,max_width)
	width=min(max(len(l) for l in wrapped),max_width)
	bar="+"+("-"*(width+2))+"+"
	print(c(f"\n{bar}",GREEN)); print(c(f"| {title:<{width}} |",GREEN)); print(c(bar,GREEN))
	for l in wrapped: print(f"| {l:<{width}} |")
	print(c(bar,GREEN))

# --- Nueva función: chequeo de relevancia ---
def es_relevante(texto: str, tema: str) -> bool:
	texto_lower = texto.lower()
	if tema == "país":
		return any(p in texto_lower for p in ["país", "nación", "territorio", "capital", "frontera", "bandera"])
	elif tema == "animal":
		return any(p in texto_lower for p in ["animal", "mamífero", "ave", "pez", "reptil", "insecto", "especie"])
	elif tema == "personaje":
		return any(p in texto_lower for p in ["persona", "histórico", "nació", "murió", "famoso", "biografía"])
	return True

# --- Generador con verificación ---
def generar_dato_curioso() -> tuple[str, str, bool]:
	vertexai.init(project=PROJECT_ID, location=LOCATION)
	last_error = None
	for model_name in (PRIMARY_MODEL, FALLBACK_MODEL):
		try:
			model = GenerativeModel(model_name)
			resp = model.generate_content(prompt)
			texto = resp.text if hasattr(resp, "text") else str(resp)
			return texto.strip(), model_name, es_relevante(texto, tema)
		except Exception as e:
			last_error = e
	if last_error:
		raise last_error

# --- Ejecución principal ---
if __name__ == "__main__":
	try:
		banner("EJERCICIO MCP #1 · Creador de Datos Curiosos")
		print_section("M (Modelo)", f"Preferido: {PRIMARY_MODEL} · Alternativa: {FALLBACK_MODEL}")
		print_section("C (Contexto)", f"Tema elegido: '{tema}'")
		print_section("P (Petición)", "Un solo dato curioso, 1-3 frases, en español, sin listas.")

		texto, usado, ok = generar_dato_curioso()
		print_box(f"Resultado · Modelo usado: {usado}", texto)

		if not ok:
			print(c("\n⚠ Posible desvío de tema: la respuesta podría no estar relacionada con el tema elegido.", YELLOW))
			print(c("   Puedes volver a ejecutar el programa para intentar otra respuesta.", GRAY))

	except Exception as e:
		print(f"\n Ocurrió un error: {e}")
		print("\n   Asegúrate de que:")
		print("   1. GOOGLE_APPLICATION_CREDENTIALS apunte a tu JSON de servicio.")
		print("   2. El ID de proyecto y región son correctos.")
		print("   3. La API de Vertex AI esté habilitada en el proyecto.")
