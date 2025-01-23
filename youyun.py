import time

from util import *

username = sys.argv[1]  # 登录账号
password = sys.argv[2]  # 登录密码

# 检查元素是否存在
# 手动触发


def check_element_exists(driver, element, condition):
    try:
        if condition == 'class':
            driver.find_element_by_class_name(element)
        elif condition == 'id':
            driver.find_element_by_id(element)
        elif condition == 'xpath':
            driver.find_element_by_xpath(element)
        return True
    except Exception as e:
        return False


@retry(stop_max_attempt_number=5)
def youyun():
    try:
        driver = get_web_driver()
        driver.get("https://youyun666.com/auth/login")
        driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath(
            "//*[@class='btn btn-primary btn-lg btn-block login']").click()

        # driver.find_element_by_xpath("//*[@id='rectBottom']").click()
        time.sleep(10)
        modelReadBtnIsExit = check_element_exists(
            driver, "//div[@class='modal-content']/div[3]/button[1]", "xpath")
        if modelReadBtnIsExit:
            driver.find_element_by_xpath(
                "//div[@class='modal-content']/div[3]/button[1]").click()
        time.sleep(10)
        driver.find_element_by_xpath(
            "//*[@id='checkin-div']/a[1]").click()  # signIn
    except:
        raise
    finally:
        driver.quit()


if __name__ == '__main__':
    youyun()
