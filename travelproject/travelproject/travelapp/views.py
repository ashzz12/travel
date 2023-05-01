from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, team


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=team.objects.all()
    # name="india"
    return render(request,"index.html",{'result':obj,'result2':obj2})


                  # {'obj':name})
# def operations(request):
#     x = int(request.GET.get('num1'))
#     y = int(request.GET.get('num2'))
#     result=x+y
#     result1=x-y
#     result2=x*y
#     result3=x/y
#     return render(request,"additionresult.html",{'result': result,'result1':result1,'result2':result2,'result3':result3})

    # return render(request, "additionresult.html", {'result': result}, "substraction.html",
    #            {'subtraction  result': result1},"multiplication.html", {'result': result2},"division.html", {'result': result3})

#     x=int(request.GET.get('num1'))
#     y=int(request.GET.get('num2'))
#     result=x+y
#     return render(request,"additionresult.html",{'result': result})
#
# def subtraction(request):
#     x = int(request.GET.get('num1'))
#     y = int(request.GET.get('num2'))
#     result1 = x-y
#     return render(request,"additionresult.html",{'result': result},"substraction.html" ,{'subtraction  result':result1})
# #
# def multiplication(request):
#     x = int(request.GET.get('num1'))
#     y = int(request.GET.get('num2'))
#     mul = x*y
#     return render(request,{'multiplication result': mul})
#
# def division(request):
#     x = int(request.GET.get('num1'))
#     y = int(request.GET.get('num2'))
#     di = x/y
#     return render(request,{'division result':div})