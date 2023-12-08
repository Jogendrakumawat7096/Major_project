from django.shortcuts import render , redirect
from . models import Signup,User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import random
import requests

# Create your views here.
def index(request):
    return render(request,"index.html")

def product(request):
    return render(request,"product.html")

def shoping_cart(request):
    return render(request,"shoping-cart.html")

def blog(request):
    return render(request,"blog.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def product_detail(request):
    return render(request,"product-detail.html")

def home_02(request):
    return render(request,"home-02.html")


def home_03(request):
    return render(request,"home-03.html")

def login(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email = request.POST['email'])
            
            if check_password(request.POST['password'],user.password):
                request.session['email'] = user.email
                request.session['name']=user.name
                request.session['image'] = user.image.url if user.image else None
                return render(request,"index.html",{'user':user})
            else:
                msg ="password Incorrect"
                return render(request,"login.html",{'msg':msg})
        except:
            msg ="Email Not Registered"
            return render(request,"login.html",{'msg':msg})      
            
    else:      
      return render(request,"login.html")

def signup(request):
    if request.method=="POST":
        try:
            User.objects.get(email = request.POST['email'])
            msg = "Email Is Already Registered , Please Enter Another Email Id"
            return render(request,"signup.html",{'msg':msg})
            
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    name=request.POST['name'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address'],
                    image = request.FILES['image'],
                    password=make_password(request.POST['password']),
                                    
                )
                msg = "Sign Up Successfully"
                return render(request,"login.html",{'msgs':msg}) 
            else:
                msg = "Password or Confirm Password Does Not Matched"
                return render(request,"signup.html",{'msg':msg})     
    else:   
        return render(request,"signup.html")
    

def forgot_password(request):
    if request.method == "POST":
            
        try:
            
            otp = random.randint(1000, 9999)
            mobile = request.POST['mobile'] 
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {
                "authorization": "VlO5sarhU8T76cPG0qMmvxHKYBiJ4DRZInEzfAF3L1pudekWCQf1t4D63AikUrC57TRZdJ8QMgGWbHYS",
                "variables_values": str(otp),
                "route": "otp",
                "numbers": mobile
            }
            headers = {'cache-control': "no-cache"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
            user = User.objects.get(mobile=mobile)
            request.session['mobile'] = mobile
            uotp = make_password(str(otp))
            return render(request, "otp.html", {'otp': uotp})
        except:
            msg = "Mobile Number Not Exists"
            return render(request, "forgot-password.html", {'msg': msg})
    else:
        return render(request, "forgot-password.html")
    
def verify_otp(request):
    otp = request.POST['otp']
    if check_password(request.POST['uotp'],otp):
        return render(request,"new-password.html")
    else:
        msg = "Invalid otp"
        return render(request,"otp.html",{'msg':msg})

def new_password(request):
    if request.POST['new-password']==request.POST['cnew-password']:
        mobile= request.session['mobile']
        user = User.objects.get(mobile=mobile)
        user.password=make_password(request.POST['new-password'])
        user.save()
        return redirect("logout")
    else:
        msg= "password and confirm password does not matched"  
        return render(request,"new-password.html",{'msg':msg})

def logout(request):
    del request.session['email']
    return render(request,"login.html")


def update_profile(request):
    user = User.objects.get(email = request.session['email'])    
    return render(request,"update-profile.html",{'user':user})

def update_data(request):
    if request.method == "POST":
        user = User.objects.get(email=request.session['email'])
        if 'pimage' in request.FILES:
            uploaded_file = request.FILES['pimage']
            save_path = 'user_images/'
            print("Uploaded file name:", uploaded_file.name)
            print("Save path:", save_path)
            file_name = default_storage.save(save_path + uploaded_file.name, ContentFile(uploaded_file.read()))
            user.image = file_name
        user.name = request.POST['name']
        user.mobile = request.POST['mobile']
        user.address = request.POST['address']
        user.save()
        del request.session['image']
        request.session['image'] = user.image.url if user.image else None
        msg = "Profile update successful"
        return render(request, "update-profile.html", {'msg': msg, 'user': user})
    else:
        return render(request, "update-profile.html")
    
def change_password(request):
    if request.method=='POST':
        user = User.objects.get(email=request.session['email'])
        if check_password(request.POST['old-password'],user.password):
            if request.POST['new-password']==request.POST['cnew-password']:
                user.password=make_password(request.POST['new-password'])                
                user.save()
                del request.session['email']
                msgs= "password Upadate successfull"
                return render(request,"login.html",{'msgs':msgs})
            else:
                msg= "password or confirm password not matched"
                return render(request,"change-password.html",{msg:'msg'})
        else:
            msg= "old Password Does Not Matched"
            return render(request,"change-password.html",{msg:'msg'})
    else:   
        return render(request,"change-password.html")