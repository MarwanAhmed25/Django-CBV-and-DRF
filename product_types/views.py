from .models import Type
from .forms import TypeForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

# Create your views here.

class TypeListView(ListView):
    model = Type
    template_name = "types_list.html"

class TypeDetailView(DetailView):
    model = Type
    template_name = "type_detial.html"

class TypeCreateView(CreateView):
    model = Type
    form_class = TypeForm
    template_name = "create_Type.html"
    

class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm
    template_name = "type_update.html"

class TypeDeleteView(DeleteView):
    model = Type
    template_name = "type_delete.html"

