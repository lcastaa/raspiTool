import os
import time
import subprocess as sub
from sys import platform
from os.path import exists
from pathlib import Path


def main():
    print('')
    print('Choose to execute')
    print('')
    print('[1] - Installer')
    print('[2] - Hostname Editor')
    print('[3] - OverClocker')
    print('[4] - FireWall Configurator')
    print('[5] - Auto Run..')
    print('')
    choice = int(input('Choice ->: '))
    if(choice == 1):
        installer()
    elif(choice == 2):
        hostname()
        reboot()
    elif(choice == 3):
        overclocker()
        reboot()
    elif(choice == 4):
        firewall()
    elif(choice == 5):
        hostname()
        overclocker()
        installer()
        reboot()

def firewall():
    os.chdir('/bin')
    path_to_file = 'ufw'
<<<<<<< HEAD
    path = Path(path_to_file)
=======
>>>>>>> 1f24783b9904277a4327b9562e0c8ce6813f6e69
    if path.is_file():
        firewallrules = []
        limit = int(input('How many rules you have?: '))
        while i != limit:
            count = 1
            rule = int(input('Enter Rule #'+count+': '))
            firewallrules.append(rule)
            count += 1
            i += 1
        o = 0
        while o != limit:
            for x in firewallrules:
                os.system('sudo ufw allow '+ x)
    else:
        print('')
        print('UFW Doesnt Exist on system.....')
        print('')
        print('Installing Now....')
        os.system('sudo apt install ufw -y')
        firewall()





def installer():
    print('')
    print('Enter App to install:')
    print('[1] Pi-Hole')
    print('[2] Pi-Vpn')
    print('[3] Docker')
    print('[4] OpenMediaVault 6')
    print('[5] Apache2')
    print('[6] Nginx')
    print('[7] Homebridge')
    print('[8] I2C Display Configure')
    choice = int(input('Choice ->: '))
    if(choice == 1):
        print('')
        print('Installing Pi-Hole')
        print('')
        os.system('sudo curl -sSL https://install.pi-hole.net | sudo bash')
        installer()
    elif(choice == 2):
        print('')
        print('Installing Pi - VPN')
        print('')
        os.system('sudo curl -L https://install.pivpn.io | sudo bash')
        installer()
    elif(choice == 3):
        print('')
        print('Installing Docker')
        print('')
        os.system('sudo apt-get update && sudo apt-get upgrade -y')
        os.system('sudo curl -sSL https://get.docker.com | sudo sh')
        os.system('sudo usermod -aG docker [user_name]')
        installer()
    elif(choice == 4):
        print('')
        print('Installing OpenMediaVault')
        print('')
        os.system('sudo wget -O - https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install | sudo bash')
        installer()
    elif(choice == 5):
        print('')
        print('Installing Apache2')
        print('')
        os.system('sudo apt install apache2 -y')
    elif(choice == 6):
        print('')
        print('Installing Nginx')
        print('')
        os.system('sudo apt install nginx -y')
        installer()
    elif(choice == 7):
        print('')
        print('Installing Homebridge')
        print('')
        os.system('sudo curl -sSfL https://repo.homebridge.io/KEY.gpg | sudo gpg --dearmor | sudo tee /usr/share/keyrings/homebridge.gpg  > /dev/null && echo "deb [signed-by=/usr/share/keyrings/homebridge.gpg] https://repo.homebridge.io stable main" | sudo tee /etc/apt/sources.list.d/homebridge.list > /dev/null')
        os.system('sudo apt-get update')
        os.system('sudo apt-get install homebridge -y')
        installer()
    elif(choice == 8):
        print('')
        print('Installing')
        os.system('sudo apt-get update && sudo apt-get full-upgrade -y')
        os.system('sudo apt-get install python3-pip -y')
        os.system('sudo pip3 install --upgrade setuptools')
        os.system('sudo pip3 install --upgrade adafruit-python-shell')
        os.system('sudo wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py')
        os.system('pip3 install adafruit-circuitpython-ssd1306')
        os.system('sudo apt-get install python3-pil -y')
        os.system('sudo apt install git -y')
        os.system('git clone https://github.com/mklements/OLED_Stats.git')
        os.system('sudo python3 raspi-blinka.py')
    else:
        print('')
        print('Yo Wrong choice try again')
        print('')
        installer()

def hostname():
    hostname = input('Enter the name of the host you would like ->: ')
    f = open('/etc/hosts','r')
    f2 = open('/etc/hostname','r')
    filedata = f.read()
    filedata2 = f2.read()
    f.close()
    f2.close
    newdata = filedata.replace('raspberrypi', hostname)
    newdata2 = filedata2.replace('raspberrypi', hostname)
    f = open('/etc/hosts','w')
    f2 = open('/etc/hostname','w')
    f.write(newdata)
    f2.write(newdata2)
    print('/etc/hosts is successfully changed')
    print('')
    print('/etc/hostname is successfully changed')
    f.close()
    f2.close()

def overclocker():
    print('')
    overclock = int(input('Enter ClockSpeed MHZ ->: '))
    print('')
    overvolt = int(input('Enter Over Voltage ->: '))
    f = open('/boot/config.txt','r')
    filedata = f.read()
    newdata = filedata.replace('#arm_freq=800','arm_freq='+ str(overclock) + '\n' + 'over_voltage='+ str(overvolt))
    print('')
    print('Changing File....')
    print('')
    f.close()
    f = open('config.txt','w')
    f.write(newdata)
    f.close()
    print('File Successfully changed....')

def reboot():
    print('')
    choice = int(input('Do you want to reboot System? [1] - Yes | [2] - No :'))
    print('')
    if(choice == 1):
        os.system('sudo reboot')
    elif(choice == 2):
        main()


main()
