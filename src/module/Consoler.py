import os
from sys import platform
from re import findall


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

    def capture_command(self, ip):
        p = os.popen(self.command + ' ' + ip)
        output = p.readlines()
        p.close()
        output = ''.join(output)
        return output

    def check_succeed(self, text):
        if self.system == 'linux':
            end_of_incmpt_out = '* * */n'
            index_of_incmplt_out = text.rfind(end_of_incmplt_out)
            if index_of_incmplt_out == len(end_of_incmplt_out):
                raise UnreachableHostException(self.ip)
        elif self.system == 'win':
            len_of_ending_string = 26
            max_len_of_ipv4 = 20
            if text.rfind(self.ip) < len_of_ending_string + max_len_of_ipv4 + 1:
                raise UnreachableHostException(self.ip)
        

class UnreachableHostException(Exception):
    def __init__(self, ip):
        self.ip = ip

    def __str__(self):
        return 'Не получилось добраться до хоста {1},'\
               'Попробуйте другой ip-адрес.'.format(self.ip)

if __name__ == '__main__':
    c = Consoler('8.8.8.8')
    print (c.output)
