from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Button
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from crispy_forms.helper import FormHelper


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # Přidejte všechna potřebná pole

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Zadejte uživatelské jméno.'
        self.fields['email'].help_text = 'Zadejte platný email.'
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Registrační údaje',
                'username',
                'email',
                'password1',
                'password2',
            ),
            FormActions(
                ButtonHolder(
                    Submit('submit', 'Registrovat', css_class='btn-primary mr-2'),
                    Button('cancel', 'Storno', css_class='btn-secondary',
                           onclick='window.history.back();'),
                    css_class='d-flex'
                )
            ),
        )
