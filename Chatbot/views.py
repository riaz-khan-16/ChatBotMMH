from django.shortcuts import render
from django.http import request,JsonResponse

# Create your views here.

def home(request):
    return render(request,"index.html")

def ai_response(request):
    if request.method == "POST":
        # Get the user message from request
        user_message = request.POST.get("message", "")
        # Simple rule-based response
        if "hello" in user_message.lower():
            reply = "Hi there! How can I help you?"
        elif "bye" in user_message.lower():
            reply = "Goodbye! Have a nice day!"
        else:
            reply = "Sorry, I don't understand that."
        # Return JSON response
        return JsonResponse({"reply": reply})
    return JsonResponse({"reply": "Invalid request."})
