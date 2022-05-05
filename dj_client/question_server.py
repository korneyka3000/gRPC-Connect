from concurrent import futures

import grpc

from app.models import Question
from question_pb2 import QuestionResponse
from question_pb2_grpc import QuizServicer, add_QuizServicer_to_server


class QuizService(QuizServicer):
    def GetQuestion(self, request, context):
        print(request, '<<<request itself')
        metadata = dict(context.invocation_metadata())
        print(metadata, 'metadata')
        add_question = Question.objects.create(body=request)
        print(add_question, '<<add_question')
        return QuestionResponse(answer=f'Таки Ваш вопрос был: {request}')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    add_QuizServicer_to_server(QuizService(), serve)
    server.add_insecure_port('localhost:50052')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
