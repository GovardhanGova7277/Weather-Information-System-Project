
# localhost:8000/demo/

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index_page'), # localhost:8000/demo/  # to display the menu
    path('register/', views.register, name = 'register_page'), # localhost:8000/demo/register/  # is for inserting data
    path('view/', views.view, name = 'view_page'), # localhost:8000/demo/view/  # is for inserting data
    path('disp/', views.disp, name = 'disp_page'), # localhost:8000/demo/disp/
    path('<city>/', views.search, name = 'search_page'),
    # http://localhost:8000/demo/
    # http://localhost:8000/demo/register/
    # 
    #localhost:8000/demo/bangalore/
    #localhost:8000/demo/tumkur/
    #localhost:8000/demo/belgavi/
    #localhost:8000/demo/hassan/
]