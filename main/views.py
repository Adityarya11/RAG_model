from django.shortcuts import render
from django.http import HttpResponse
from ..Model.parse import process_question
# Create your views here.


def load_frontend(request):
    return render(request, 'index.html')   

def submit_prompt(request):
    if request.method == 'POST':
        question = request.POST.get('prompt')
        parsed_result = process_question(question)
        return render(request, 'index.html', {'result': parsed_result})
    
