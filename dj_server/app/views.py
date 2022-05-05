import grpc
from django.shortcuts import render

import question_pb2
import question_pb2_grpc
from app.forms import QuestionForm


def q_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            print(request.POST)
            print(request.POST['body'])
            with grpc.insecure_channel('dj_c:50052') as channel:
                stub = question_pb2_grpc.QuizStub(channel)
                response = stub.GetQuestion(question_pb2.QuestionRequest(body=request.POST['body']))
                context = {
                    'response': response
                }
                return render(request, 'ask_question.html', context)
    form = QuestionForm()
    context = {
        'form': form
    }
    return render(request, 'ask_question.html', context)

