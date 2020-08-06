from django.shortcuts import render
import requests

# Create your views here.

def base(request):
    return render(request, 'base.html')

def insult(request):
    url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
    response = requests.get(url)
    data = response.json()
    ins = data['insult']
    return render(request, 'insult.html', {"insult": ins})

def advice(request):
    url = 'https://api.adviceslip.com/advice'
    response = requests.get(url)
    data = response.json()
    print(data)
    adv = data['slip']['advice']
    return render(request, 'advice.html', {"advice": adv})
