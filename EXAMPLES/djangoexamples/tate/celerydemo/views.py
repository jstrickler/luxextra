from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .forms import FeedbackForm

class FeedbackFormView(FormView):
    template_name = "celerydemo/home.html"
    form_class = FeedbackForm
    success_url = reverse_lazy('celerydemo:success')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

class SuccessView(TemplateView):
    template_name =  "celerydemo/success.html"