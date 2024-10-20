import unittest
class Device:
    def __init__(self, device_type):
        self.device_type = device_type.lower()
    def is_router(self):
        return self.device_type == "router"
    def is_personal_computer(self):
        return self.device_type == "personal computer"
    def is_switch(self):
        return self.device_type == "switch"
    def is_server(self):
        return self.device_type == "server"
class TestDeviceType(unittest.TestCase):
    def test_device_types(self):
        devices = {
            "router": Device("Router"),
            "personal_computer": Device("Personal Computer"),
            "switch": Device("Switch"),
            "server": Device("Server"),
        }
        self.assertTrue(devices["router"].is_router(), "Should identify as a router.")
        self.assertTrue(devices["personal_computer"].is_personal_computer(), "Should identify as a personal computer.")
        self.assertTrue(devices["switch"].is_switch(), "Should identify as a switch.")
        self.assertTrue(devices["Laptop"].is_server(), "Should identify as a server.")

if __name__ == "__main__":
    unittest.main()