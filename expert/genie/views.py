from django.shortcuts import render
from django.http import HttpResponse
from .models import Actor
from .libs.expert import Expert
from .libs.enums import Gender
from .libs.constants import Constants

# Create your views here.

expert = Expert(Actor.objects.all())


def rub(request):
    question = expert.query()
    if question == Constants.expert_end:
        return render(request, 'result.html', {'answer': expert.get_answer()})
    if question == Constants.expert_unknown:
        return render(request, 'empty.html')
    if question == Constants.expert_empty:
        return render(request, 'empty.html')
    return render(request, 'poll.html', {'question': question})


def answer(request, answer):
    response = expert.update(answer)
    return rub(request)


def index(request):
    return render(request, 'index.html')


def restart(request):
    expert.restart(Actor.objects.all())
    return rub(request)


def test(request):
    filter = "gender"
    value = Gender.Female
    actors = Actor.objects.all()
    return HttpResponse(actors.filter(gender=value).count())


def input(request, firstname, lastname):
    data = expert.get_dataset()
    Actor.objects.create()
    return index(request)