from django_grpc_framework import proto_serializers

import jobs_pb2
from app.models import Jobs


class JobsProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Jobs
        proto_class = jobs_pb2.JobResponse
        fields = [
            'id',
            'title',
            'level',
            'salary',
            'location',
        ]
