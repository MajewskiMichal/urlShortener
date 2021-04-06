from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from .models import Shortener


class AddressCreate(CreateView):
    model = Shortener
    fields = ['url']

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('shortener-detail', kwargs={'pk': form.instance.pk}))
        return HttpResponse("form is not validated")

class AddressDetailView(DetailView):
    model = Shortener
