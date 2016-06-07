# import sys
# import os
# import time
import json

from Computer import Computer

class LXSysInv:
    """Linux System Inventigator main class"""
    def __init__(self):
        """ init method """

        print "\n----------------------------------"
        print "LXInv - Linux System Inventigator"
        print "---------------------------------- \n\n"

        self.data = []

        computer = Computer()
        self.computer_name = computer.name

        print ":: ComputerName: ", self.computer_name




        print "\n\nEND \n\n"

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)





#unumber = os.getuid()
#pnumber = os.getpid()
#where = os.getcwd()
#what = os.uname()
#used = os.times()
#now = time.time()
#means = time.ctime(now)



#print "User number: ", unumber
#print "Process ID: ", pnumber
#print "Current Directory: ", where
#print "System information: ", what
#print "System information: ", used

#print "\nTime is now: ", now
#print "Which interprets as:", means


