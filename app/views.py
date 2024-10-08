from django.shortcuts import render

from app.forms import OrderForm, LegalServicesForm


def main_page(request):
    return render(request, "main.html")


def order(request):
    if request.method == "GET":
        form = OrderForm()
        return render(request, "order.html", {"form": form})

    form = OrderForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, "success.html")


def legal_services(request):
    if request.method == "GET":
        form = LegalServicesForm()
        return render(request, "legal_services.html", {"form": form})

    form = LegalServicesForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, "success.html")


def international_transportation(request):
    if request.method == "GET":
        form = OrderForm()
        return render(request, "international_order.html", {"form": form})

    form = OrderForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, "success.html")
