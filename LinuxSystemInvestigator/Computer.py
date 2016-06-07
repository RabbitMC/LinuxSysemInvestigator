import socket


class ComputerName:
    def __init__(self):
        self.name = socket.gethostname()