import socket
import shutil
import os

def recv_file(p, c, s): 
    c.send("which file".encode())

    received_message= c.recv(1024).decode('utf-8').strip('\r\n')
    list_name= received_message.split("/")
    file_name=  list_name[-1]
    path_server= p+file_name
    file_path = received_message
    try:
        shutil.copyfile(file_path, path_server)
        c.send("upload succesed :)")
    except:
        c.send("upload failed :(")

def send_file(p, c, s):
    c.send("which file".encode())

    received_message= c.recv(1024).decode('utf-8').strip('\r\n')
    path_file=p+received_message
    file_list= os.listdir(p)
    if received_message in file_list:
        c.send(path_file.encode())
    else:
        c.send("sorry, the file not exist".encode())

if __name__ == "__main__":
    ip= "127.0.0.1"
    port= 8080
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((ip,port))
        print("server is listening \nwaiting for connection...")
    except:
        print("binding Error")
    s.listen(1)
    c, addr= s.accept()  
    p= "/Users/agamboni/Desktop/clientFiles/"

    action= c.recv(1024).decode('utf-8').strip('\r\n')
    while(action!='0'):
        if(action=='u'):
            recv_file(p, c, s)
        elif(action=='d'):
            send_file(p, c, s)
        action= c.recv(1024).decode('utf-8').strip('\r\n')

    c.close()
    s.close()        