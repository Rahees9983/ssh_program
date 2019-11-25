import os 
import subprocess
import docker 

client = docker.DockerClient("tcp://10.90.31.33:2375")
mycon2 = client.containers.run("con1_img",name="python_sdk_con2",tty=True, stderr=True, stdout=True,detach=True)
# os.system("expect expect1.sh")