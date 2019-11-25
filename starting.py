import os 
import subprocess
import docker 
import time 
def up_container():

    # os.system("cd" "Java" "Dockerfile ")

    # os.system("docker build -t con2_java_image ./Java")
    
    client = docker.from_env()
    # aead627e34fb  con1_img  "python flask4_con1.…"   2 hours ago Up 2 hours   22/tcp, 5002/tcp         docker_con
    my_container = client.containers.run("host_ssh_img",ports={"5004/tcp":5004},name="host_ssh_con",tty=True, stderr=True, stdout=True,detach=True)
    # print("Container created successfully ")
    # print("program is going to sleep for 30 seconds .......")
    # time.sleep(20)
    # print("program is resumed after the sleep of 30 seconds ........")

    # exit_code, strrr = my_container.exec_run(['sh', '-c', 'service ssh start & expect expect1.sh'],stdout=True, stderr=True, stdin=True, tty=True,stream=True, demux=False)
    # my_container.exec_run(["python","do_ssh_of_host.py"],stdout=True, stderr=True, stdin=True, tty=True,stream=True, demux=False)
    my_container.exec_run(['sh', '-c', 'mkdir again_using_sdk'])
    # my_container.exec_run(['sh', '-c', 'service ssh start & mkdir secont_time'])
    my_container.exec_run(['python','run_expect.py'],stdout=True, stderr=True, stdin=True, tty=True,stream=True, demux=False)
    my_container.exec_run(['sh', '-c', 'sshpass -p gslab@123 ssh gslab@10.90.31.33'])
    client.containers.list()
    
    # print(exit_code)
    # for a in strrr:
    #     print(a)
    # print("Wating for the expect file to make connection")
    time.sleep(22)
    # print("hope ssh of host will be done ")

    # os.system("docker run -it --name main_con container1_image")

    # os.system("docker run -it --name java_con1 con2_java_image")
    # a = subprocess.check_output("docker inspect -f '{{json .NetworkSettings.Networks.bridge.IPAddress}}' java_con1", shell=True)
    # ip = a.decode("utf-8")
    # os.system("expect expect1.sh "+ip)
    # os.system("expect expect.sh ")

up_container()