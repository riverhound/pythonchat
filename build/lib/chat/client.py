
import sys, threading, socket, time, subprocess, sqlite3
from PyQt5 import Qt, QtGui, QtWidgets, QtCore

app = Qt.QApplication(sys.argv)

widget = QtWidgets.QWidget()
widget.resize(400, 300)
widget.setWindowTitle('Chat Application')

layout = QtWidgets.QGridLayout(widget)

text = QtWidgets.QTextBrowser()
lmessage = QtWidgets.QLabel("Message:")
message = QtWidgets.QLineEdit()
lname = QtWidgets.QLabel("Log in:")
name = QtWidgets.QLineEdit()
name.setText("User_1")
password = QtWidgets.QLineEdit()
password.setEchoMode(QtWidgets.QLineEdit.Password)
send = QtWidgets.QPushButton("Send")
send.setDefault(True)
conn = QtWidgets.QPushButton("Connect")
send.setDisabled(True)

layout.addWidget(text,0,0,6,6)
layout.addWidget(lname,6,0)
layout.addWidget(name,6,1,1,2)
layout.addWidget(password,6,3,1,1)
layout.addWidget(conn,6,5,1,1)
layout.addWidget(send,6,4,1,1)
layout.addWidget(lmessage,7,0,1,1)
layout.addWidget(message,7,1,1,5)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8001
host = 'localhost'

def sendfunc(sender):
	if len(message.text())<=0:
		return 
	buf = name.text() + ": "+message.text() 
	message.clear()
	#server_db.add_conn(name, time.asctime(), sender, buf)
	sock.send(buf.encode())
	return


def connfunc(sender):
	global sock
	if send.isEnabled() == False:
		name.setDisabled(True)
		password.setDisabled(True)
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((host,port))	
			send.setDisabled(False)
			subprocess.Popen(['python', 'add.py', '--login', name.text(), '--level', '1', '--password', password.text()])
			text.append("Connect success!")
			conn.setText("Exit")
		except:
			text.append("Connect fault! Please check your network")
	else:
		send.setDisabled(True)
		name.setDisabled(False)
		password.setDisabled(False)
		sock.send("Exit".encode())
		sock.close()
		text.append("goodbye!")	
		conn.setText("Connect")
		
def recv():
	while True:
		try:
			ss = sock.recv(1024).decode()
			print(ss)
			if len(ss)>1:
				text.append("(%s) \n %s" % (time.asctime(), ss))
		except:
			pass
	sys.exit()


send.mousePressEvent = sendfunc
conn.mousePressEvent = connfunc

widget.show()
threading._start_new_thread(recv, ())
app.exec_()
sys.exit(sock.close())
