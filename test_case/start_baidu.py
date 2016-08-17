# coding=utf-8
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
import unittest
import time
# import re
import HTMLTestRunner


class Baidu(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.baidu.com/'
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_id('kw').send_keys('selenium webdriver')
        driver.find_element_by_id('su').click()
        time.sleep(2)
        driver.close()

    def test_baidu_set(self):
        driver = self.driver
        driver.get(self.base_url + '/gaoji/preference.html')
        m = driver.find_element_by_name('NR')
        m.find_element_by_xpath('//option[@value=100]').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/form/div/input').click()
        time.sleep(2)
        driver.switch_to.alert().accept()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu('test_baidu_search'))
    testunit.addTest(Baidu('test_baidu_set'))

    filename = 'D:\\Practice\\Python+Selenium\\report\\result.html'
    fp = file(filename, 'wb+')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'百度搜索测试报告', description=u'用例执行情况:')
    runner.run(testunit)

