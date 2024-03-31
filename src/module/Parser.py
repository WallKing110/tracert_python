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
            as_pattern = r'AS\d+'
            provider_pattern = r'mnt-by: *(.*)'
        elif rir == 'afrinic':
            as_pattern = r'AS\d+'
            provider_pattern = r'mnt-by: *(.+)'
        elif rir == 'arin':
            as_pattern = r'AS\d+'
            provider_pattern = r'NetHandle: +(.*)'
        elif rir == 'apnic':
            as_pattern = r'AS\d+'
            provider_pattern = r'NetHandle: +(.*)'
        as_found = findall(as_pattern, text)
        provider_found = findall(provider_pattern, text)
        asys = self._choose_from_parsed(as_found)
        provider = self._choose_from_parsed(provider_found)
        result = {'ip': '', 'asys': asys, 'provider': provider}
        return result

    def _choose_from_parsed(self, found_items):
        '''Метод, который выбирает наидлиннейший из элементов списка,
или возвращает None если элементов нет'''
        if len(found_items) > 1:
            return max(found_items, key=len)
        elif len(found_items) == 0:
            return ' '
        else:
            return found_items[0]


if __name__ == '__main__':
    pass
