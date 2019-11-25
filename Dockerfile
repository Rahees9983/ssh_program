FROM python:slim
RUN apt-get update
RUN apt install -y expect
RUN pip3 install flask
RUN pip3 install docker
RUN apt -y install openssh-server
WORKDIR  /for_ssh
COPY  . /for_ssh
# RUN chmod +x test2.sh 
RUN apt install sshpass
RUN ./test2.sh
EXPOSE  5004 22
CMD [ "python3","flask4_ssh.py" ]