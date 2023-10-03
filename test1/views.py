from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ContactForm



# Create your views here.

def home(request):
    myproduct = Product.objects.all()
    paginator = Paginator(myproduct, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'test1/home.html',{'page_obj':page_obj})


   #Filter  starts
   
def  allproducts(request):
    if request.method == 'GET':
        myproducts = Product.objects.all()
        return render(request,"test1/filter.html",{'x':myproducts})
    else:
        z = request.POST.get('myfood')
        # print (z)
        m = float(request.POST.get('price_range'))
        # print(m)
        if(z=='Select'):
            k = Product.objects.filter( price__lte=m )
        # k = Product.objects.filter(category=z)
        else:
            k = Product.objects.filter(category=z, price__lte=m )
        # print(k)
        # return HttpResponse('Hello')
        return render(request, "test1/filter.html", {'x': k,'j':m})
    
    #filter ends

def demo(request):
    myproduct = Product.objects.all()
    return render(request,'test1/demo.html',{'x':myproduct})

def signup1(request):
    if request.method == 'GET':
        return render(request,'test1/signup.html',{'form':UserCreationForm()})
    else:
        if(request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('login1')
            except IntegrityError:
                return render(request,'test1/signup.html',{'form':UserCreationForm(),'y':'Username already taken'})
            
        else:
            return render(request,'test1/signup.html',{'form':UserCreationForm(),'z':'Passwords Unmatched'})


       

def login1(request):
    if request.method == 'GET':
        return render(request,'test1/login.html',{'form':AuthenticationForm()})
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'test1/login.html',{'form':AuthenticationForm(),'k':'Invalid Username or Password!'})


def logout1(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def contactus(request):
    form = ContactForm
    return render(request, 'test1/contactus.html',{'form': form})

def add_record(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Data Added Successfully</h2>')
        


# @login_required(login_url='login1')
def details(request,pid):
    if request.user.is_authenticated:
        myproduct = get_object_or_404(Product,pk=pid)
        return render(request,'test1/details.html',{'z':myproduct})
    else:
        if request.method == 'GET':
            return render(request,'test1/login.html',{'form':AuthenticationForm(),'o':'Login Required!'})
        else:
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request,'test1/login.html',{'form':AuthenticationForm(),'k':'Invalid Username or Password!'})

def aboutus(request):
        return render(request,'test1/aboutus.html')



def search(request):
    # query = request.GET['query']
    if request.method == 'POST':
        query = request.POST.get('search1')
        # query = request.GET('search1')
        print(query)
        if len(query) > 0 :
            if Product.objects.filter(Title__icontains=query) | Product.objects.filter( category__icontains=query):
                if(Product.objects.filter(Title__icontains=query)):
                    k = Product.objects.filter(Title__icontains=query)
                    return render(request,"test1/search.html",{'x':k})
                if(Product.objects.filter(category__icontains=query)):
                    k = Product.objects.filter(category__icontains=query)
                    return render(request,"test1/search.html",{'x':k})
            else:
                return render(request,'test1/search.html',{'o':'Item Not Available'})
        else:
            return redirect("show")

def show(request):
    myproducts = Product.objects.all()
    return render(request,"test1/search.html",{'x':myproducts})
