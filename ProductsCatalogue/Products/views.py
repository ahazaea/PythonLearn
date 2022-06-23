from django.shortcuts import get_object_or_404, render, redirect
from .forms import NewUserForm
from .models import product
from django.contrib.auth import login
from django.contrib import messages


def home(request):
    products= product.objects.all()
    return render(request, "main/home.html",{"products": products})

def detail(request, id):
    prod = get_object_or_404(product, pk=id)
    return render(request, "main/detail.html", {"product": prod})
    
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
    messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "main/register.html", {"register_form": form})
