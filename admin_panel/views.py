from django.shortcuts import render, redirect, get_object_or_404
from requests import post

from .models import Contact
from .forms import ContactForm
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    template_name = 'admin_panel/index.html'
    context_object_name = 'contact_list'

    def get_queryset(self):
        return Contact.objects.all()


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'admin_panel/contact-detail.html'


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ContactForm()

    return render(request, 'admin_panel/create.html', {'form': form})


def edit(request, pk, template_name='crudapp/edit.html'):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='admin_panel/confirm_delete.html'):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object': contact})
