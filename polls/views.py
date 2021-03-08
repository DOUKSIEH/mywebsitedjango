#from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import loader
from .models import Question,Choice
from django.shortcuts import render,get_object_or_404
from django.http import Http404
import emoji 

datedujour = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')

# Create your views here.
def index(request):
    try:
        liste_dernieres_questions = Question.objects.order_by('-pub_date')[:3]
        resultats = ', '.join([q.question_text for q in liste_dernieres_questions])
        # template = loader.get_template('polls/index.html')
        context = {'liste_dernieres_questions': liste_dernieres_questions}
    except:
        raise Http404("La question n'existe pas {}".format(emoji.emojize(':winking_face_with_tongue:')))
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))
    # return HttpResponse("Bonjour tous le monde, La page d'accueil de l'appli des sondages ({})".format(datedujour))


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("La question n'existe pas {}".format(emoji.emojize(':winking_face_with_tongue:')))

    ## Comme ci-dessus, la methode get_object_or_404 lève une exception Http404 si l'objet n'existe pas
    question = get_object_or_404(Question, pk=question_id)
    #permet de retourner l'ensemble des questions
    # print(Question.objects.all().prefetch_related('choice_set'))
    # print(Choice.objects.order_by('question'))
    # print(Question.objects.values_list())
    return render(request, 'polls/detail.html', {'question': question,'id':question_id})
    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Vous avez voté à la question {}.".format(question_id))

