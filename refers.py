import time
from selenium import webdriver

LoginVals = ["//*[@id='login']/table/tbody/tr[1]/td[2]/input", "admin", "//*[@id='login']/table/tbody/tr[2]/td[2]/input", "//*[@id='login']/table/tbody/tr[3]/td[2]/input[1]"]
OCvals = ["/html/body/table/tbody/tr/td[2]/table[3]/tbody/tr[3]/td/a", "/html/body/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr[3]/td/a"]
DelayVals = ["/html/body/table/tbody/tr/td[2]/form[2]/div/table/tbody/tr[1]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[2]/div/table/tbody/tr[3]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[2]/div/table/tbody/tr[7]/td/input"]
PowerlossVals = ["/html/body/table/tbody/tr/td[2]/form[3]/div/table/tbody/tr[1]/td[2]/input[2]", "/html/body/table/tbody/tr/td[2]/form[3]/div/table/tbody/tr[3]/td/input"]
WifiVals = ["/html/body/table/tbody/tr/td[2]/form[7]/div[2]/table/tbody/tr[1]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[7]/div[2]/table/tbody/tr[13]/td/input", "/html/body/table/tbody/tr/td/p[3]/a"]
PlaintextVals = ["/html/body/table/tbody/tr/td[2]/form[12]/div/table/tbody/tr[1]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[12]/div/table/tbody/tr[6]/td/input"]
AccessnameVals = ["//*[@id='login1']", "administrator", "//*[@id='password1']", "CAL1108cal"]
AccessOutletVals = ["//*[@id='perm1_1']", "//*[@id='perm1_2']", "//*[@id='perm1_3']", "//*[@id='perm1_4']", "//*[@id='perm1_5']", "//*[@id='perm1_6']", "//*[@id='perm1_7']", "//*[@id='perm1_8']", "/html/body/table/tbody/tr/td[2]/form[11]/div[2]/table/tbody/tr[3]/td[11]/input"]
AdminVals = ["/html/body/table/tbody/tr/td[2]/form[9]/div[2]/table/tbody/tr[2]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[9]/div[2]/table/tbody/tr[3]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[9]/div[2]/table/tbody/tr[4]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[9]/div[2]/table/tbody/tr[5]/td[1]/input"]
LANxvals = ["/html/body/table/tbody/tr/td[2]/form[6]/div/table/tbody/tr[3]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[6]/div/table/tbody/tr[5]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[6]/div/table/tbody/tr[6]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[6]/div/table/tbody/tr[7]/td/input", "/html/body/table/tbody/tr/td/p[3]/a"]
LANvals = ["192.168.168.206", "192.168.168.168", "8.8.8.8"]
Unitxvals = ["/html/body/table/tbody/tr/td[2]/form[1]/div/table/tbody/tr[1]/td[2]/input","/html/body/table/tbody/tr/td[2]/form[1]/div/table/tbody/tr[2]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[1]/div/table/tbody/tr[3]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[1]/div/table/tbody/tr[4]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[1]/div/table/tbody/tr[5]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[1]/div/table/tbody/tr[6]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[1]/div/table/tbody/tr[7]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[1]/div/table/tbody/tr[8]/td[2]/input", "/html/body/table/tbody/tr/td[2]/form[1]/div/table/tbody/tr[9]/td[2]/input"]

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome()
driver.get("http://192.168.0.100")

def clear(x):
    driver.find_element_by_xpath(x).clear() #clears the default start time
    time.sleep(0.001)
    return

