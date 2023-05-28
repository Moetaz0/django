from rest_framework import routers
from django.urls import include, path
from .views import CategoryAPIView, ProductViewset, ProduitAPIView
from . import views
router = routers.SimpleRouter()
router.register('produit', ProductViewset, basename='produit')
urlpatterns = [ 
    path('', views.index, name='index'),
    path('mag', views.mag, name='mag'),
    path('vitrine', views.vitrine, name='vitrine'),
    path('order', views.order, name='order'),
    path('nouveauFournisseur', views.nouveauFournisseur, name='nouveauFournisseur'),
    path('register/',views.register, name = 'register'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitAPIView.as_view(), name='produits-api'),
    path('listF/', views.listeFournisseurs, name='listF'),
    path('api/', include(router.urls)),
]

