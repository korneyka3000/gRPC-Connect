import grpc
from django_grpc_framework.services import Service
from app.models import Jobs
from app.serializers import JobsProtoSerializer


class JobService(Service):
    def get_queryset(self, title):
        try:
            return Jobs.objects.filter(title=title)
        except Jobs.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'Jobs for:%s not found!' % title)

    def GetJobs(self, request, context):
        jobs = self.get_queryset(title=request.title)
        serializer = JobsProtoSerializer(jobs, many=True)
        for msg in serializer.message:
            yield msg

    def GetListJobs(self, request, context):
        jobs = Jobs.objects.all()
        serializer = JobsProtoSerializer(jobs, many=True)
        for msg in serializer.message:
            yield msg

    def CreateJob(self, request, context):
        print(type(request))
        print(request)
        serializer = JobsProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

