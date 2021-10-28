#!/usr/bin/env python
# Author: Marcius Bezerra <marciusbezerra@outlook.com>
# Controle de temperatura do Raspberry

# criando o serviço linux:
# sudo nano /etc/systemd/system/temp-alert.service

# [Unit]
# Description=Temperature Alert Shutdown!! (Marcius)
#
# [Service]
# WorkingDirectory=/home/ubuntu/Projetos/temp-alert
# ExecStart=/usr/bin/python3 /home/ubuntu/Projetos/temp-alert/temp-alert.py
# Restart=always
#
# [Install]
# WantedBy=multi-user.target

# sudo systemctl enable temp-alert.service
# sudo systemctl start temp-alert.service
# systemctl status temp-alert.service
#
# ver log:
# tail -f temp-alert.log 

import os
from time import sleep
from datetime import datetime

maxTMP = 79  # maximum temperature!


def log(msg):
    print(msg)
    with open('temp-alert.log', 'a') as f:
        f.write("{}: {}\n".format(datetime.now(), msg))


def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp = (res.replace("temp=", "").replace("'C\n", ""))
    return temp


def temp_ok(temp):
    log("temperature OK: {}/{}".format(temp, maxTMP))


def temp_high(temp):
    log("TEMPERATURE HIGH! {}/{} SHUTDOWN NOW!".format(temp, maxTMP))
    os.system("shutdown now -h")


def getTEMP():
    CPU_temp = float(getCPUtemperature())
    if CPU_temp > maxTMP:
        temp_high(CPU_temp)
    else:
        temp_ok(CPU_temp)
    return()


while True:
    getTEMP()
    sleep(30)

# python temp-alert.py
