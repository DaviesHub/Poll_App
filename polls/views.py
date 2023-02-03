from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

# Create your views here.
def poll_index(request):
    if request.user.is_authenticated:
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list,
        "firstname": request.user.first_name,
        }
        return render(request, "polls/poll.html", context)
    else:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
        
def detail(request, question_id):
    if request.user.is_authenticated:
        question = get_object_or_404(Question, pk=question_id) 
        return render(request, 'polls/detail.html', {'question': question})
    else:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )

def results(request, question_id):
    if request.user.is_authenticated:
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})
    else:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )

def vote(request, question_id):
    if request.user.is_authenticated:
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(
                pk=request.POST['choice']
            )
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice."
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(
                reverse('polls:results', args=(question_id,))
            )
    else:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )

