# CPU Temperature example

from gpiozero import CPUTemperature
import time
import socket

def main():
    sock = sk_init()
    cpu = CPUTemperature()

    while True:
        temp_c = cpu.temperature
        temp_f = round(temp_c * (9.0 / 5.0) + 32.0, 2)
        temp_k = round(temp_c + 273.15, 1)
        # print('CPU Temperature: {}F'.format(temp_f))
        sk_send(sock, "environment.inside.lituyamon.temperature", temp_k)

        # propulsion.1.temperature
        # environment.inside.engineRoom.temperature
        # environment.outside.temperature
        # /vessels/<RegExp>/environment/inside/[A-Za-z0-9]+/temperature
        # electrical.alternators.1.temperature.warnUpper

        time.sleep(5)

def sk_send(sock, path, value):
   sk_delta_msg='{"updates": [{"$source": "lituyamon","values":[ {"path":"'+ path +'","value":'+ str(value) + '}]}]}\n'
   print(sk_delta_msg.encode())
   sock.sendto(sk_delta_msg.encode(), ('127.0.0.1', 55557))


def sk_init():
    # Initiate socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # socket.AF_INET is  Internet
    # socket.SOCK_DGRAM) is  UDP
    return(sock)

main()