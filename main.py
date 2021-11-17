# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "9.0"
caps["browserName"] = ""
caps["appium:appiumVersion"] = "1.22.0"
caps["appium:deviceName"] = "Samsung Galaxy S9 FHD GoogleAPI Emulator"
caps["appium:deviceOrientation"] = "portrait"
caps["appium:app"] = "storage:filename=Calculator_v8.1 (403424005)_apkpure.com.apk"
caps["appium:appPackage"] = "com.google.android.calculator"
caps["appium:appActivity"] = "com.android.calculator2.Calculator"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 0
caps["appium:connectHardwareKeyboard"] = True

#Acionador do script / código
if __name__ == '__main__':

#    def testar_somar_dois_numeros():
        #Conexão com o Sauce Labs, contém o data center, meu usuário e chave
        driver = webdriver.Remote("https://oauth-felipe.brum-a7d94:bc365b32-525a-409c-834f-f4c948086858@ondemand.us-west-1.saucelabs.com:443/wd/hub", caps)

        resultado_esperado = '13'

        #Realiza a conta automaticamente (Operações previamente realizadas de forma manual)
        botao_8 = driver.find_element_by_id("com.google.android.calculator:id/digit_8")
        botao_8.click()
        botao_somar = driver.find_element_by_accessibility_id("plus")
        botao_somar.click()
        botao_5 = driver.find_element_by_id("com.google.android.calculator:id/digit_5")
        botao_5.click()
        botao_igual = driver.find_element_by_accessibility_id("equals")
        botao_igual.click()
        resultado_final = driver.find_element_by_id("com.google.android.calculator:id/result_final")
        print(f'resultado final = {resultado_final.text} \n resultado esperado = {resultado_esperado}')

        assert resultado_final.text == resultado_esperado

        driver.quit()