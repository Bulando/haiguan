from django.urls import path
from . import views
from .views import DataxListView
app_name = 'testapp'

urlpatterns = [path('', views.index, name='index'),
               path("datax/", DataxListView.as_view()),
               path('datax/<int:year>/', views.detail, name='detail'),
              # path("datax/<int:id>/update/", views.datax_chakan.as_view()),
               ]