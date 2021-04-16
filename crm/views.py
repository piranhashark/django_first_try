from django.shortcuts import render
from .models import Cars
from .forms import CarsForm
from cms.models import CmsSlider

def first_page(request):
    slider_list = CmsSlider.objects.all()
    return render(request, './index.html', {'slider_list':slider_list,})

def alright_page(request):
    brand = request.POST['brand']
    model = request.POST['model']
    elements = Cars(cars_brand = brand, cars_model = model)
    elements.save()
    return render(request, './Alright.html', {'brand':brand, 'model':model})