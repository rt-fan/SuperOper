# -*- coding: utf-8 -*-
import re
import sys
from pysnmp.hlapi import *
from const import *

number = 0

answer_status = ''
answer_speed = ''
answer_uptime = ''
answer_inError = ''
answer_outError = ''
answer_description = ''
answer_error_message = ''

description_list = {}
ports_list = {}
status_list = {}
speed_list = {}
uptime_list = {}
inErr_list = {}
outErr_list = {}


def interface_list(host, oid):
    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData(community),
                              UdpTransportTarget((host, 161)),
                              ContextData(),
                              ObjectType(ObjectIdentity(oid)),
                              lexicographicMode=False):
        if errorIndication:
            print(errorIndication, file=sys.stderr)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'),
                  file=sys.stderr)
            break

        else:
            for varBind in varBinds:
                if oid == oid_ind:  # INDEX
                    continue

                elif oid == oid_system:
                    print(varBind)

                elif oid == oid_des:  # DESCRIPTION
                    descr = str(varBind[-1])
                    index = str(varBind[0][-1])
                    if re.search(r'thernet', descr) or re.search(r' Port', descr):
                        description_list[index] = descr
                        global number
                        number += 1
                        ports_list[index] = number

                elif oid == oid_stat:  # STATUS  1-up 2-down
                    index = str(varBind[0][-1])
                    if str(varBind[-1]) == '1':
                        status = 'up'
                    elif str(varBind[-1]) == '2':
                        status = 'down'
                    else:
                        status = str(varBind[-1])
                    status_list[index] = status

                elif oid == oid_speed:  # SPEED
                    index = str(varBind[0][-1])
                    if str(varBind[-1]) == '1000000000':
                        speed = '1000 Mb/s'
                    elif str(varBind[-1]) == '100000000':
                        speed = '100 Mb/s'
                    elif str(varBind[-1]) == '10000000':
                        speed = '10 Mb/s'
                    elif str(varBind[-1]) == '0':
                        speed = '0 Mb/s'
                    else:
                        speed = 'unkown speed'
                    speed_list[index] = speed

                elif oid == oid_inErr:  # INPUT ERROR
                    index = str(varBind[0][-1])
                    in_error = str(varBind[-1])
                    inErr_list[index] = in_error

                elif oid == oid_outErr:  # OUTPUT ERROR
                    index = str(varBind[0][-1])
                    out_error = str(varBind[-1])
                    outErr_list[index] = out_error

                else:
                    print('прочее')


def search_port(ip, port):
    interface_list(ip, oid_system)
    interface_list(ip, oid_des)
    interface_list(ip, oid_stat)
    interface_list(ip, oid_speed)
    interface_list(ip, oid_inErr)
    interface_list(ip, oid_outErr)

    for key_port in ports_list:
        if ports_list.get(key_port) == port:
            global answer_description
            answer_description = description_list.get(key_port)

            global answer_status
            answer_status = status_list.get(key_port)

            global answer_speed
            answer_speed = speed_list.get(key_port)

            global answer_inError
            answer_inError = inErr_list.get(key_port)

            global answer_outError
            answer_outError = outErr_list.get(key_port)

            return answer_description, answer_status, answer_speed, answer_inError, answer_outError
