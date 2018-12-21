
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.common.by import By
driver  = webdriver.Chrome()

driver.get("https://pre.svocloud.com")
a = driver.get_cookies()
print(a)
driver.find_element_by_css_selector("[formcontrolname='username']").send_keys(18600929870)
driver.find_element_by_css_selector("[formcontrolname='password']").send_keys(123456)
driver.find_element_by_css_selector("button").click()
#提交操作；submit可以提交内容，来达到clike的作用
#driver.find_element_by_css_selector("a[herf='#/page/meeting/conference-management']").submit()
sleep(5)
a = driver.find_element_by_css_selector("a > span").text
print(a)
"""
I have a dream
Delivered on the steps at the Lincoln Memorial in Washington D.C. on August 28, 1962.
Source; Martin Luther King,Jr; The Peaceful Warrior,Pocket Books, NY 1968

I am happy to join with you today in what will go down in history as the greatest
drmonstration for freedom in the history of our nation.

Five score years ago, a great American , in whose symbolic shadow we stand today,
signed the Emancipation Proclamation. This momentous decree came as great beacon
light of hope to millons of Negro slaves who had been seared in the flames of withering
injustive. It came as a joyous daybrreak to end the long night of bad captivity.

But one hundred years late, the Negro still is not free. One hundred years later, the
life of the Negro is still crippled by the manacles of segregation and the chains of
discreimination. One hundred years later, the Negro lives on a lonly island of poverty in the
midst of a vast ocean of material prosperity. One hundred years later, the Negro is still
languished in the corners of American society and finds himself an exile in his own land.So
we've come here today to dramatize a shameful condition.

In a sense we have come to our nation's capital to cash a cheque.When the architects
of our republic wrote the magnificient words of the Constitution and the Declaration of 
Independence, they were signing a promissory note to which every American was to fall 
heir. This note was a promise that all men , yes, black men as well as white men, would be
guarantedd the unalienable rights of life, liberty, and the pursuit of happiness 

It is obvious today that America has defaulted on this promissory note in sofar as her
citizens of color are concerned. Instead of honoring this sacred obligation, America has
given the Negro people a bad cheque, a cheque which has come back marked "insufficient
funds". But we refuse to believe that the bank of justice is bankrupt. We refuse to believe
that ehre aere insufficient funds in the great vaults of oppourtunity of this nation. So we
have come to cash this cheque -- a cheque that will give up upon demand the riches of 
freedom and the security of justice. We have also come to this hallowed spot to remind
Amrica of the fierce urgency of now. This is no time to engage in the luxury of cooling off
or to take the tranquilizing drug of gradualism. Now is the time to make real the promises
of democracy. Now is the time to rise from the dark and desolate valley of segregation to 
the sunlit path of racial justice. Now is the time to lift our nation from the quick sands of 
racial injestice to the solid rock of brotherhood. Now is the time to make justice a reality
for all of God's children.

It would be fatal for the nation to overlook the urgency of the moment. This sweltering
summer of the Negro's legitimate discontent will not pass until there is an invigorating
autumn of freedom and queality. Nineteen sixty-three is not an end, but a beginning.
Those who hope that the Negro needed to blow off steam and will now be content will
have a rude awakening if the nation retruns to business as usual. There will be neither rest
nor tranquility in America until the Negro is granted his citizenship rights. The whirlwinds
of revolt will continue to shake the fondations of our nation until the bright day of justice
emerges.

But there is something that i must say to my people who shand on the warm threshold
which leads into the palace of justice. In the process  

"""
