import requests
import sys
import urllib

class GeoLookup:

    def __init__(self, api_key):
        self.__api_key = api_key
        self.__timeout = 10
        self.__use_https = False
        self.__find_hostname = False
        self.__assess_security = False
        self.__language = "en"

    def get_location(self, *ips):
        if len(ips) > 50:
            raise Exception(
                "IPStack Error: Bulk lookup limited to "
                "50 IP addresses at a time."
            )

        ips = map(lambda ip: self.__format_ip(ip), ips)

        url = ("http" if not self.__use_https else "https") + \
            "://api.ipstack.com/"
        url = url + ",".join(ips) + "?access_key=" + self.__api_key
        url = url + "&output=json"
        url = url + ("&hostname=1" if self.__find_hostname else "")
        url = url + ("&security=1" if self.__assess_security else "")
        url = url + "&language=" + self.__language
        r = requests.get(url, timeout=self.__timeout)
        return self.__process_response(r)

    def get_own_location(self):
        return self.get_location(requests.get('https://ip.42.pl/raw').text)

    def __format_ip(self, ip):
        if sys.version_info > (3, 0):
            return urllib.parse.quote_plus(ip)
        else:
            return urllib.quote(ip)

    def __process_response(self, response):
        if response.status_code == 200:
            json = response.json()
            if "error" in json.keys():
                raise Exception("IPStack Error: " + json["error"]["info"])
            return json
        return None

    def find_hostname(self):
        self.__find_hostname = True
        return self

    def use_https(self):
        self.__use_https = True
        return self

    def assess_security(self):
        self.__assess_security = True
        return self

    def timeout(self, val):
        self.__timeout = val
        return self

    def language(self, val):
        self.__language = val
        return self
