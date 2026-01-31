# polls/views.py
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

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

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})