from django import forms 

class DeleteConfirmForm(froms.Form):
    check = forms.BooleanField(label='您確定要刪除嗎?')