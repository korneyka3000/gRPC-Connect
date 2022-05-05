from django_grpc_framework.services import Service
from .serializers import QuestionProtoSerializer


class QuizService(Service):
    def GetQuestion(self, request, context):
        serializer = QuestionProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer.message.body = f'Hey User, Your question was: {serializer.message.body.upper()}'
        return serializer.message
