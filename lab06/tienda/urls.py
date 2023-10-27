from django.urls import path

from.import views

app_name ='tienda'

urlpatterns =[
    path('', views.index, name='index'),
    
    # Rutas para categorías
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/<int:categoria_id>/', views.CategoriaDetailView.as_view(), name='categoria_detail'),

    # Rutas para productos
    path('productos/', views.ProductoListView.as_view(), name='producto_list'),
    path('productos/<int:producto_id>/', views.ProductoDetailView.as_view(), name='producto_detail'),

]