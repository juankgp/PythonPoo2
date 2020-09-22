from django.urls import path
from .import views

urlpatterns = [
    path('userDetails',views.UserDetailsPageView.as_view(), name='userDetails'),
    path('blogDetails',views.BlogDetailsPageView.as_view(), name='blogDetails'),
    path('',views.PiezasList.as_view(), name = 'piezas_list'),
    path('view/<int:pk>',views.PiezasDetail.as_view(), name = 'piezas_view'),
    path('new',views.PiezasCreate.as_view(), name = 'piezas_new'),
    path('edit/<int:pk>',views.PiezasUpdate.as_view(), name = 'piezas_edit'),
    path('delete/<int:pk>',views.PiezasDelete.as_view(), name = 'piezas_delete'),

    path('prove',views.ProveedorList.as_view(), name = 'proveedor_list'),
    path('viewprove/<int:pk>',views.ProveedorDetail.as_view(), name = 'proveedor_view'),
    path('newprove',views.ProveedorCreate.as_view(), name = 'proveedor_new'),
    path('editprove/<int:pk>',views.ProveedorUpdate.as_view(), name = 'proveedor_edit'),
    path('deleteprove/<int:pk>',views.ProveedorDelete.as_view(), name = 'proveedor_delete'),
    

    path('sumi',views.SuministraList.as_view(), name = 'suministra_list'),
    path('viewsumi/<int:pk>',views.SuministraDetail.as_view(), name = 'suministra_view'),
    path('newsumi',views.SuministraCreate.as_view(), name = 'suministra_new'),
    path('editsumi/<int:pk>',views.SuministraUpdate.as_view(), name = 'suministra_edit'),
    path('deletesumi/<int:pk>',views.SuministraDelete.as_view(), name = 'suministra_delete'),
]