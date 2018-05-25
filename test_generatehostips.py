import generatehostips
import  unittest

class TestAdd(unittest.TestCase):
    def test_gethostips(self):
        result = generatehostips.get_HostIps("www.baidu.com\n")
        print(result)
        self.assertFalse(not result)


if __name__ == '__main__':
    unittest.main()