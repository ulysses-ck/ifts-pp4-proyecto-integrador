from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class LandingPageView(TemplateView):
    template_name = 'landing.html' 


class MyLoginRequiredMixin(LoginRequiredMixin):
    login_url = "/user/login"