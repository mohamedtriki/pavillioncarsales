from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import vehicle,make,model
from django.http import JsonResponse


#import pagination stuff 
from django.core.paginator import Paginator
#form stuff
from .forms import contactForm

from django.core.mail import send_mail
# Create your views here.



def home(request):
    submited=False
    if request.method == "POST":
        form= contactForm(request.POST)
        if form.is_valid():
            form.save()
            contact_name= form.cleaned_data.get("name")
            contact_phone= form.cleaned_data.get("phone")
            contact_email= form.cleaned_data.get("email")
            contact_message="phone: "+contact_phone+"\n"+"message: "+ form.cleaned_data.get("message")+"\n"+"email: "+contact_email
            send_mail(contact_name,contact_message,contact_email,['itsmohamedtriki@gmail.com',])
            return HttpResponseRedirect("?submited=True")
    else:
        form= contactForm
        if "submited" in request.GET:
            submited=True
    return render(request,'index.html',{"form":form,"submited":submited})



def is_valid_queryparam(para):
    return para!='' and para is not None

def finance(request):
    return render(request,'finance.html')
def vehicles(request):
    vehiclee=vehicle.objects.all()
    makes=vehicle.objects.values('make').distinct()
    transmissions=vehicle.objects.values('transmission').distinct()
    fuels=vehicle.objects.values('fuel_type').distinct()
    count=vehiclee.count()
    make=request.GET.get('make')
    model=request.GET.get('model')
    transmission=request.GET.get('transmission')
    fuel=request.GET.get('fuel')
    min_price=request.GET.get('min_price')
    max_price=request.GET.get('max_price')

    if is_valid_queryparam(make) and make!='-----':
        vehiclee=vehiclee.filter(make_id=make)

    if is_valid_queryparam(model) and model!='-----':
        vehiclee=vehiclee.filter(model_id=model)

    if is_valid_queryparam(fuel) and fuel!='-----':
        vehiclee=vehiclee.filter(fuel_type=fuel)

    if is_valid_queryparam(transmission) and transmission!='-----':
        vehiclee=vehiclee.filter(transmission=transmission)

    if is_valid_queryparam(min_price) and min_price!='-----':
        vehiclee=vehiclee.filter(price__gte=min_price)

    if is_valid_queryparam(max_price) and max_price!='-----':
        vehiclee=vehiclee.filter(price__lt=max_price)

    #set up pagination
    p = Paginator(vehiclee,20)
    page= request.GET.get('page')
    cars=p.get_page(page)


    t={"vehicle":cars,"cars":cars,"count":count ,"makes":makes,"transmissions":transmissions,"fuels":fuels}
    return render(request,'vehicles.html',t)



def vehicle_detail(request,slug):
    t={"vehicle":vehicle.objects.get(slug=slug)}
    return render(request,'vehicle_detail.html',t)

def get_json_car_data(request):
    available_qs =list(vehicle.objects.values('make_id').distinct())
    qs_val = list(make.objects.values())
    return JsonResponse({'data':qs_val,"vehicle":available_qs})

def get_json_model_data(request, *args, **kwargs):
    selected_car = kwargs.get('car')
    obj_models = list(model.objects.filter(make_id=selected_car).values())
    return JsonResponse({'data':obj_models})

