import unittest
import ipaddress

class Subnet:
    def __init__(self, prefix_length):
        self.prefix_length = prefix_length

    def get_subnet_mask(self):
        return str(ipaddress.IPv4Network(f'0.0.0.0/{self.prefix_length}', strict=False).netmask)

    def is_valid_subnet_mask(self, subnet_mask):
        expected_mask = self.get_subnet_mask()
        return expected_mask == subnet_mask

class TestSubnetMask(unittest.TestCase):
    def test_subnet_mask_validation(self):
        subnet = Subnet(24)
        valid_mask = "255.255.255.254"

        self.assertTrue(subnet.is_valid_subnet_mask(valid_mask), "Subnet mask should be valid for /24 prefix.")

if __name__ == "__main__":
    unittest.main()