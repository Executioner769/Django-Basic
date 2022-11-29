from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item
from .forms import ItemForm

@login_required
def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def secret_page(request):
    Items = Item.objects.all()
    return render(request, 'secret_page.html', {
        'items' : Items
    })

@login_required
def edit(request):
    if(request.method=="POST"):
        return render(request,'edit.html')
    else:
        form = ItemForm()
        return render(request, 'edit.html', {
        'form': form})
        

def item(request):
    if(request.method=="POST"):
        print('hit')
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('admin')
    else:
        return render('admin')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'
