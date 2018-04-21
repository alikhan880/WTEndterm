from django.http import JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from libraryapp.models import Category, Book

# Create your views here.
@csrf_exempt
def categories_list(request):
	if request.method == 'GET':
		list = Category.objects.all()
		json_ans = [t.to_json() for t in list]
		return JsonResponse(json_ans, safe = False)
	elif request.method == 'POST':
		data = request.POST
		category = Category()
		category.title = data.get('title', '')
		category.save()
		return JsonResponse(category.to_json(), status=201)

@csrf_exempt
def categories_detail(request, category_id):
	try:
		c = Category.objects.get(pk = category_id)
		books = Book.objects.filter(category_id=category_id)
		print(books)
	except Exception as e:
		raise JsonResponse({"error" : str(e)}, status = 404)
	if request.method == 'GET':
		resp = [b.to_json() for b in books]
		return JsonResponse(resp, safe = False)
	elif request.method == 'PUT':
		data = QueryDict(request.body)
		c.title = data.get('title', c.title)
		c.save()
		return JsonResponse(c.to_json())
	elif request.method == 'DELETE':
		c.delete()
		return JsonResponse(c.to_json())
	elif request.method == 'POST':
		data = request.POST
		b = Book()
		b.title = data.get('title', '')
		b.author = data.get('author', '')
		b.category_id = c
		b.save()
		return JsonResponse(b.to_json())

@csrf_exempt
def book_detail(request, category_id, book_id):
	if(request.method == 'GET'):
		try:
			book = Book.objects.get(pk = book_id)
			return JsonResponse(book.to_json())
		except Exception as e:
			raise JsonResponse({"error" : str(e)}, status = 404)
	elif request.method == 'PUT':
		try:
			book = Book.objects.get(pk = book_id)
			cat = Category.objects.get(pk = category_id)
			data = QueryDict(request.body)
			book.title = data.get('title', book.title)
			book.author = data.get('author', book.author)
			book.category_id = cat
			book.save()
			return JsonResponse(book.to_json())
			print(books)
		except Exception as e:
			raise JsonResponse({"error" : str(e)}, status = 404)
	elif request.method == 'DELETE':
		try:
			book = Book.objects.get(pk = book_id)
			book.delete()
			return JsonResponse(book.to_json())
			print(books)
		except Exception as e:
			raise JsonResponse({"error" : str(e)}, status = 404)



