from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('faq/',views.faq,name='faq'),
    path('events/',views.events,name='events'),
    path('registration/',views.registration,name='registration'),
    path('contact/',views.contact,name='contact')

]