from . import views
from django.urls import path

app_name= 'adoptions'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:cat_id>/', views.detail, name='detail' ),
    path('contact/', views.contact, name='contact'),
    path('recently-adopted/', views.recently_adopted, name='recently-adopted'),
    path('<int:cat_id>/adopt-cat/', views.adopt_cat, name='adopt-cat'),
]