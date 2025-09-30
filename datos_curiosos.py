import vertexai
from vertexai.generative_models import GenerativeModel

# Paso 1: Bibliotecas y Configuración (sin os/sys)
PROJECT_ID = "stone-poetry-473315-a9"
LOCATION = "us-central1"

# Paso 2: M (Modelo)
PRIMARY_MODEL = "gemini-1.5-flash"
FALLBACK_MODEL = "gemini-2.5-flash"

# Paso 3: C (Contexto) - pide el tema de forma obligatoria
try:
	while True:
		_user_input = input("Tema (animal/país/personaje) [obligatorio]: ").strip()
		if _user_input:
			tema = _user_input
			break
		print("Por favor, ingresa un tema válido.")
except Exception:
	raise RuntimeError("Entrada interactiva no disponible: ejecuta en una terminal e ingresa un tema.")

# Paso 4: P (Petición)
prompt = (
	"M (Modelo): Usa 'gemini-1.5-flash' si está disponible.\n"
	f"C (Contexto): El tema es '{tema}'. Puede ser un animal, país o personaje histórico.\n"
	"P (Petición): Devuelve UN solo dato curioso, sorprendente y verificable sobre el tema. "
	"Responde en 1 a 3 frases, en español, sin listas."
)

# --- Decoración consola (sin dependencias externas) ---
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
GRAY = "\033[90m"
# Activa colores ANSI (puedes poner False si tu consola no los soporta)
USE_COLORS = True


def c(text: str, color: str) -> str:
	return f"{color}{text}{RESET}" if USE_COLORS else text


def banner(title: str) -> None:
	line = "=" * (len(title) + 6)
	print(c(line, CYAN))
	print(c(f"== {title} ==", CYAN))
	print(c(line, CYAN))


def print_section(title: str, body: str) -> None:
	print(c(f"\n{title}", BOLD))
	print(c(body, GRAY))


def _wrap_text(text: str, width: int) -> list[str]:
	# Wrapper simple sin dependencias
	lines: list[str] = []
	for raw in text.splitlines():
		line = raw.strip()
		while len(line) > width:
			cut = line.rfind(" ", 0, width)
			if cut == -1:
				cut = width
			lines.append(line[:cut])
			line = line[cut:].lstrip()
		if line:
			lines.append(line)
	if not lines:
		lines.append("")
	return lines


def print_box(title: str, content: str) -> None:
	max_width = 96
	wrapped = _wrap_text(content, max_width)
	width = min(max(len(line) for line in wrapped), max_width)
	bar = "+" + ("-" * (width + 2)) + "+"
	print(c(f"\n{bar}", GREEN))
	print(c(f"| {title:<{width}} |", GREEN))
	print(c(bar, GREEN))
	for line in wrapped:
		print(f"| {line:<{width}} |")
	print(c(bar, GREEN))


def generar_dato_curioso() -> tuple[str, str]:
	vertexai.init(project=PROJECT_ID, location=LOCATION)
	for model_name in (PRIMARY_MODEL, FALLBACK_MODEL):
		try:
			model = GenerativeModel(model_name)
			resp = model.generate_content(prompt)
			texto = resp.text if hasattr(resp, "text") else str(resp)
			return texto, model_name
		except Exception as e:
			last_error = e
			continue
	raise last_error  # type: ignore[name-defined]


if __name__ == "__main__":
	try:
		banner("EJERCICIO MCP #1 · Creador de Datos Curiosos")
		print_section("M (Modelo)", f"Preferido: {PRIMARY_MODEL} · Alternativa: {FALLBACK_MODEL}")
		print_section("C (Contexto)", f"Tema elegido: '{tema}'")
		print_section("P (Petición)", "Un solo dato curioso, 1-3 frases, en español, sin listas.")

		texto, usado = generar_dato_curioso()
		print_box(f"Resultado · Modelo usado: {usado}", texto)
	except Exception as e:
		print(f"\n Ocurrió un error: {e}")
		print("\n   Asegúrate de que:")
		print("   1. GOOGLE_APPLICATION_CREDENTIALS apunte a tu JSON de servicio.")
		print("   2. El ID de proyecto y región son correctos.")
		print("   3. La API de Vertex AI esté habilitada en el proyecto.")