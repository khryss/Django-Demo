import operator
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import *


def index(request):
    tests = Test.objects.all()
    return render(request, 'tests/index.html', {'tests': tests})


def _get_questions_for_test_(test_obj):

    questions = test_obj.question_set.all()
    return questions


def _get_results_for_test(test_obj):

    results = test_obj.result_set.all()
    return results


def get_test_by_id(request, test_id):
    test = Test.objects.get(id=test_id)
    questions = _get_questions_for_test_(test)
    results = _get_results_for_test(test)
    return render(request, 'tests/test_detail.html', {'test': test, 'questions': questions, 'results': results})


def _compute_result(test, score):
    # I don't really understand what should happen here.
    # It looks like you are assuming there are always at least some results.
    # But in the beginning, there will be no results for any test, so you get 500 for IndexError.
    results = sorted(test.result_set.all(), key=operator.attrgetter('max_score'))
    for i in range(0, len(results) - 2):
        if results[i].max_score < score < results[i + 1].max_score:
            return results[i+1]
    return results[len(results) - 1]


@csrf_exempt
def submit_test(request, test_id):
    answer_ids_str = request.POST.getlist('answer_ids')
    if not answer_ids_str:
        return HttpResponse("Please answer all questions before submitting")

    # Fortunately this is not needed. Django figures out that the field is integer and converts it with int().
    answer_ids = [int(answer_id) for answer_id in answer_ids_str]

    # You can use the django way .filter(id__in=<your_id_list>).
    # Also, to get a queryset with ids only, you can use qs.values_list('id', flat=True).
    # Django querysets act like lists, so you will safely be able to use the sum() over it.
    scores = [Answer.objects.get(id=a_id).score for a_id in answer_ids]
    score = sum(scores)
    test = Test.objects.get(id=test_id)
    result = _compute_result(test, score)

    return render(request, 'tests/test_result.html', {'test': test, 'result': result, 'score': score})
