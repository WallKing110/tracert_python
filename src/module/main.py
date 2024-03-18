from Parser import Parser
from Whois import Whois
from Consoler import Consoler
from Consoler import UnreachableHostException
import sys
from socket import gaierror


class Main(object):
    '''Класс, содержащий скрипт для выполнения'''
    def __init__(self):
        self.main()

    def check_args(self):
        '''Метод проверяет аргументы скрипта, если -h или --help, то
возвращает справку, если дан ip или домен, то возрващает соответствующую
строку'''
        if len(sys.argv) == 1:
            return self.helper()
        elif len(sys.argv) > 2:
            return self.helper
        elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
            return self.helper()
        elif Consoler.is_ip(sys.argv[1]):
            return 'ip'
        elif Consoler.is_domain(sys.argv[1]):
            return 'domain'
        else:
            return self.helper()

    def helper(self):
        '''Метод выводит справку к программе'''
        print('Запуск: script.py domain/ip')
        print('Данная программа принимает на вход или домен, или ipv4.\n' +
              'На выход выдает список ip, asn и провайдера' +
              'встретившихся на трассировке ip-адресов.'
              )

    def main(self):
        '''Main-метод скрипта'''
        try:
            arg = self.check_args()
        except gaierror as e:
            print('Не удалось разрешить ip адрес хоста. ' +
                  'Проверьте правописание.')
            return
        if arg == 'ip':
            ip_target = sys.argv[1]
        elif arg == 'domain':
            ip_target = Consoler.get_ip_from_domain(sys.argv[1])
        else:
            return
        try:
            c = Consoler(ip_target)
        except UnreachableHostException as e:
            print(e)
            return
        p = Parser(c.output)
        w = Whois(p.ips)
        for ip in w.ips:
            rir = w.find_right_rir(ip)
            if rir is None:
                continue
            whois_reply = w.get_whois(rir, ip)
            parsed_reply = p.parse_reply(rir, whois_reply)
            parsed_reply['ip'] = ip
            print(parsed_reply['ip'] + ' ' +
                  parsed_reply['asys'] + ' ' +
                  parsed_reply['provider']
                  )
        print('Программа завершила работу')
        return


if __name__ == '__main__':
    main = Main()
