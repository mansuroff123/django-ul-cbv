from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Item
from .forms import ItemForm


# Create: Add a new item
class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('item_list')

# Read: List all items
class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'

# Update: Edit an existing item
class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('item_list')

# Delete: Remove an item
class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('item_list')