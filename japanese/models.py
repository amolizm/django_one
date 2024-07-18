from django.db import models

class Hiragana(models.Model):
    unicode = models.IntegerField()
    pronounce = models.CharField(max_length=6)
    kanaletter = models.CharField(max_length=8, default='NA')

    def __str__(self):
        self.hiragana_text = "Hiragana {}".format(self.pronounce)
        return self.hiragana_text

class Katakana(models.Model):
    unicode = models.IntegerField()
    pronounce = models.CharField(max_length=6)
    kanaletter = models.CharField(max_length=8, default='NA')

    def __str__(self):
        self.katakana_text = "Katakana {}".format(self.pronounce)
        return self.katakana_text

class Kanji(models.Model):
    unicode = models.IntegerField()
    pronounce = models.CharField(max_length=16)

    def __str__(self):
            self.kanji_text = "Kanji {}".format(self.pronounce)
            return self.kanji_text
