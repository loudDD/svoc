from page.loginpage import LoginPage
import unittest
from public.logger import Logger


class signin(unittest.TestCase):

    def setUp(self):
        self.logger = Logger("debug").getLog()
    def tearDown(self):
        pass

    def test_signin(self):
        try:
            LoginPage().sigin()