from django.urls import path
from . import views


urlpatterns = [
    path("/", views.apiOverview, name="api-overview"),
    path("list/", views.showProducts, name="list"),
    path("list-one/<int:pk>/", views.showProduct, name="list-one"),
    path("item-create", views.createProduct, name="item-create"),
    path("item-update/<int:pk>/", views.updateProduct, name="item-update"),
    path("item-delete/<int:pk>/", views.deleteProduct, name="item-delete"),
]
