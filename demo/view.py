from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {}
    context["hello"] = "你好！"
    context["world"] = "世界"
    return render(request, 'hello.html', context)
