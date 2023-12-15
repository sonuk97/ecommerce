from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from ecommerceapp.models import category,product,member
from ecommerceapp.models import cart

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')



def admin_home(request):
    return render(request,'admin_home.html')


def user_home(request):
    cat=category.objects.all()
    current_user = request.user.id
    mem=member.objects.filter(user_id=current_user)
    return render(request,'user_home.html',{'mem':mem,'cat':cat})

def add_category(request):
    return render(request,'add_category.html')

def add_product(request):
    cat=category.objects.all()
    return render(request,'add_product.html',{'cat':cat})

def show_product(request):
    prod=product.objects.all()
    return render(request,'show_product.html',{'prod':prod})
def user_signup(request):
    return render(request,'user_signup.html')

def user_details(request):
    mem=member.objects.all()
    return render(request,'user_details.html',{'mem':mem})

def all_products(request):
    prod=product.objects.all()
    cat=category.objects.all()
    current_user = request.user.id
    mem=member.objects.filter(user_id=current_user)
    return render(request,'all_products.html',{'mem':mem,'cat':cat,"prod":prod})
@login_required(login_url='login')
def Cart(request):
    current_user = request.user.id
    mem=member.objects.filter(user_id=current_user)
    item = cart.objects.filter(user_id=current_user)
    cat=category.objects.all()
    return render(request,'Cart.html',{'user':item,'cat':cat,'mem':mem})

def log_in(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request)
                return redirect('admin_home')
            else:
                
                auth.login(request,user)
                messages.info(request,f'WELCOME {username}')
                return redirect('user_home')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request,'index.html')
    
   
def addc(request):
    
        if request.method=="POST":
            category_name=request.POST['cname']
            cat=category(category_name=category_name)
            cat.save()
            messages.info(request,"Category Added")
            return redirect('add_category')
        
       
def add_pro(request):
    
        if request.method == 'POST':
            name = request.POST.get('pname')
            des = request.POST.get('pdes')
            price = request.POST.get('price')
            sel = request.POST.get('sel')
            cat = category.objects.get(id=sel)
            image = request.FILES.get('file')
            prod = product(name=name,description=des,price=price,image=image,category=cat)
            prod.save()
            messages.info(request, "Product Added")
            return redirect('add_product')
        
        
def delete_prod(request,pk):
    
        dele=product.objects.get(id=pk)
        dele.delete()
        return redirect('show_product')
    
    
def add_user(request):
    
        if request.method == 'POST':
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            username = request.POST.get('uname')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')
            address = request.POST.get('address')
            email = request.POST.get('email')
            cnumber = request.POST.get('number')
            image = request.FILES.get('file')

            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username already exists")
                    return redirect('user_signup')
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=fname, last_name=lname)
                    user.save()
                    user1 = member(address=address, number=cnumber, image=image, user=user)
                    user1.save()
                    return render(request,'index.html')
            else:
                messages.info(request, "Password does not match")
                return redirect('user_signup')
            
            
def delete_user(request,pk):
    
        dele=member.objects.get(id=pk)
        dele.delete()
        dele.user.delete()
        return redirect('user_details')
    
    
def add_to_cart(request, pk):
    product_instance = get_object_or_404(product, id=pk)
    user_instance = get_object_or_404(User, id=request.user.id)
    cart_item, created = cart.objects.get_or_create(user=user_instance, product=product_instance)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('user_home')

    
def log_out(request):
    
        auth.logout(request)
        return render(request,'index.html')
    
    
def remove_from_cart(request,pk):
    item=cart.objects.filter(product_id=pk)
    item.delete()
    return redirect('Cart')


def category_detail(request,pk):
    prod=product.objects.filter(category_id=pk)
    cat=category.objects.all()
    current_user = request.user.id
    mem=member.objects.filter(user_id=current_user)
    return render(request,'category_detail.html',{'mem':mem,'cat':cat,"prod":prod})
    