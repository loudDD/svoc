from page.basepage import POM
from time import sleep


class RootPage(POM):
    with open(r"C:\Users\loudDD\GitProject\svoc\svoc\Locator\rootpage.json", "r", encoding="utf-8") as f:
        # login
        startmeeting = f["Pripage"]["startmeeting"]

    def create_real_time_meeting(self):
        self.findelement()
