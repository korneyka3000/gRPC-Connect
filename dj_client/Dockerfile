FROM ubuntu:bionic
ENV PYTHONUNBUFFERED 1
WORKDIR /proj
COPY . .
RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
#RUN apt-get install python3-dev  # can be deleted
#RUN apt-get install gcc g++  # can be deleted
RUN pip3 install -r requirements.txt
RUN ["chmod", "+x", "runner.sh"]
#ENTRYPOINT ["runner.sh"]
#CMD ["python3", "manage.py", "grpcrunserver", "--dev", "[::]:50052"]