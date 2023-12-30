import socket
import shutil

def send_file(s):

    received_message= s.recv(1024).decode('utf-8').strip('\r\n')

    path=input("server answer: {}".format(received_message))
    s.send(path.encode())
    print(s.recv(1024).decode('utf-8').strip('\r\n') + "\n")

def recv_file(s):
    received_message= s.recv(1024).decode('utf-8').strip('\r\n')

    name=input("server answer: {}".format(received_message) + "\n")
    s.send(name.encode())

    received_message= s.recv(1024).decode('utf-8').strip('\r\n')
    path= input("where would you like to keep your file? \n")
    path +='/'+name
    if(name in received_message):
        try:
            shutil.copyfile(received_message, path)
            print("download succesed \n")
        except EnvironmentError:
            print("something went wrong \n")
    else:
        print(received_message + "\n")

if __name__ == "__main__":
    ip= "127.0.0.1"
    port= 8080
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 8080)) 
    action= input("Hi, what would you like to do dounload-d or upload-u \n")
    s.send(action.encode())
    while(action!='0'): 
        if(action=='d'):
            recv_file(s)
        elif(action =='u'):
            send_file(s)
        action= input("Hi, what would you like to do dounload-d or upload-u \n")
        s.send(action.encode())
    s.close()