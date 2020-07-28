from tkinter import *
from pysnmp.hlapi import *
from const import *
import os
from tkinter import messagebox
import telnetlib
import time

root = Tk()


def button_click():
    oid = '1.3.6.1.2.1.1.1'
    ip_input = ip_address_input.get()
    p_input = port_input.get()

    # если узел пингуется, то проверяем вендор коммутатора

    response = os.system("ping -n 1 -w 20 " + ip_input)
    if response == 0:

        # узнаем вендор коммутатора

        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in nextCmd(SnmpEngine(),
                                  CommunityData(community),
                                  UdpTransportTarget((ip_input, 161)),
                                  ContextData(),
                                  ObjectType(ObjectIdentity(oid)),
                                  lexicographicMode=False):
            if errorIndication:

                # пинг проходит, по SNMP подключения нет

                print(errorIndication, file=sys.stderr)

                text_frame2 = Label(frame_2, bg='#dddddd', text='>>> Ping Yes')
                text_frame2.place(x=0, y=0)
                text_frame2 = Label(frame_2, bg='#dddddd', text='>>> no SNMP connect')
                text_frame2.place(x=0, y=20)
                break

            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'),
                      file=sys.stderr)
                break

            else:
                for varBind in varBinds:
                    text_vendor = str(varBind)
                    if re.search(r'DES', text_vendor):

                        telnet = telnetlib.Telnet(ip_input)
                        time.sleep(0.1)
                        telnet.write(telnet_login_default.encode('ascii') + b'\n')
                        time.sleep(1)
                        telnet.write(telnet_password_default.encode('ascii') + b'\n')
                        telnet.write(b'\n')
                        time.sleep(1)
                        telnet.write(b'disable clipaging')
                        time.sleep(1)
                        telnet.write(b'\n')
                        time.sleep(1)
                        command = command_telnet_link_dlink + str(p_input)
                        telnet.write(command.encode('ascii') + b'\n')
                        time.sleep(5)
                        telnet.read_until(b'show ports', timeout=5)
                        answer = telnet.read_very_eager()
                        time.sleep(1)

                        text = Text(frame_2, height=25, width=87, font='Arial 9', wrap=WORD)
                        text.insert(1.0, 'D-Link DES')
                        text.insert(3.0, answer)
                        text.place(x=0, y=0)
                        scrollbar = Scrollbar(frame_2)
                        scrollbar.pack(side=RIGHT, fill=Y)
                        # первая привязка
                        scrollbar['command'] = text.yview
                        # вторая привязка
                        text['yscrollcommand'] = scrollbar.set

                        telnet.close()

                    elif re.search(r'DGS', text_vendor):

                        # авторизация через telnet на коммутаторе

                        telnet = telnetlib.Telnet(ip_input)
                        time.sleep(0.1)
                        telnet.write(telnet_login_default.encode('ascii') + b'\n')
                        time.sleep(1)
                        telnet.write(telnet_password_default.encode('ascii') + b'\n')
                        time.sleep(1)
                        telnet.write(b'\n')
                        time.sleep(1)
                        telnet.write(b'disable clipaging')
                        time.sleep(1)
                        telnet.write(b'\n')
                        time.sleep(1)
                        command = command_telnet_link_dlink + str(p_input)
                        telnet.write(command.encode('ascii') + b'\n')
                        time.sleep(5)
                        telnet.read_until(b'show ports', timeout=5)
                        answer = telnet.read_very_eager()
                        time.sleep(1)

                        text = Text(frame_2, height=25, width=87, font='Arial 9', wrap=WORD)
                        text.insert(1.0, 'D-Link DGS')
                        text.insert(3.0, answer)
                        text.place(x=0, y=0)
                        scrollbar = Scrollbar(frame_2)
                        scrollbar.pack(side=RIGHT, fill=Y)
                        # первая привязка
                        scrollbar['command'] = text.yview
                        # вторая привязка
                        text['yscrollcommand'] = scrollbar.set

                        telnet.close()

                    elif re.search(r'Cisco', text_vendor):
                        # авторизация через telnet на коммутаторе

                        telnet = telnetlib.Telnet(ip_input)
                        time.sleep(0.1)
                        telnet.write(telnet_login_default.encode('ascii') + b'\n')
                        time.sleep(1)
                        telnet.write(telnet_password_default.encode('ascii') + b'\n')
                        telnet.write(b'\n')
                        time.sleep(1)
                        telnet.write(b'terminal lenght 0')
                        time.sleep(1)
                        telnet.write(b'\n')
                        time.sleep(1)
                        command = command_telnet_link_cisco
                        telnet.write(command.encode('ascii') + b'\n')
                        time.sleep(5)
                        telnet.read_until(b'sh ip int brief', timeout=5)
                        answer = telnet.read_very_eager()
                        time.sleep(1)

                        text = Text(frame_2, height=25, width=87, font='Arial 9', wrap=WORD)
                        text.insert(1.0, 'Cisco')
                        text.insert(3.0, answer)
                        text.place(x=0, y=0)
                        scrollbar = Scrollbar(frame_2)
                        scrollbar.pack(side=RIGHT, fill=Y)
                        # первая привязка
                        scrollbar['command'] = text.yview
                        # вторая привязка
                        text['yscrollcommand'] = scrollbar.set

                        telnet.close()

                    elif re.search(r'SNR', text_vendor):
                        text_frame2 = Label(frame_2, bg='#dddddd', text='>>> SNR')
                        text_frame2.grid(row='0', column='0')

                    elif re.search(r'MES', text_vendor):
                        text_frame2 = Label(frame_2, bg='#dddddd', text='>>> Eltex')
                        text_frame2.place(x=0, y=0)

                    elif re.search(r'Huawei', text_vendor):
                        # авторизация через telnet на коммутаторе

                        telnet = telnetlib.Telnet(ip_input)
                        time.sleep(0.1)
                        telnet.write(telnet_login_default.encode('ascii') + b'\n')
                        time.sleep(1)
                        telnet.write(telnet_password_default.encode('ascii') + b'\n')
                        telnet.write(b'\n')
                        time.sleep(1)
                        telnet.write(b'screen-lenght 0 temporary')
                        time.sleep(1)
                        telnet.write(b'\n')
                        time.sleep(1)
                        command = command_telnet_link_cisco
                        telnet.write(command.encode('ascii') + b'\n')
                        time.sleep(5)
                        telnet.read_until(b'dis int brief', timeout=5)
                        answer = telnet.read_very_eager()
                        time.sleep(1)

                        text = Text(frame_2, height=25, width=87, font='Arial 9', wrap=WORD)
                        text.insert(1.0, 'Huawei')
                        text.insert(3.0, answer)
                        text.place(x=0, y=0)
                        scrollbar = Scrollbar(frame_2)
                        scrollbar.pack(side=RIGHT, fill=Y)
                        # первая привязка
                        scrollbar['command'] = text.yview
                        # вторая привязка
                        text['yscrollcommand'] = scrollbar.set

                        telnet.close()

                    else:
                        text_frame2 = Label(frame_2, bg='#dddddd', text='>>> unknown vendor')
                        text_frame2.grid(row='0', column='0')

    else:
        messagebox.showinfo(title="Название", message='ip адрес не пингуется, либо некорректно написан')

    # print(info_str)
    # text_frame2 = Label(frame2, bg='#dddddd', text_vendor=info_str)
    # text_frame2.grid(row='0', column='0')


