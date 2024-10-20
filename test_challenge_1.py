import unittest

class Router:
    def __init__(self, location, ip_address, subnet_mask):
        self.location = location
        self.ip_address = ip_address
        self.subnet_mask = subnet_mask

class TestRouterConfig(unittest.TestCase):
    def test_router_config(self):
        router = Router("TIP_Manila", "192.168.45.25", "255.255.255.0")
        
        self.assertEqual(router.location, "TIP_Manila")
        self.assertEqual(router.ip_address, "192.168.45.25")
        self.assertEqual(router.subnet_mask, "255.255.255.0")

if __name__ == "__main__":
    unittest.main()