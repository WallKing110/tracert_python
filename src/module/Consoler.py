import os
from sys import platform
from re import findall
from socket import gethostbyname
from socket import gaierror


class Consoler(object):
    '''Класс, который предназнаечен для общения с командной строкой'''
    def __init__(self, ip):
        self.ip = ip
        self.system = platform
        self.command = ''
        if self.system.startswith('win'):
            self.system = 'win'
            self.command = 'tracert /d /w 500'
        elif self.system.startswith('linux'):
            self.system = 'linux'
            self.command = 'traceroute -I -n'
        self.output = self.capture_command(self.ip)
        self.check_succeed(self.output)

    @staticmethod
    def get_ip_from_domain(domain):
        '''domain -> ip'''
        ip = gethostbyname(domain)
        return ip

    def capture_command(self, ip):
        '''ip -> текст команды по трассировке'''
        p = os.popen(self.command + ' ' + ip)
        output = p.readlines()
        p.close()
        output = ''.join(output)
        return output

    def check_succeed(self, text):
        '''Метод берет на вход текст команды traceroute и поднимает
ошибку, если не удалось дотрассироваться до конечного хоста'''
        if self.system == 'linux':
            end_of_incmpt_out = '* * */n'
            index_of_incmplt_out = text.rfind(end_of_incmplt_out)
            if index_of_incmplt_out == len(end_of_incmplt_out):
                raise UnreachableHostException(self.ip)
        elif self.system == 'win':
            len_of_ending_string = 27
            max_len_of_ipv4 = 20
            if text.rfind(self.ip) < len_of_ending_string + max_len_of_ipv4:
                raise UnreachableHostException(self.ip)

    @staticmethod
    def is_ip(text):
        '''Метод берет на вход текст и возвращает True если этот текст ipv4
без маски, либо False, если нет.'''
        ip_pattern = r'\d+\.\d+\.\d+\.\d+'
        ip_found = findall(ip_pattern, text)
        if len(ip_found) != 1:
            return False
        if text == ip_found[0]:
            return True
        return False

    @staticmethod
    def is_domain(text):
        '''Метод берет на вход текст и возвращает True если из этого текста
можно получить ipv4 адрес, либо выбрасывает исключение socket.gaierror'''
        ip = gethostbyname(text)
        return True


class UnreachableHostException(Exception):
    '''Класс-исключение, которое предназначено для сигнализирования о том,
что не удалось добраться до конечного пункта трассировки'''
    def __init__(self, ip):
        self.ip = ip

    def __str__(self):
        return 'Не получилось добраться до хоста {0},'\
               'Попробуйте другой ip-адрес.'.format(self.ip)


if __name__ == '__main__':
    pass
