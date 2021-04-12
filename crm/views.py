from django.shortcuts import render
from .models import Cars
from .forms import CarsForm

def first_page(request):
    cars_list = Cars.objects.all()
    form = CarsForm()
    return render(request, './index.html', {'cars_list':cars_list, 'form':form})

def alright_page(request):
    brand = request.POST['brand']
    model = request.POST['model']
    elements = Cars(cars_brand = brand, cars_model = model)
    elements.save()
    return render(request, './Alright.html', {'brand':brand, 'model':model})