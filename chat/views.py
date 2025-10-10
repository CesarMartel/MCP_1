from django.shortcuts import render
from .graph import generar_respuesta
from .models import guardar_mensaje, obtener_conversacion

def chat_view(request):
    usuario = "default_user"
    ai_response = ""
    user_message = ""

    if request.method == "POST":
        user_message = request.POST.get("mensaje")
        ai_response = generar_respuesta(user_message)
        guardar_mensaje(usuario, user_message, ai_response)

    historial = obtener_conversacion(usuario)
    return render(request, "chat/chat.html", {
        "historial": historial,
        "ai_response": ai_response,
        "user_message": user_message,
    })
