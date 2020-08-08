from pysnmp.hlapi import *
from const import *
import sys

oid_name = '1.3.6.1.2.1.1.5'
answer_sys_name = ''


def sys_name(host, oid):
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
                global answer_sys_name
                answer_sys_name = varBind[1]
                return answer_sys_name
