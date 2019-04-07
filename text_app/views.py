# from django.shortcuts import render,get_object_or_404
# from django.http import HttpResponse,HttpResponseRedirect
# from .models import Question,Choice
# from django.urls import reverse
# # Create your views here.
#
#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'text/index.html', context)
#
# def detail(request, question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     #get_obj___404(一个model,manage,或query对象  , pk 查询条件)
#     return render(request,'text/detail.html',{'question':question})
#
#
# def results(request, question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request,'text/results.html',{'question':question})
#
# def vote(request, question_id):
#
#     question=get_object_or_404(Question,pk=question_id)
#     try:
#         # request.POST是一个类字典对象，让你可以通过关键字的名字获取提交的数据
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         #如果没有符合的字典对象 ,返回其他网页并报错 ,传入此网页需要的对应关键字
#         return render(request, 'text/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         #数据的操作
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         #redirect只接收一个参数,重定向网页,reverse避免硬解码:(重定向页面,向页面传入的参数)
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

def text_index(request):
    '''测试主页'''
    return render(request,"text/text_index.html")

class IndexView(generic.ListView):
    template_name = 'text/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'text/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'text/results.html'


def vote(request, question_id):

    question=get_object_or_404(Question,pk=question_id)
    try:
        # request.POST是一个类字典对象，让你可以通过关键字的名字获取提交的数据
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        #如果没有符合的字典对象 ,返回其他网页并报错 ,传入此网页需要的对应关键字
        return render(request, 'text/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        #数据的操作
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #redirect只接收一个参数,重定向网页,reverse避免硬解码:(重定向页面,向页面传入的参数)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
