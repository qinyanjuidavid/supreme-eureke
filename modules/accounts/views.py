from django.contrib.auth import authenticate, login
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from modules.accounts.models import RoleChoices, User
from modules.accounts.forms import CustomAuthenticationForm, UserSignupForm


class SignupView(CreateView):
    """
    View for user registration/signup.
    """

    model = User
    form_class = UserSignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")

    def get_context_data(self, **kwargs):
        """
        Get the context data for rendering the template.
        """
        kwargs["user_type"] = RoleChoices.SUPERUSER
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        """
        Process a valid form submission.
        """
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))


def loginView(request):
    """
    View for user login.
    """
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login success.")
                # Redirect to the success page.
                return HttpResponseRedirect(reverse("accounts:home"))
    else:
        form = CustomAuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})


@login_required
def HomeView(request):
    """
    View for the home page.
    """
    userQuery = User.objects.all()
    context = {
        "users": userQuery,
    }
    return render(request, "pages/home.html", context)