# Виджеты на главном окне
# Виджеты на первом фрейме

frame = Frame(root, bg='#3d3d3d')
frame.place(relx=0.01, rely=0.03, relwidth=0.98, relheight=0.13)

otstup1 = Label(frame, text='000', fg='#3d3d3d', bg='#3d3d3d')
otstup1.pack(side='left')

ip_address_input = Entry(frame, bg='white')
ip_address_input.pack(side='left', fill='x')

title2 = Label(frame, text='Введите ip', bg='#3d3d3d', fg='white')
title2.pack(side='left')

otstup2 = Label(frame, text='000', fg='#3d3d3d', bg='#3d3d3d')
otstup2.pack(side='left')

port_input = Entry(frame, bg='white', width='4')
port_input.pack(side='left')

title4 = Label(frame, text='Порт', fg='white', bg='#3d3d3d')
title4.pack(side='left')

otstup3 = Label(frame, text='00000000', fg='#3d3d3d', bg='#3d3d3d')
otstup3.pack(side='left')

button_search = Button(frame, text='Поиск', bg='#256d7b', fg='white', command=button_click, height='1')
button_search.pack(side='left')

# Виджеты на втором фрейме

frame_2 = Frame(root, bg='#dddddd')
frame_2.place(relx=0.01, rely=0.17, relwidth=0.98, relheight=0.78)

# Главное окно

root['bg'] = '#fafafa'  # цвет заднего фона
root.title('SuperOper')  # название программыв шапке окна
root.wm_attributes('-alpha', 1)  # прозрачность окна
root.geometry('650x500+400+200')  # размер окна и расположение относительно верхнего левого края
root.resizable(width=False, height=False)  # запрет на изменение размера окна

root.mainloop()  # запуск постоянного цикла
