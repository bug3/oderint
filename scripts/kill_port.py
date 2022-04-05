from data.config import port
from psutil import process_iter, net_connections
from signal import SIGKILL


def getPid(p):
    for nc in net_connections():
        if nc.laddr[1] == p:
            return nc.pid


def kill():
    for p in process_iter():
        if p.pid == getPid(port):
            p.send_signal(SIGKILL)
