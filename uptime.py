from pysnmp.hlapi import *
from const import *
import sys
from datetime import *


oid_uptime = '1.3.6.1.2.1.1.3'
answer_sys_uptime = ''


def sys_uptime(host, oid):
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
                x = int(varBind[1])
                d = timedelta(milliseconds=x)  # 4th argument - milliseconds
                # time_format = "%Y-%m-%d %H:%M:%S"
                global answer_sys_uptime
                answer_sys_uptime = d
                return answer_sys_uptime

# формат времени исправить
