import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning.settings')
django.setup()


from japanese.models import Katakana, Hiragana
from KanaPhonetics import kana

def update_katakana(start_hex, end_hex):
    for unicode in range(int(start_hex, 16), int(end_hex, 16) +1):
        Katakana.objects.create(unicode=hex(unicode)[2:].lower(), 
                                pronounce=kana.katakana.get(unicode, 'NA'))

def update_hiragana(start_hex, end_hex):
    for unicode in range(int(start_hex, 16), int(end_hex, 16) +1):
        Hiragana.objects.create(unicode=hex(unicode)[2:].lower(), pronounce="Update me !")

update_katakana(start_hex= "30A0",
                end_hex= "30FF")

# update_hiragana(start_hex= "3040",
#                 end_hex= "309F")


# Caution dont do it
# Katakana.objects.all().delete()
