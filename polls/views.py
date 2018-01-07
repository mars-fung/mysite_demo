from django.shortcuts import render, get_object_or_404
from django.template import loader
# Create your views here.
from django.urls import reverse
from django.http import HttpResponse
from .models import Question, Choice
from django.http import Http404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:]
    template = loader.get_template('polls/index.html')
    context = {
    'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def indexRe(request):
    return HttpResponse("这个APP：polls的index页面")

def indexSort(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ',   '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    # #方法1：
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    #方法2
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 发生choice未找到异常时，重新返回表单页面，并给出提示信息
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 成功处理数据后，自动跳转到结果页面，防止用户连续多次提交。
      #  return HttpResponseRedirect(reverse('polls/results.html', args=(question.id,)))
        return render(request, 'polls/results.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})