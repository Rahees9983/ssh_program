import flask
import os

app = flask.Flask(__name__)

@app.route('/get',methods =['GET'])
def fetech_data():
    return "Hello Sultan Mirza This container 2 flask !!!!!!!!!!!!1"

@app.route('/get/make_ssh',methods =['GET'])
def make_ssh_con():
    os.system("mkdir flask_dir")
    # os.system("sshpass -p gslab@123 ssh gslab@192.168.1.106")
    os.system("expect expect1.sh")
    return "ssh with expect script "

@app.route('/get/ssh_with_pass',methods =['GET'])
def sh_con_pass():
    os.system("mkdir pass_dir")
    # os.system("sshpass -p gslab@123 ssh gslab@10.90.31.33")
    os.system("sshpass -p gslab@123 ssh gslab@192.168.1.106")
    return "ssh using sshpass command "

@app.route('/get/ssh_command',methods =['GET'])
def with_ddh_command():
    os.system("mkdir flask_dir")
    # os.system("sshpass -p gslab@123 ssh gslab@192.168.1.106")
    os.system("ssh gslab@192.168.1.106")
    return "Doing ssh with ssh user_name@ipaddress "


if __name__ == "__main__":
    app.run(debug=True,port=5004,host='0.0.0.0')