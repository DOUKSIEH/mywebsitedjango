#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.template import loader
from .models import Question,Choice
from django.shortcuts import render,get_object_or_404
from django.http import Http404
import emoji 
from django.urls import reverse
from django.views import generic

datedujour = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')

# Create your views here.
class IndexListView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'
    def get_queryset(self):
        """Returne les dernières questions ."""
        return Question.objects.order_by('-pub_date')[:6]

    # try:
    #     liste_dernieres_questions = Question.objects.order_by('-pub_date')[:3]
    #     resultats = ', '.join([q.question_text for q in liste_dernieres_questions])
    #     # template = loader.get_template('polls/index.html')
    #     context = {'liste_dernieres_questions': liste_dernieres_questions}
    # except:
    #     raise Http404("La question n'existe pas {}".format(emoji.emojize(':winking_face_with_tongue:')))
    # return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))
    # return HttpResponse("Bonjour tous le monde, La page d'accueil de l'appli des sondages ({})".format(datedujour))


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("La question n'existe pas {}".format(emoji.emojize(':winking_face_with_tongue:')))

#     ## Comme ci-dessus, la methode get_object_or_404 lève une exception Http404 si l'objet n'existe pas
#     question = get_object_or_404(Question, pk=question_id)
#     #permet de retourner l'ensemble des questions
#     # print(Question.objects.all().prefetch_related('choice_set'))
#     # print(Choice.objects.order_by('question'))
#     # print(Question.objects.values_list())
#     return render(request, 'polls/detail.html', {'question': question,'id':question_id})
#     # return HttpResponse("You're looking at question %s." % question_id)


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Veuillez selectionné(e) l'une des réponses.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
