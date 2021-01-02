from django.shortcuts import render, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ItemsModel
from .serializers import ItemSerializer

# Create your views here.


@csrf_exempt
def ItemsView(request):

    if request.method == 'GET':
        items = ItemsModel.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def ItemView(request, nm):
    try:
        item = ItemsModel.objects.get(id=nm)
    except ItemsModel.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(item, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == "DELETE":
        item.delete()
        return HttpResponse(status=204)


def sayHello(request):
    html = '''<h1>Hello There This is a HTML file</h1><img src="lena.png" alt="picture" width = "104" height="142">'''
    return HttpResponse(html, status=200)


def Books(request):
    return HttpResponse("This is a books webpage")


def BookID(request, bookid):
    return HttpResponse(f"The book ID is:{bookid}")
