from abc import ABC, abstractmethod
import re

class Dispositivo(ABC):
    def __init__(self, ip: str, mac: str):
        if self.Validando_IP(ip) and self.Validando_MAC(mac):
            self.__ip = ip
            self.__mac = mac

    @property
    def ip(self):
        return self.__ip

    @property
    def mac(self):
        return self.__mac

    @ip.setter
    def ip(self, novoIp):
        self.__ip = novoIp

    @mac.setter
    def mac(self, novoMac):
        self.__mac = novoMac

    @abstractmethod
    def Validando_IP(self, ip: str):
        partes = ip.split(".")
        if len(partes) != 4:
            return False
        for item in partes:
            if not 0 <= int(item) <= 255:
                return False
        return True

    @abstractmethod
    def Validando_MAC(self, mac: str):
        regex = (
            "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})|" +
            "([0-9a-fA-F]{4}\\.[0-9a-fA-F]{4}\\.[0-9a-fA-F]{4})$"
        )
        p = re.compile(regex)
        if (mac is None):
            return False
        if(re.search(p, mac)):
            return True
        else:
            return False

    def __str__(self):
        return f"Endereço IP: {self.__ip}, Endereço MAC: {self.__mac}"
