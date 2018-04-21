from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('categories/', views.category_list, name = 'category_list'),
	path('categories/<int:category_id>/', views.category_detail, name = 'category_detail'),
	path('new_category/', views.new_category, name='new_category'),
	path('add_category/', views.add_category, name="add_category"),
	path('edit_category/<int:category_id>/', views.edit_category, name="edit_category"),
	path('save_category/<int:category_id>/', views.save_category, name="save_category"),
	path('delete_category/<int:category_id>/', views.delete_category, name = "delete_category"),
	path('new_book/<int:category_id>', views.new_book, name='new_book'),
	path('add_book/<int:category_id>/', views.add_book, name="add_book"),
	path('edit_book/<int:category_id>/<int:book_id>/', views.edit_book, name="edit_book"),
	path('save_book/<int:category_id>/<int:book_id>/', views.save_book, name="save_book"),
	path('delete_book/<int:category_id>/<int:book_id>/', views.delete_book, name = "delete_book"),
]
