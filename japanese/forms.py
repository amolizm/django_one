from django import forms

class ButtonClickForm(forms.Form):
    button_clicked = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class InputKana(forms.Form):
    input_value = forms.CharField(widget=forms.HiddenInput, initial=True)