from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.forms import EmailField
from django.utils.translation import gettext_lazy as _
from django import forms
from modules.accounts.models import RoleChoices
from django.db import transaction
from django.contrib.auth.forms import AuthenticationForm


User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User
        field_classes = {"email": EmailField, "role": forms.ChoiceField}


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    role = forms.ChoiceField(choices=RoleChoices.choices)

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ("email", "role")
        field_classes = {"email": EmailField, "role": forms.ChoiceField}
        error_messages = {
            "email": {"unique": _("This email has already been taken.")},
        }


class UserSignupForm(forms.ModelForm):
    """
    A form for user registration/signup.
    """

    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=156, required=True)
    phone = forms.CharField(max_length=20, required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_confirmation = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput,
    )

    class Meta:
        """
        Meta class for UserSignupForm.

        Specifies the model and fields to be used in the form.
        """

        model = User
        fields = ("name", "phone", "email", "password", "password_confirmation")

    def clean(self):
        """
        Clean method for additional form-wide validation.

        Raises:
            forms.ValidationError: If the passwords do not match.
        Returns:
            dict: The cleaned form data.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError("The passwords do not match.")

        return cleaned_data

    @transaction.atomic
    def save(self, commit=True):
        """
        Save method to create and save a new user instance.

        Args:
            commit (bool): If True, save the user instance to the database.

        Returns:
            User: The created user instance.
        """
        user = super().save(commit=False)
        user.is_active = True
        user.role = RoleChoices.SUPERUSER
        user.phone_no = self.cleaned_data["phone"]
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    """
    A custom authentication form that extends Django's AuthenticationForm.
    """

    email = EmailField(
        label=_("Email address"),
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        fields = ["email", "password"]

    field_order = ["email", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "username" in self.fields:
            del self.fields["username"]
