import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

print('初始化浏览器')
ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 ' \
     'MicroMessenger/6.3.27 NetType/WIFI Language/zh_CN '

option = webdriver.ChromeOptions()
option.headless = True
option.add_argument('user-agent=' + ua)
# driver = webdriver.Chrome(executable_path='D://webdrivers/chromedriver.exe', options=option)
driver = webdriver.Chrome(executable_path= '/usr/bin/chromedriver', options = option)
USERNAME = os.environ['ID']
PASSWORD = os.environ['PASSWORD']

print('正在上报')
driver.get('https://ids.hit.edu.cn/authserver/')
driver.find_element_by_id('mobileUsername').send_keys(USERNAME)
driver.find_element_by_id('mobilePassword').send_keys(PASSWORD)
driver.find_element_by_id('load').click()

success = False

for i in range(0, 5):
    try:
        driver.get('https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsMrsbNew/index')
        driver.execute_script(f'gpsjd = 126.633353')
        driver.execute_script(f'gpswd = 45.74274')
        driver.execute_script(f'kzl6 = "黑龙江省"')
        driver.execute_script(f'kzl7 = "哈尔滨市"')
        driver.execute_script(f'kzl8 = "南岗区"')
        driver.execute_script(f'kzl9 = "工建街9号"')
        driver.execute_script(f'kzl10 = "黑龙江省哈尔滨市南岗区花园街道哈尔滨工业大学西苑小区"')
        driver.execute_script(f'kzl38 = "黑龙江省"')
        driver.execute_script(f'kzl39 = "哈尔滨市"')
        driver.execute_script(f'kzl40 = "南岗区"')
        driver.execute_script('document.getElementById("txfscheckbox").click()')
        driver.find_element_by_class_name('submit').click()
        success = True
        break
    except:
        print('失败' + str(i + 1) + '次，正在重试...')
driver.quit()
if success:
    print('上报完成')
else:
    raise Exception('上报多次失败，可能学工系统已更新')
