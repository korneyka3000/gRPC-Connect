# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import jobs_pb2 as jobs__pb2


class JobServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetJobs = channel.unary_stream(
                '/jobs.JobService/GetJobs',
                request_serializer=jobs__pb2.JobRequest.SerializeToString,
                response_deserializer=jobs__pb2.JobResponse.FromString,
                )
        self.GetListJobs = channel.unary_stream(
                '/jobs.JobService/GetListJobs',
                request_serializer=jobs__pb2.Empty.SerializeToString,
                response_deserializer=jobs__pb2.JobResponse.FromString,
                )
        self.CreateJob = channel.unary_unary(
                '/jobs.JobService/CreateJob',
                request_serializer=jobs__pb2.AddJob.SerializeToString,
                response_deserializer=jobs__pb2.Empty.FromString,
                )


class JobServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetJobs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetListJobs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JobServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetJobs': grpc.unary_stream_rpc_method_handler(
                    servicer.GetJobs,
                    request_deserializer=jobs__pb2.JobRequest.FromString,
                    response_serializer=jobs__pb2.JobResponse.SerializeToString,
            ),
            'GetListJobs': grpc.unary_stream_rpc_method_handler(
                    servicer.GetListJobs,
                    request_deserializer=jobs__pb2.Empty.FromString,
                    response_serializer=jobs__pb2.JobResponse.SerializeToString,
            ),
            'CreateJob': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateJob,
                    request_deserializer=jobs__pb2.AddJob.FromString,
                    response_serializer=jobs__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jobs.JobService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JobService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetJobs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/jobs.JobService/GetJobs',
            jobs__pb2.JobRequest.SerializeToString,
            jobs__pb2.JobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetListJobs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/jobs.JobService/GetListJobs',
            jobs__pb2.Empty.SerializeToString,
            jobs__pb2.JobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jobs.JobService/CreateJob',
            jobs__pb2.AddJob.SerializeToString,
            jobs__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
