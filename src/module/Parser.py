from re import findall
from Consoler import Consoler

class Parser(object):
    def __init__(self, text):
        self.origin_text = text
        self.ips = self.parse_text(self.origin_text)

    def parse_text(self, text):
        string_starting = '1 '
        text = self.origin_text
        text = text[text.find(string_starting):]
        pattern = r'\d+.\d+.\d+.\d+'
        found_ips = findall(pattern, text)
        return found_ips

if __name__ == '__main__':
    c = Consoler('8.8.8.8')
    p = Parser(c.output)
    print (p.ips)
