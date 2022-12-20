from django import forms
class FilmsForms(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"name":'title'}))
    actors = forms.CharField(widget=forms.Textarea(attrs={"name":'actors'}))
    category_id = forms.ChoiceField(choices=((1,'Наука'),(2,'Спорт'),(3,'Комедия')),widget=forms.Select(attrs={"name":'category_id'}))
    date_showed = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"name":'date_showed'}))