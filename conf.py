# данные для подключения и тд
ip_adress = ''
community = ''

telnet_login_default = ''
telnet_password_default = ''

# прочие данные
const1 = ''
const2 = ''
const3 = ''
const4 = ''

# команды для telnet
command_telnet_link_cisco = 'sh ip int brief '  # Interface Status
command_telnet_link_huawei = 'dis int brief '  # Interface PHY Protocol
command_telnet_link_dlink = 'sh ports '  # State/MDI Connection Speed/Duplex/FlowCtrl
command_telnet_link_snr = 'sh int ethernet status '  # Interface Link/Protokol Speed Vlan
command_telnet_link_eltex = 'sh int status '  # Port Type Speed LinkState

command_telnet_error_cisco = ''
command_telnet_error_huawei = ''
command_telnet_error_dlink = ''
command_telnet_error_snr = ''
command_telnet_error_eltex = ''

command_telnet_mac_cisco = ''
command_telnet_mac_huawei = ''
command_telnet_mac_dlink = ''
command_telnet_mac_snr = ''
command_telnet_mac_eltex = ''


# disable clipaging (d-link)
# terminal lenght 0 (cisco)
# screen-lenght 0 temporary (huawei)

# OID :
system_description = '1.3.6.1.2.1.1.1.0'
system_name = '1.3.6.1.2.1.1.5.0'
system_uptime = '1.3.6.1.2.1.1.3.0'
system_ip = '1.3.6.1.2.1.4.20.1.1'  # 1.3.6.1.2.1.4.22.1.3 [] - arp ip
system_mac = '1.3.6.1.2.1.17.1.1.0'  # 1.3.6.1.4.1.171.12.15.2.1.0
system_arp_table = '1.3.6.1.2.1.4.22.1.2'
interface_description = ''' 1.3.6.1.2.1.2.2.1.1 [] - index
                            1.3.6.1.2.1.2.2.1.2 [] - descr
                            1.3.6.1.2.1.2.2.1.5 [] -speed
                            1.3.6.1.2.1.2.2.1.14 [] -inErr
                            1.3.6.1.2.1.2.2.1.20 [] - outErr
                            1.3.6.1.2.1.2.2.1.9 [] - uptime '''
interface_status = '1.3.6.1.2.1.2.2.1.8'  # [](up, down)
interface_mac = '1.3.6.1.2.1.17.7.1.2.2.1.2'
vlan = '1.3.6.1.2.1.17.7.1.4.3.1.1'
system_model = '1.3.6.1.4.1.171.12.11.1.9.4.1.9.1'


oid_system = '1.3.6.1.2.1.1.1'
oid_ind = '1.3.6.1.2.1.2.2.1.1'
oid_des = '1.3.6.1.2.1.2.2.1.2'
oid_stat = '1.3.6.1.2.1.2.2.1.8'
oid_speed = '1.3.6.1.2.1.2.2.1.5'
oid_upt = '1.3.6.1.2.1.2.2.1.9'
oid_inErr = '1.3.6.1.2.1.2.2.1.14'
oid_outErr = '1.3.6.1.2.1.2.2.1.20'
