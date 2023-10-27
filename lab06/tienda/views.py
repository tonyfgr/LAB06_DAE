from django.shortcuts import get_object_or_404, render
from .models import Producto, Categoria
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CategoriaSerializer, ProductoSerializer
# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias = Categoria.objects.all()  # Obtener todas las categorías
    context = {'product_list': product_list, 'categorias': categorias}
    return render(request, 'index.html', context)


def producto(request, producto_id):
    producto= get_object_or_404(Producto, pk=producto_id)
    return render(request,'producto.html', {'producto': producto})

def productos_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    context = {'categoria': categoria, 'productos': productos}
    return render(request, 'productos_categoria.html', context)


class CategoriaListView(APIView):
    
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

class CategoriaDetailView(APIView):
    
    def get(self, request, categoria_id):
        categoria = Categoria.objects.get(pk=categoria_id)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    
    def put(self, request, categoria_id):
        categoria = Categoria.objects.get(pk=categoria_id)
        serializer = CategoriaSerializer(categoria, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, categoria_id):
        categoria = Categoria.objects.get(pk=categoria_id)
        categoria.delete()
        return Response(status=204)

class ProductoListView(APIView):
    
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

class ProductoDetailView(APIView):
    
    def get(self, request, producto_id):
        producto = Producto.objects.get(pk=producto_id)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    def put(self, request, producto_id):
        producto = Producto.objects.get(pk=producto_id)
        serializer = ProductoSerializer(producto, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, producto_id):
        producto = Producto.objects.get(pk=producto_id)
        producto.delete()
        return Response(status=204)