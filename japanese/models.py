from django.db import models

# Create your models here.


# with a unicode 30BC it can be shown as 
# u'\u30BC'

class Hiragana(models.Model):
    unicode = models.CharField(max_length=8)
    pronounce = models.CharField(max_length=6)

    def __str__(self):
        self.hiragana_text = "Hiragana {}".format(self.pronounce)
        return self.hiragana_text

class Katakana(models.Model):
    unicode = models.CharField(max_length=8)
    pronounce = models.CharField(max_length=6)

    def __str__(self):
        self.katakana_text = "Katakana {}".format(self.pronounce)
        return self.katakana_text

class Kanji(models.Model):
    unicode = models.CharField(max_length=8)
    pronounce = models.CharField(max_length=16)

    def __str__(self):
            self.kanji_text = "Kanji {}".format(self.pronounce)
            return self.kanji_text
