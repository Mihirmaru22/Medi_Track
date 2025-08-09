# base image 

FROM python:3.11-slim

# workingdir

WORKDIR /main

# copy 
COPY requirements.txt /main/

#run 
RUN apt-get update && apt-get upgrade -y && apt-get clean
RUN pip install -r requirements.txt

#copy
COPY . /main

#port 

EXPOSE 8000

#command

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]