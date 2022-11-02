from random import choices
from secrets import choice
from django import forms


class FormArticle(forms.Form):

    title = forms.CharField(
        label="Titulo",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Mete el titulo", "class": "titulo_form_article"}
        ),
    )

    content = forms.CharField(label="Contenido", widget=forms.Textarea)
    content.widget.attrs.update(
        {
            "placeholder": "Mete el contenido",
            "class": "contenido_form_article",
            "id": 'contenido_form'
        }
    )

    public_options = [(1, "si"), (0, "no")]

    public = forms.TypedChoiceField(label="Publicado", choices=public_options)
