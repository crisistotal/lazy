from django.urls import path
from .views import ArticuloListView, ArticuloDetailView, ArticuloCreateView, ArticuloUpdateView, ArticuloDeleteView

articulo_patterns =([
    path('', ArticuloListView.as_view(), name='articulos'),
    path('<int:pk>/<slug:slug>', ArticuloDetailView.as_view(),name='articulo'),
    path('create/',ArticuloCreateView.as_view(),name='create'),
    path('update/<int:pk>/', ArticuloUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/', ArticuloDeleteView.as_view(),name='delete'),
], 'articulo')

