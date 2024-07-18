from django.http import HttpResponse
from django.shortcuts import render

from .models import Katakana, Hiragana
from .forms import ButtonClickForm
import random

def get_katakana():
    kana_size = Katakana.objects.count()
    if kana_size !=0:
        kana_letter = Katakana.objects.all()[random.randint(0, kana_size)]
        kana_letter.unicode = chr(int(kana_letter.unicode, 16))
    else: kana_letter = "No letters in DB"
    return {"kana_letter": kana_letter}

def get_hiragana():
    kana_size = Hiragana.objects.count()
    kana_letter = Hiragana.objects.all()[random.randint(0, kana_size)]
    kana_letter.unicode = chr(int(kana_letter.unicode, 16))
    return {"kana_letter": kana_letter}


def index(request):
    context = get_katakana()
    # context = get_hiragana()
    if request.method == 'POST':
        form = ButtonClickForm(request.POST)
        if form.is_valid() and form.cleaned_data['button_clicked']:
            # Perform any server-side logic here
            return render(request, "japanese/index.html", context)
    else:
        form = ButtonClickForm()
    return render(request, "japanese/index.html", context)

def next_character(request):
    # Define your logic here
    return HttpResponse("Button clicked!")


def input(request):
    code = ""
    context = {"unicode": code}

    if request.method == 'POST':
        form = ButtonClickForm(request.POST)
        if form.is_valid() and form.cleaned_data['button_clicked']:
            context["submit"] = "Kana submit successfull"
            # Perform any server-side logic here
            return render(request, "japanese/input.html", context)
    else:
        form = ButtonClickForm()

    return render(request, "japanese/input.html", context)
