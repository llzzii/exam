from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
from app_1 import num_count


def upload(request):
    if request.method == "POST":
        File = request.FILES.get("files", None)
        if File is None:
            return HttpResponse("请选择需要上传的题库文件")
        else:
            with open("./app_1/logs_files/%s" % File.name, 'wb+') as f:
                for chunk in File.chunks():
                    f.write(chunk)
            print(num_count.uploadFile)
            return render(request, "upload.html", {"data": num_count.uploadFile(request).all()})

    else:
        return render(request, "upload.html")


def examAjax(request):
    # return JsonResponse(json.loads(num_count.load(request)), safe=False)
    return render(request, "examAjax.html", {"data": JsonResponse(json.loads(num_count.load(request)), safe=False)})


def examType(request):
    return JsonResponse(json.loads(num_count.getTypeData(request)), safe=False)


def exam(request):
    # return JsonResponse(json.loads(num_count.load(request)), safe=False)
    return render(request, "exam.html", {"data": json.loads(num_count.load(request)), "dataJs": num_count.load(request)})


def examData(request):
    return JsonResponse(json.loads(num_count.load(request)), safe=False)
    # return render(request, "exam.html", {"data": JsonResponse(json.loads(num_count.load(request)), safe=False)})


def examDataBytype(request):
    return JsonResponse(num_count.getDataByType(request))


def examPage(request):
    return render(request, "examPage.html")
