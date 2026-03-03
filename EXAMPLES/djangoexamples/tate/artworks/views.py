from django.views.generic.base import TemplateView

class WelcomeView(TemplateView):

    template_name = "welcome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'You are now logged in'
        return context
