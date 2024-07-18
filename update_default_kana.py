import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning.settings')
django.setup()


from japanese.models import Katakana, Hiragana
from KanaPhonetics import kana

def update_katakana(start_num, end_num):
    for unicode in range(start_num, end_num +1):
        Katakana.objects.create(unicode=unicode, 
                                pronounce=kana.katakana.get(unicode, 'NA'))

def update_hiragana(start_num, end_num):
    for unicode in range(start_num, end_num +1):
        Hiragana.objects.create(unicode=unicode,
                                pronounce=kana.hiragana.get(unicode, "NA"))

update_katakana(start_num= 12449,
                end_num= 12539)

update_hiragana(start_num= 12353,
                end_num= 12436)


# Caution dont do it
# Hiragana.objects.all().delete()
# Katakana.objects.all().delete()
# print(Hiragana.objects.count())
# print(Katakana.objects.count())