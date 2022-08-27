from app import views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.mlogin,name='login'),
    path('signup/',views.signup),
    path('add/',views.add),
    path('delete/<int:id>',views.mdelete),
    path('update/<int:id>',views.update),
    path('logout/',views.signout)
]
