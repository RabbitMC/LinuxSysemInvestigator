import sys
import os
import time
import json

class LXSysInv:
    """Linux System Inventigator main class"""
    def __init__(self):
        """ init method """
        self.data = []

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)





unumber = os.getuid()
pnumber = os.getpid()
where = os.getcwd()
what = os.uname()
used = os.times()
now = time.time()
means = time.ctime(now)

print "User number",unumber
print "Process ID",pnumber
print "Current Directory",where
print "System information",what
print "System information",used

print "\nTime is now",now
print "Which interprets as",means