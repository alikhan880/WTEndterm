from django.urls import path, include
from . import views

urlpatterns = [
	path('categories/', views.categories_list),
	path('categories/<int:category_id>/', views.categories_detail),
	path('categories/<int:category_id>/<int:book_id>/', views.book_detail)
]
