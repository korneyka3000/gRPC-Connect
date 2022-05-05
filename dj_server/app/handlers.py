from app.services import JobService
import jobs_pb2_grpc


def grpc_handlers(server):
    jobs_pb2_grpc.add_JobServiceServicer_to_server(JobService.as_servicer(), server)
