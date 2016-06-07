import socket


class Computer:
    def __init__(self):
        self.name = socket.gethostname()