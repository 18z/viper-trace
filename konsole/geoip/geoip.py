import re
import os
import socket
import IP2Location

from csv import reader
from urllib import urlopen


class GeoIP:

    def __init__(self, querystring):
        self.ip2location_file = os.path.dirname(
            __file__)+"/IP2Location_DB20.BIN"
        self.URL = "http://10.3.40.55:8080/csv/%s"

        # check the querystring is IP or Domain name.
        ipPattern = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
        dnPattern = re.compile('^[a-zA-Z\d-]{,63}(\.[a-zA-Z\d-]{,63})*$')
        if re.findall(ipPattern, querystring):
            self.ip = querystring
        elif re.findall(dnPattern, querystring):
            self.dn = querystring

    def _dn2ip(self, dn):
        try:
            result = socket.gethostbyname(dn)
        except socket.gaierror:
            return None

        return result

    def _query_freegeoip(self, ip):
        URL = self.URL % ip
        response_csv = reader(urlopen(URL))
        csv_data = response_csv.next()

        return csv_data

    def ip2countrycode(self):
        if hasattr(self, 'ip'):
            csv_data = self._query_freegeoip(self.ip)

            return csv_data[1]
        else:
            return None

    def ip2countryname(self):
        if hasattr(self, 'ip'):
            csv_data = self._query_freegeoip(self.ip)

            return csv_data[2]
        else:
            return None

    def ip2location(self):
        if hasattr(self, 'ip'):
            IP2LocObj = IP2Location.IP2Location()
            IP2LocObj.open(self.ip2location_file)
            result = IP2LocObj.get_all(self.ip)

            return result
        else:
            return None

    def dn2countrycode(self):
        if hasattr(self, 'dn'):
            ip = self._dn2ip(self.dn)
            csv_data = self._query_freegeoip(ip)

            if csv_data[0] != 'Not Found':
                return csv_data[1]
            else:
                return None
        else:
            return None

    def dn2countryname(self):
        if hasattr(self, 'dn'):
            ip = self._dn2ip(self.dn)
            csv_data = self._query_freegeoip(ip)

            if csv_data[0] != 'Not Found':
                return csv_data[2]
            else:
                return None
        else:
            return None