class funcss:
    def login(y):
        driver.find_element_by_xpath(LoginVals[0]).send_keys(LoginVals[1])
        driver.find_element_by_xpath(LoginVals[2]).send_keys(y)
        driver.find_element_by_xpath(LoginVals[3]).click()
        time.sleep(0.5)
        return
    def set_outlet():
        driver.find_element_by_xpath(OCvals[0]).click()
        driver.find_element_by_xpath(OCvals[1]).click()
        return
    def set_delay():
        clear(DelayVals[0])
        driver.find_element_by_xpath(DelayVals[0]).send_keys("3")
        clear(DelayVals[1])
        driver.find_element_by_xpath(DelayVals[1]).send_keys("3")
        time.sleep(1)
        driver.find_element_by_xpath(DelayVals[2]).click()
        time.sleep(1)
        return
    def set_powerloss():
        driver.find_element_by_xpath(PowerlossVals[0]).click()
        driver.find_element_by_xpath(PowerlossVals[1]).click()
        time.sleep(1)
        return
    def set_wifi():
        driver.find_element_by_xpath(WifiVals[0]).click()
        driver.find_element_by_xpath(WifiVals[1]).click()
        driver.switch_to_alert().accept()
        time.sleep(1)
        driver.find_element_by_xpath(WifiVals[2]).click()
        time.sleep(0.5)
        return
    def set_plaintext():
        driver.find_element_by_xpath(PlaintextVals[0]).click()
        driver.find_element_by_xpath(PlaintextVals[1]).click()
        time.sleep(0.5)
    def set_access():
        clear(AccessnameVals[0])
        driver.find_element_by_xpath(AccessnameVals[0]).send_keys(AccessnameVals[1])
        clear(AccessnameVals[2])
        driver.find_element_by_xpath(AccessnameVals[2]).send_keys(AccessnameVals[3])
        time.sleep(0.1)
        driver.find_element_by_xpath(AccessOutletVals[0]).click()
        driver.find_element_by_xpath(AccessOutletVals[1]).click()
        driver.find_element_by_xpath(AccessOutletVals[2]).click()
        driver.find_element_by_xpath(AccessOutletVals[3]).click()
        driver.find_element_by_xpath(AccessOutletVals[4]).click()
        driver.find_element_by_xpath(AccessOutletVals[5]).click()
        driver.find_element_by_xpath(AccessOutletVals[6]).click()
        driver.find_element_by_xpath(AccessOutletVals[7]).click()
        driver.find_element_by_xpath(AccessOutletVals[8]).click()
    def set_admincred(t,u):
        time.sleep(0.5)
        driver.find_element_by_xpath(AdminVals[0]).send_keys(u)
        driver.find_element_by_xpath(AdminVals[1]).send_keys(t)
        driver.find_element_by_xpath(AdminVals[2]).send_keys(t)
        driver.find_element_by_xpath(AdminVals[3]).click()
        time.sleep(0.5)
        return
    def set_lan(q,w,e):
        clear(LANxvals[0])
        driver.find_element_by_xpath(LANxvals[0]).send_keys(q)
        driver.find_element_by_xpath(LANxvals[1]).send_keys(w)
        driver.find_element_by_xpath(LANxvals[2]).send_keys(e)
        driver.find_element_by_xpath(LANxvals[3]).click()
        driver.switch_to_alert().accept()
        time.sleep(1)
        driver.switch_to_default_content()
        driver.find_element_by_xpath("/html/body/table/tbody/tr/td/p[3]/a").click()
        return
    def set_units(a,b,c,d,e,f,g,h,i):
        time.sleep(1)
        clear(Unitxvals[0])
        driver.find_elements_by_xpath(Unitxvals[0]).send_keys(a)
        clear(Unitxvals[1])
        driver.find_elements_by_xpath(Unitxvals[1]).send_keys("testt")
        clear(Unitxvals[2])
        driver.find_elements_by_xpath(Unitxvals[2]).send_keys(c)
        clear(Unitxvals[3])
        driver.find_elements_by_xpath(Unitxvals[3]).send_keys(d)
        clear(Unitxvals[4])
        driver.find_elements_by_xpath(Unitxvals[4]).send_keys(e)
        clear(Unitxvals[5])
        driver.find_elements_by_xpath(Unitxvals[5]).send_keys(f)
        clear(Unitxvals[6])
        driver.find_elements_by_xpath(Unitxvals[6]).send_keys(g)
        clear(Unitxvals[7])
        driver.find_elements_by_xpath(Unitxvals[7]).send_keys(h)
        clear(Unitxvals[8])
        driver.find_elements_by_xpath(Unitxvals[8]).send_keys(i)
        return

funcss.login("CAL1108cal")
funcss.set_outlet()
funcss.set_delay()
