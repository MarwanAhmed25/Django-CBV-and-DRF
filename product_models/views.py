from .models import BrandModel
from .forms import Model_Form
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

# Create your views here.

class Model_ListView(ListView):
    model = BrandModel
    template_name = "models_list.html"

class Model_DetailView(DetailView):
    model = BrandModel
    template_name = "model_detial.html"

class Model_CreateView(CreateView):
    model = BrandModel
    form_class = Model_Form
    template_name = "create_model.html"

class Model_UpdateView(UpdateView):
    model = BrandModel
    form_class = Model_Form
    template_name = "model_update.html"

class Model_DeleteView(DeleteView):
    model = BrandModel
    template_name = "model_delete.html"

