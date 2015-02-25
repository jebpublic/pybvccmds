#!/usr/bin/python

import sys
import pybvc

from pybvc.controller.netconfnode import NetconfNode
from pybvc.common.status import STATUS
from pybvc.controller.controller import Controller
from pybvc.common.utils import load_dict_from_file


if __name__ == "__main__":

    f = "cfg.yml"
    d = {}
    if(load_dict_from_file(f, d) == False):
        print("Config file '%s' read error: " % f)
        exit()

    try:
        ctrlIpAddr = d['ctrlIpAddr']
        ctrlPortNum = d['ctrlPortNum']
        ctrlUname = d['ctrlUname']
        ctrlPswd = d['ctrlPswd']

        nodeName = d['nodeName']
        nodeIpAddr = d['nodeIpAddr']
        nodePortNum = d['nodePortNum']
        nodeUname = d['nodeUname']
        nodePswd = d['nodePswd']
    except:
        print ("Failed to get Controller device attributes")
        exit(0)

    ctrl = Controller(ctrlIpAddr, ctrlPortNum, ctrlUname, ctrlPswd)
    node = NetconfNode(ctrl, nodeName, nodeIpAddr, nodePortNum, nodeUname, nodePswd)

    print (">>> Removing '%s' from the Controller '%s'" % (nodeName, ctrlIpAddr))
    result = ctrl.delete_netconf_node(node)
    status = result[0]
    if(status.eq(STATUS.OK) == True):
        print ("'%s' was successfully removed from the Controller" % nodeName)
    else:
        print ("\n")
        print ("!!!Failed, reason: %s" % status.brief().lower())
        exit(0)

    print "\n"
