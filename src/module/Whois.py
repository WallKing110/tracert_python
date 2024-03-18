import socket
from chardet import detect


PORT = 43
HOSTS = {'ripe': 'whois.ripe.net',
         'arin': 'whois.arin.net',
         'lacnic': 'whois.lacnic.net',
         'apnic': 'whois.apnic.net',
         'afrinic': 'whois.afrinic.net'
         }


class Whois(object):
    '''Класс для работы с запросами к whois серверам'''
    def __init__(self, ips):
        self.ips = ips

    def get_whois(self, host, ip):
        '''Получает на вход сервер whois и ip, который нужно спросить.
Возвращает строку-ответ whois сервера'''
        output = ''
        ip = ip + '\r\n'
        ip = ip.encode()
        s = socket.create_connection((HOSTS[host], PORT))
        s.sendall(ip)
        while True:
            buf = s.recv(4096)
            if len(buf) == 0:
                return output
            encoding = detect(buf)['encoding']
            buf = buf.decode(encoding)
            output += buf

    def find_right_rir(self, ip):
        '''Метод берет на вход ipv4, возвращает сервер whois для ip''' 
        text = self.get_whois('afrinic', ip)
        if text.find('LACNIC') != -1:
            return 'lacnic'
        elif text.find('RIPENCC') != -1:
            return 'ripe'
        elif text.find('APNIC') != -1:
            return 'apnic'
        elif text.find('ARIN') != -1:
            return 'arin'
        elif text.find('Country is really world wide') != -1:
            return None
        else:
            return 'afrinic'


if __name__ == '__main__':
    pass
