from django.urls import path
from .import views

urlpatterns = [
    path('',views.EmpleadosList.as_view(), name = 'empleados_list'),
    path('view/<int:pk>',views.EmpleadosDetail.as_view(), name = 'empleados_view'),
    path('new',views.EmpleadosCreate.as_view(), name = 'empleados_new'),
    path('edit/<int:pk>',views.EmpleadosUpdate.as_view(), name = 'empleados_edit'),
    path('delete/<int:pk>',views.EmpleadosDelete.as_view(), name = 'empleados_delete'),

]