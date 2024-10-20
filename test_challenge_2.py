import unittest
import re

class PC:
    def __init__(self, ip_address, mac_address):
        self.ip_address = ip_address
        self.mac_address = mac_address

    def is_valid_ip(self):
        return bool(re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", self.ip_address)) and all(0 <= int(part) <= 255 for part in self.ip_address.split('.'))

    def is_valid_mac(self):
        return bool(re.match(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", self.mac_address))

class TestPCConfig(unittest.TestCase):
    def test_ip_and_mac(self):
        valid_pc = PC("192.168.1.1", "00:1A:2B:3C:4D:5G")
        invalid_mac_pc = PC("256.100.50.25", "00:1A:2B:3C:4D:5G")

        self.assertTrue(valid_pc.is_valid_ip())
        self.assertTrue(valid_pc.is_valid_mac())
if __name__ == "__main__":
    unittest.main()