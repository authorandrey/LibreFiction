from django.contrib.auth.views import LoginView as BaseLoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, login
from user.forms import UserCreationForm


User = get_user_model()


class LoginView(BaseLoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('main:index')


class RegisterCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
