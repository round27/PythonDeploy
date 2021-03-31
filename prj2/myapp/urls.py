
from django.contrib import admin
from django.urls import path
from myapp import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'myapp'

urlpatterns = [
    
    path('details/<int:id>', views.show,name='details'),
    path('index/', views.index,name='index'),
    path('create/', views.create,name='create'),
    path('edit/<int:id>', views.edit,name='edit'),
    path('update/<int:id>', views.update,name='update'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('send/',views.sendEmail,name='sendEmail'),

]
