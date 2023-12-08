from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('',views.index,name="index"),
    path('product/',views.product,name="product"),
    path('shoping-cart/',views.shoping_cart,name="shoping-cart"),
    path('blog/',views.blog,name="blog"),    
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('product-detail/',views.product_detail,name="product-detail"),
    path('home-02/',views.home_02,name="home-02"),
    path('home-03/',views.home_03,name="home-03"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('forgot-password/',views.forgot_password,name="forgot-password"),
    path('verify-otp/',views.verify_otp,name="verify-otp"),
    path('new-password/',views.new_password,name="new-password"),
    path('logout/',views.logout,name="logout"),
    path('update-profile/',views.update_profile,name="update-profile"),
    path('update_data/',views.update_data,name="update_data"),
    path('change-password/',views.change_password,name="change-password"),
      
 
 
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)