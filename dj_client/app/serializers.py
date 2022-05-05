from django_grpc_framework import proto_serializers
import question_pb2
from .models import Question


class QuestionProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Question
        proto_class = question_pb2.QuestionRequest
        fields = ['body']
