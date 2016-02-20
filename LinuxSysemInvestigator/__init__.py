import argparse
from os import path
import LXSysInv


parser = argparse.ArgumentParser(description='LinuxSystemInvestigator')
parser.add_argument('-o', dest="output path dir, where to store the resulting json file.")
args = parser.parse_args()

if path.exists(args.o):
    linuxSysInv = LXSysInv()
