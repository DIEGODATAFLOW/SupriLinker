from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # fields = "__all__"
        # ^
        # hack -> O '__all__' é um atalho especial no Django que significa "incluir todos os campos do modelo"
        # hack -> no formulário. Quando usado, o Django automaticamente incluirá todos os campos do modelo
        # hack -> especificado (neste caso, o modelo User) no formulário gerado.

        fields = ["username", "email", "password1", "password2"]
