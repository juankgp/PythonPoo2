from django.urls import path
from .import views

urlpatterns=[
 
    path('', views.MatriculasList.as_view(), name='matriculas_list'),
    path('View/<int:pk>', views.MatriculasDetail.as_view(), name='matriculas_view'),
    path('new', views.MatriculasCreate.as_view(), name='matriculas_new'),
    path('edit/<int:pk>', views.MatriculasUpdate.as_view(), name='matriculas_edit'),
    path('delete/<int:pk>', views.MatriculasDelete.as_view(), name='matriculas_delete'),

]