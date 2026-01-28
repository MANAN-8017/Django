# polls/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))

def home(request):
    return render(request, 'hello.html')

def calc(request):
    result = None

    if request.method == "POST":
        x = int(request.POST.get('x'))
        y = int(request.POST.get('y'))
        op = request.POST.get('op')
        
        if x and y:
            if op == '+' or op == 'sum':
                result = x + y
            elif op == '-' or op == 'sub':
                result = x - y
            elif op == '*' or op == 'mul':
                result = x * y
            elif op == '/' or op == 'div':
                result = x / y
            elif op == '**' or op == '^' or op == 'exp' or op == 'power':
                  result = pow(x, y)
            elif op == '%' or op == 'mod':
                result = x % y
            elif op == '//':
                result = x // y
            else:
                result = "Invalid Operator"

    return render(request, 'calc.html', {'result': result})

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

