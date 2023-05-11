import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import re

class MagicTwix():
    def __init__(self):
        self.a_mcafeeAddUser()

    def clear(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    def a_mcafeeAddUser(self):

        self.clear()
        from selenium.webdriver.edge.options import Options

        #while (self.informations["new_pc"] == "- -"): # si le pc cible n'est pas connu
            #self.dataInput(1)

        driver = webdriver.Edge()
        driver.get("https://wpa2i264:8443/core/orionNavigationLogin.do#/ProtectionWorkspace/html/index.html")
        time.sleep(1)
        inputElement = driver.find_element(By.ID,"name")
        inputElement.send_keys("COMPTES\PTKOEH")
        inputElement = driver.find_element(By.ID,"password")
        inputElement.send_keys("Bonjour01!")
        time.sleep(0.5)
        inputElement = driver.find_element(By.ID,"login.button")
        inputElement.click()
        time.sleep(1)
        driver.get("https://wpa2i264:8443/core/orionNavigationLogin.do#/core/orionTab.do?sectionId=DataProtection&tabId=EPEADMIN.userManagement&orion.user.security.token=7atVqrpjoj5s7m5F")
        time.sleep(3)

        test = driver.find_element(By.ID,"theForm")
        test = driver.find_element(By.ID,"orion.content.disable")
        test = driver.find_element(By.ID,"orion.current.help.id")
        test = driver.find_element(By.ID,"mfsNav")
        test = driver.find_element(By.ID,"mfsNavAside")
        test = driver.find_element(By.ID,"messagecenter.nav.button")
        test = driver.find_element(By.ID,"mfsUHM")
        test = driver.find_element(By.ID,"mfsUHMButton")
        
      
        
        
        
        #select = Select(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select.orionSelect")))).select_by_value('1')
        #selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element
        """select = Select(EC.element_to_be_clickable((By.ID, "systems_filterList")))
        select.select_by_value('1')
        select.click()"""

        """
        inputElement = driver.find_element(By.ID,"systems_quickFind")
        inputElement.send_keys("L9037746")
        time.sleep(2)
        inputElement = driver.find_element(By.className("orionCheckboxV2"))
        inputElement = inputElement.find_element(By.tagName("input")).get(0);
        inputElement.click()"""
        
        
        time.sleep(5)


MagicTwix()
