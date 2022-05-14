import sys

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://buchung.wangerooge.de/?&page=vermietung&from=leistung')
browser.implicitly_wait(2000)
firstDiv = browser.find_element(By.ID, "typ_1_1_heading")
firstDiv.click()
secondDiv = browser.find_element(By.ID, 'vermietung_kalender_1_1_von')
secondDiv.click()

startDateInput = browser.find_element(By.ID, 'vermietung_kalender_1_1_von')
endDateInput = browser.find_element(By.ID, 'vermietung_kalender_1_1_bis')
startDateInput.clear()
startDateInput.send_keys("01.08.2022")
startDateInput.send_keys(Keys.RETURN)
endDateInput.clear()
endDateInput.send_keys("13.08.2022")
startDateInput.send_keys(Keys.RETURN)

selectElement = browser.find_element(By.ID,'typ_1_1_standort')
selectObject = Select(selectElement)
allOptions = selectObject.options
for e in allOptions:
  print(e.text)

print(len(allOptions))

if len(allOptions) > 1:
  sys.exit("Strandkörbe verfügbar")

