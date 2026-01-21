# polls/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'hello.html')

def calc(request):
    result = None

    if request.method == "POST":
        x = request.POST.get('x')
        y = request.POST.get('y')
        op = request.POST.get('op')

        if op == '+':
            if x and y:
                result = int(x) + int(y)   # Example operation
        elif op == '-':
            if x and y:
                result = int(x) - int(y)
        elif op == '*':
            if x and y:
                result = int(x) * int(y)
        elif op == '/':
            if x and y:
                result = int(x) / int(y)
        else:
            result = "Invalid Operator"

    return render(request, 'calc.html', {'result': result})