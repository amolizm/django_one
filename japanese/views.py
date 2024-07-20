from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Katakana, Hiragana
from .forms import ButtonClickForm
import random

def get_katakana():
    kana_size = Katakana.objects.count()
    if kana_size !=0:
        kana = Katakana.objects.all()[random.randint(0, kana_size)]
        kana.kanaletter = chr(kana.unicode)
    else:
        kana = "No letters in DB"
    return {"kana_letter": kana}

def get_hiragana():
    kana_size = Hiragana.objects.count()
    if kana_size !=0:
        kana = Hiragana.objects.all()[random.randint(0, kana_size)]
        kana.kanaletter = chr(kana.unicode)
    else:
        kana_letter = "No letters in DB"
    return {"kana_letter": kana}


def index(request):
    return render(request, "japanese/index.html")

def hiragana_index(request):
    context = get_hiragana()
    context['kana_type'] = 'hiragana'
    if request.method == 'POST':
        form = ButtonClickForm(request.POST)
        if form.is_valid() and form.cleaned_data['button_clicked']:
            return render(request, "japanese/kana.html", context)
    else:
        form = ButtonClickForm()
    return render(request, "japanese/kana.html", context)

def katakana_index(request):
    context = get_katakana()
    context['kana_type'] = 'katakana'
    print("Request", request)
    if request.method == 'POST':
        form = ButtonClickForm(request.POST)
        print(form)
        if form.is_valid() and form.cleaned_data['button_clicked']:
            print("this is success !")
            return render(request, "japanese/kana.html", context)
    else:
        form = ButtonClickForm()
    return render(request, "japanese/kana.html", context)

def next_character(request):
    return HttpResponse("Button clicked!")


# def input(request):
#     code = ""
#     context = {"unicode": code}

#     if request.method == 'POST':
#         form = ButtonClickForm(request.POST)
#         if form.is_valid() and form.cleaned_data['button_clicked']:
#             context["submit"] = "Kana submit successfull"
#             # Perform any server-side logic here
#             return render(request, "japanese/input.html", context)
#     else:
#         form = ButtonClickForm()

#     return render(request, "japanese/input.html", context)
