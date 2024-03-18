from re import findall


class Parser(object):
    '''Класс для парсинга строк, возникающих при работе программы'''
    def __init__(self, text):
        self.origin_text = text
        self.ips = self.parse_text(self.origin_text)

    def parse_text(self, text):
        '''Метод берет на вход вывод команды traceroute и выводит список
 найденных там ipv4'''
        string_starting = '1 '
        text = self.origin_text
        text = text[text.find(string_starting):]
        pattern = r'\d+.\d+.\d+.\d+'
        found_ips = findall(pattern, text)
        return found_ips

    def parse_reply(self, rir, text):
        '''Парсит ответ на whois запрос регионального интернет регистратора rir
           и возвращает tuple (ip, asn, провайдера) '''
        if rir == 'ripe':
            ip_pattern = r'\d+\.\d+\.\d+\.\d+/\d+'
            as_pattern = r'AS\d+'
            provider_pattern = r'mnt-by: *(.*)'
        elif rir == 'afrinic':
            ip_pattern = r'\d+\.\d+\.\d+\.\d+/\d+'
            as_pattern = r'AS\d+'
            provider_pattern = r'mnt-by: *(.+)'
        elif rir == 'arin':
            ip_pattern = r'\d+\.\d+\.\d+\.\d+/\d+'
            as_pattern = r'AS\d+'
            provider_pattern = r'NetHandle: +(.*)'
        elif rir == 'apnic':
            ip_pattern = r'\d+\.\d+\.\d+\.\d+/\d+'
            as_pattern = r'AS\d+'
            provider_pattern = r'NetHandle: +(.*)'
        ip_found = findall(ip_pattern, text)
        as_found = findall(as_pattern, text)
        provider_found = findall(provider_pattern, text)
        ip = self._choose_from_parsed(ip_found)
        asys = self._choose_from_parsed(as_found)
        provider = self._choose_from_parsed(provider_found)
        return ip, asys, provider

    def _choose_from_parsed(self, found_items):
        '''Метод, который выбирает наидлиннейший из элементов списка,
или возвращает None если элементов нет'''
        if len(found_items) > 1:
            return max(found_items, key=len)
        elif len(found_items) == 0:
            return None
        else:
            return found_items[0]


if __name__ == '__main__':
    pass
