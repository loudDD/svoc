import yaml
import unittest
import ddt

y = open("yamlpractice.yaml")
z = yaml.load(y)
print(z)
print(type(z))
@ddt.ddt
class login(unittest.TestCase):

    # @ddt.data([123,321],[111,222])

    @ddt.data({"user":"123","pwd":"222"},{"user":"321","pwd":"000"})
    @ddt.unpack
    # @ddt.ddt(z)
    def test_login(self,user,pwd):
        print("user:", user)
        print("pwd:", pwd)


if __name__=="__main__":
    unittest.main()