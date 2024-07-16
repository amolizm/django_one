from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Hiragana)
admin.site.register(Katakana)
admin.site.register(Kanji)
