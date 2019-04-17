from page.basepage import POM
from time import sleep

class StartMeeting(POM):

    with open(r"C:\Users\loudDD\GitProject\svoc\svoc\Locator\rootpage.json", "r", encoding="utf-8") as f:
        # login
        startmeeting = f["Pripage"]["startmeeting"]

    def start_real_time_meeting(self):
        #创建实时会议
        self.findelement(self.startmeeting).click()