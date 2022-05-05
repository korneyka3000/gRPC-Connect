import question_pb2_grpc
from .services import QuizService


def grpc_handlers(server):
    question_pb2_grpc.add_QuizServicer_to_server(QuizService.as_servicer(),server)