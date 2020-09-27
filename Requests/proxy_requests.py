# -*- coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup

class proxy_requests():
    def __init__(self, logging=False):
        self.required = ["requests"]
        self.proxies = proxy_requests.crawl_proxies(logging)
        self.logging = logging

    @staticmethod
    def crawl_proxies(logging=False):
        """
        Comment: gets available proxies for use with python requests
        Input: None
        Output: List of proxies
        Special: Nothing special
        """
        url = "https://www.sslproxies.org/"
        proxies = []
        r = requests.get(url)
        s = BeautifulSoup(r.text, "html.parser")
        for i in s.find_all("tr"):
            try:
                data = i.find_all("td")
                adress = data[0].text
                port = data[1].text
                proxy = "{adress}:{port}"
                proxy = proxy.format(adress=adress, port=port)
                proxies.append(proxy)
            except Exception as e:
                if logging:
                    print (e)
                else:
                    pass
        return proxies[:-16]
    def get_proxies(self, logging):
        """
        Comment: gets the proxies without BeautifulSoup
        Input:
        Output:
        Special: BeautifulSoup not needed
        """

    def get_curr_proxies(self):
        """
        Comment: returns all currently saved proxies
        Input: name of Instance
        Output: List of Proxies
        Special: Does NOT renew the proxies
        """
        return self.proxies



def main():
    test = proxy_requests()
    print (test.get_proxies())

if __name__ == '__main__':
    main()
