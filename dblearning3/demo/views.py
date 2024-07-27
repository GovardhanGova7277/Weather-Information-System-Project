from django.shortcuts import render
from .models import Weather # importing the model class 
from django.contrib import messages # importing messages for giving messages
from .forms import AuthorForm


# Create your views here.

def index(request):
    form = AuthorForm(request.POST)

    if form.is_valid():
        form.save()
        
    return render(request, 'index.html', {'form' : form})

# when index method is called we are creting one instance of Author Form and 
# we are saving if it is post method and django will create new form for use

def register(request):

    if request.method == 'POST':
        # when the submit button is clicked
        # retreive the data from form
        
        cname = request.POST['cname']
        temp = request.POST['temp']
        prsr = request.POST['prsr']
        rstatus = request.POST['rainStatus']
        ramt = request.POST['amtOfRain']
        desc = request.POST['desc']

    
        # create an object of your Model class

        obj = Weather()
        
        # use the object to access properties and assign value to them
        # we are assigning retrieved values from form to class fields through object
        obj.cityName = cname
        obj.temperature = temp
        obj.pressure = prsr
        obj.rainPossibility = rstatus
        obj.amountOfRain = ramt
        obj.description = desc
        # save the object
        try:
            obj.save()

            print(obj)

            messages.success(request, 'Weather information added to database')

            info = {'obj':obj}
            return render(request, 'register.html', info)
        
        except Exception as ex:
            messages.error(request, ex)
            return render(request, 'register.html')

    else:
        return render(request, 'register.html')
    


def view(request):
    records = Weather.objects.all() # returns a list like object called queryset
    print(records)
    info = {'records':records}
    return render(request, 'view.html',info)



def disp(request):
    records = Weather.objects.all()
    info = {'records':records}
    return render(request, 'disp.html', info)


def search(request,city): # this we are getting it from disp html page 
    record = Weather.objects.get(cityName = city)    # returns a single object  
    print(record)
    info = {'record':record}
    return render(request, 'search.html', info)    
