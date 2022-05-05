import grpc
import jobs_pb2
import jobs_pb2_grpc
from jobs_pb2 import JobRequest, JobResponse, AddJob
from django.shortcuts import render
from google.protobuf.json_format import MessageToDict
from app.forms import MyForm, AddForm


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            with grpc.insecure_channel('dj_s:50051') as channel:
                stub = jobs_pb2_grpc.JobServiceStub(channel)
                arr = []
                for job in stub.GetJobs(JobRequest(title=request.POST['title'])):
                    dict_job = MessageToDict(job)
                    arr.append(dict_job)
            form = MyForm()
            context = {
                'form': form,
                'arr': arr,
            }
            return render(request, 'base.html', context)
    form = MyForm()
    with grpc.insecure_channel('dj_s:50051') as channel:
        stub = jobs_pb2_grpc.JobServiceStub(channel)
        arr = []
        for job in stub.GetListJobs(JobResponse()):
            dict_job = MessageToDict(job)
            arr.append(dict_job)
    context = {
        'arr': arr,
        'form': form,
    }
    return render(request, 'base.html', context)


def add_view(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
        with grpc.insecure_channel('dj_s:50051') as channel:
            stub = jobs_pb2_grpc.JobServiceStub(channel)
            response = stub.CreateJob(jobs_pb2.AddJob(title=form.cleaned_data['title'],
                                                      level=form.cleaned_data['level'],
                                                      salary=form.cleaned_data['salary'],
                                                      location=form.cleaned_data['location']))
            if response:
                print(response)
    form = AddForm()
    context = {
        'form': form,
    }
    return render(request, 'add.html', context)
