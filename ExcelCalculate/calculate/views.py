from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def calculate(request):
    file = request.FILES["fileInput"]
    print("# 사용자가 등록한 파일의 이름: ", file)
    return HttpResponse("calculate, calculate function!")