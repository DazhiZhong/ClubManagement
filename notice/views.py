from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from .forms import *


def home(request):
    if request.POST:
        n = NoticeForm(request.POST)
        if n.is_valid():
            n.save()
    tmpl_vars = {'form': NoticeForm()}
    return render(request, 'notice/index.html', tmpl_vars)


@api_view(['GET'])
def notice_collection(request):
    if request.method == 'GET':
        posts = Notice.objects.all()
        serializer = NoticeSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def notice_element(request, pk):
    try:
        post = Notice.objects.get(pk=pk)
    except Notice.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NoticeSerializer(post)
        return Response(serializer.data)

@api_view(['POST'])
def notice_element_create(request):
    if request.POST:
        print(request.POST)
        n = NoticeSerializer(data=request.POST)
        if n.is_valid():
            n.save()
        return Response(n.data, status=status.HTTP_201_CREATED)
    else:
        return redirect('notice_collection')


