# polls/views.py

from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from django.template import loader
from .models import Question

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

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)