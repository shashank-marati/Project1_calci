from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inp(request):
    return render(request, 'calcci.html')

def cal(request):
    x = request.POST['t1']
    y = request.POST['t2']
    x = int(x)
    y = int(y)
    optype = request.POST['op']
    if optype == "ADD":
        z = x+y
        res = "The Addition of two number are "+str(z)
    elif optype == "SUB":
        z = x-y
        res = "The Subtraction of two number are "+str(z)
    elif optype == "MUL":
        z = x*y
        res = "The Multiplication of two number are "+str(z)
    elif optype == "DIV":
        z = x/y
        res = "The Division of two number are "+str(z)
    resp = HttpResponse(res)
    return resp




