#!/usr/bin/python

import sys
import json
import pybvc

from pybvc.netconfdev.vrouter.vrouter5600 import VRouter5600
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
    vrouter = VRouter5600(ctrl, nodeName, nodeIpAddr, nodePortNum, nodeUname, nodePswd) 
    print ("<<< 'Controller': %s, '%s': %s" % (ctrlIpAddr, nodeName, nodeIpAddr))
    
    result = vrouter.get_loopback_interfaces_cfg()
    status = result[0]
    if(status.eq(STATUS.OK) == True):
        print "Loopback interfaces config:"
        dpIfCfg = result[1]
        print json.dumps(dpIfCfg, indent=4)
    else:
        print ("\n")
        print ("!!!Failed, reason: %s" % status.brief().lower())
        print ("%s" % status.detail())
        sys.exit(0)
