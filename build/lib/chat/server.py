import sys
import socket
import threading
import log_config

sockets = []


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


def deal(connection):
	while True:
		try:
			buf = connection.recv(1024).decode()
			print(buf)
			if buf == "Exit":
				log_config.disconn_info(connection.getpeername())
				sockets.remove(connection)
				StoppableThread.stop(connection)
				sys.exit()
			for i in sockets:
				i.send(buf.encode())
		except:
			break


if __name__ == '__main__':
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('localhost', 8001))
	sock.listen(5)
	print("Server started. To stop server press Ctrl+Break")
	while True:
		connection,address = sock.accept() 
		print("ip: %s:%d is connected!" % (address[0],address[1]))
		log_config.conn_info(address)
		threading._start_new_thread(deal, (connection,))
		sockets.append(connection)