from tkinter import *
from pysnmp.hlapi import *
from const import *
import os
from tkinter import messagebox
import sys
import description
import uptime
import interface


root = Tk()


def button_click():
    oid = '1.3.6.1.2.1.1.1'
    ip_input = ip_address_input.get()
    p_input = port_input.get()

    frame_2 = Frame(root, bg='#dddddd')
    frame_2.place(relx=0.01, rely=0.17, relwidth=0.98, relheight=0.78)

    # если узел пингуется, то проверяем вендор коммутатора
    response = os.system("ping -n 1 -w 50 " + ip_input)
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
                if p_input != '':
                    for varBind in varBinds:
                        text_vendor = str(varBind)

                        # DLINK DES
                        if re.search(r'DES', text_vendor):
                            text_frame2 = Label(frame_2, bg='#dddddd', text='>>> D-Link DES')
                            text_frame2.place(x=0, y=0)

                            description.sys_name(ip_input, description.oid_name)
                            uptime.sys_uptime(ip_input, uptime.oid_uptime)

                            ans_1 = 'Description:  ' + str(description.answer_sys_name)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_1)
                            text_frame2.place(x=0, y=20)

                            ans_2 = 'Время в сети:  ' + str(uptime.answer_sys_uptime)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_2)
                            text_frame2.place(x=0, y=40)

                            ans_3 = 'Порт:  ' + p_input + '   ( ' + str(interface.answer_description) + ' )   '
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_3)
                            text_frame2.place(x=0, y=60)

                            ans_4 = 'Состояние порта:  ' + str(interface.answer_status)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_4)
                            text_frame2.place(x=0, y=80)

                            ans_5 = 'Скорость на порту:  ' + str(interface.answer_speed)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_5)
                            text_frame2.place(x=0, y=100)

                            ans_6 = 'Ошибки на порту (Вх/Исх):  ' + str(interface.answer_inError) + '  /  ' + \
                                    str(interface.answer_outError)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_6)
                            text_frame2.place(x=0, y=120)
                            break

                        # DLINK DGS
                        elif re.search(r'DGS', text_vendor):
                            text_frame2 = Label(frame_2, bg='#dddddd', text='>>> D-Link DGS')
                            text_frame2.place(x=0, y=0)

                            description.sys_name(ip_input, description.oid_name)
                            uptime.sys_uptime(ip_input, uptime.oid_uptime)

                            ans_1 = 'Description:  ' + str(description.answer_sys_name)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_1)
                            text_frame2.place(x=0, y=20)

                            ans_2 = 'Время в сети:  ' + str(uptime.answer_sys_uptime)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_2)
                            text_frame2.place(x=0, y=40)

                            ans_3 = 'Порт:  ' + p_input + '   ( ' + str(interface.answer_description) + ' )   '
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_3)
                            text_frame2.place(x=0, y=60)

                            ans_4 = 'Состояние порта:  ' + str(interface.answer_status)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_4)
                            text_frame2.place(x=0, y=80)

                            ans_5 = 'Скорость на порту:  ' + str(interface.answer_speed)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_5)
                            text_frame2.place(x=0, y=100)

                            ans_6 = 'Ошибки на порту (Вх/Исх):  ' + str(interface.answer_inError) + '  /  ' + \
                                    str(interface.answer_outError)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_6)
                            text_frame2.place(x=0, y=120)
                            break

                        # CISCO
                        elif re.search(r'Cisco', text_vendor):
                            text_frame2 = Label(frame_2, bg='#dddddd', text='>>> Cisco')
                            text_frame2.place(x=0, y=0)

                            description.sys_name(ip_input, description.oid_name)
                            uptime.sys_uptime(ip_input, uptime.oid_uptime)
                            interface.search_port(ip_input, int(p_input))

                            ans_1 = 'Description:  ' + str(description.answer_sys_name)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_1)
                            text_frame2.place(x=0, y=20)

                            ans_2 = 'Время в сети:  ' + str(uptime.answer_sys_uptime)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_2)
                            text_frame2.place(x=0, y=40)

                            ans_3 = 'Порт:  ' + p_input + '   ( ' + str(interface.answer_description) + ' )   '
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_3)
                            text_frame2.place(x=0, y=60)

                            ans_4 = 'Состояние порта:  ' + str(interface.answer_status)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_4)
                            text_frame2.place(x=0, y=80)

                            ans_5 = 'Скорость на порту:  ' + str(interface.answer_speed)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_5)
                            text_frame2.place(x=0, y=100)

                            ans_6 = 'Ошибки на порту (Вх/Исх):  ' + str(interface.answer_inError) + '  /  ' + \
                                    str(interface.answer_outError)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_6)
                            text_frame2.place(x=0, y=120)
                            break

                        # SNR
                        elif re.search(r'SNR', text_vendor):
                            text_frame2 = Label(frame_2, bg='#dddddd', text='>>> SNR')
                            text_frame2.place(x=0, y=0)

                            description.sys_name(ip_input, description.oid_name)
                            uptime.sys_uptime(ip_input, uptime.oid_uptime)

                            ans_1 = 'Description:  ' + str(description.answer_sys_name)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_1)
                            text_frame2.place(x=0, y=20)

                            ans_2 = 'Время в сети:  ' + str(uptime.answer_sys_uptime)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_2)
                            text_frame2.place(x=0, y=40)

                            ans_3 = 'Порт:  ' + p_input + '   ( ' + str(interface.answer_description) + ' )   '
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_3)
                            text_frame2.place(x=0, y=60)

                            ans_4 = 'Состояние порта:  ' + str(interface.answer_status)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_4)
                            text_frame2.place(x=0, y=80)

                            ans_5 = 'Скорость на порту:  ' + str(interface.answer_speed)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_5)
                            text_frame2.place(x=0, y=100)

                            ans_6 = 'Ошибки на порту (Вх/Исх):  ' + str(interface.answer_inError) + '  /  ' + \
                                    str(interface.answer_outError)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_6)
                            text_frame2.place(x=0, y=120)
                            break

                        # ELTEX
                        elif re.search(r'MES', text_vendor):
                            text_frame2 = Label(frame_2, bg='#dddddd', text='>>> Eltex')
                            text_frame2.place(x=0, y=0)

                            description.sys_name(ip_input, description.oid_name)
                            uptime.sys_uptime(ip_input, uptime.oid_uptime)

                            ans_1 = 'Description:  ' + str(description.answer_sys_name)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_1)
                            text_frame2.place(x=0, y=20)

                            ans_2 = 'Время в сети:  ' + str(uptime.answer_sys_uptime)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_2)
                            text_frame2.place(x=0, y=40)

                            ans_3 = 'Порт:  ' + p_input + '   ( ' + str(interface.answer_description) + ' )   '
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_3)
                            text_frame2.place(x=0, y=60)

                            ans_4 = 'Состояние порта:  ' + str(interface.answer_status)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_4)
                            text_frame2.place(x=0, y=80)

                            ans_5 = 'Скорость на порту:  ' + str(interface.answer_speed)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_5)
                            text_frame2.place(x=0, y=100)

                            ans_6 = 'Ошибки на порту (Вх/Исх):  ' + str(interface.answer_inError) + '  /  ' + \
                                    str(interface.answer_outError)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_6)
                            text_frame2.place(x=0, y=120)
                            break

                        # HUAWEI
                        elif re.search(r'Huawei', text_vendor):
                            text_frame2 = Label(frame_2, bg='#dddddd', text='>>> Huawei')
                            text_frame2.place(x=0, y=0)

                            description.sys_name(ip_input, description.oid_name)
                            uptime.sys_uptime(ip_input, uptime.oid_uptime)

                            ans_1 = 'Description:  ' + str(description.answer_sys_name)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_1)
                            text_frame2.place(x=0, y=20)

                            ans_2 = 'Время в сети:  ' + str(uptime.answer_sys_uptime)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_2)
                            text_frame2.place(x=0, y=40)

                            ans_3 = 'Порт:  ' + p_input + '   ( ' + str(interface.answer_description) + ' )   '
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_3)
                            text_frame2.place(x=0, y=60)

                            ans_4 = 'Состояние порта:  ' + str(interface.answer_status)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_4)
                            text_frame2.place(x=0, y=80)

                            ans_5 = 'Скорость на порту:  ' + str(interface.answer_speed)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_5)
                            text_frame2.place(x=0, y=100)

                            ans_6 = 'Ошибки на порту (Вх/Исх):  ' + str(interface.answer_inError) + '  /  ' + \
                                    str(interface.answer_outError)
                            text_frame2 = Label(frame_2, bg='#dddddd', text=ans_6)
                            text_frame2.place(x=0, y=120)
                            break

                        # UNKNOWN VENDOR
                        else:
                            text_frame2 = Label(frame_2, bg='#dddddd', text='>>> unknown vendor')
                            text_frame2.grid(row='0', column='0')
                else:
                    messagebox.showinfo(title="Название", message='Поле "порт" пустое.')

    else:
        messagebox.showinfo(title="Название", message='ip адрес не пингуется, либо некорректно написан')


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

otstup3 = Label(frame, text='000', fg='#3d3d3d', bg='#3d3d3d')
otstup3.pack(side='left')

button_search = Button(frame, text='Поиск', bg='#256d7b', fg='white', command=button_click, height='1')
button_search.pack(side='left')

# Виджеты на втором фрейме
frame_3 = Frame(root, bg='#dddddd')
frame_3.place(relx=0.01, rely=0.17, relwidth=0.98, relheight=0.78)

# Главное окно
root['bg'] = '#fafafa'  # цвет заднего фона
root.title('SuperOper')  # название программыв шапке окна
root.wm_attributes('-alpha', 1)  # прозрачность окна
root.geometry('400x500+400+200')  # размер окна и расположение относительно верхнего левого края
root.resizable(width=False, height=False)  # запрет на изменение размера окна

root.mainloop()  # запуск постоянного цикла
