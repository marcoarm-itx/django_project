from django import forms
from django.core import validators


class FormArticle(forms.Form):
    title = forms.CharField(
        label="Titulo",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Introduce el Título'
            }
        ),
        validators=[
            validators.MinLengthValidator(20, 'El título es demasiado corto'),
            validators.RegexValidator('[A-Za-z0-9ñ ]*$', 'El titulo está mal formado', 'invalid_title')
        ]
    )
    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,

    )

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]
    public = forms.TypedChoiceField(
        label="¿Publicado?",
        choices=public_options
    )
