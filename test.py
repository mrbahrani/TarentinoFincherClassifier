from selenium import webdriver
from time import sleep
# decision maker
def decide(money):
    if money <= 500:
        return "quit", "quit"
    elif 500 <= money < 5000:
        return "50", "2"
    elif 5000 <= money < 10000:
        return "50", "3"
    elif 10000 <= money < 15000:
        return "100", "1.8"
    elif 15000 <= money < 20000:
        return "200", "1.8"
    elif 20000 <= money < 30000:
        return "300", "1.8"
    elif 30000 <= money < 40000:
        return "300", "3"
    elif 40000 <= money < 50000:
        return "400", "3"
    elif 50000 <= money < 70000:

        return "400", "4"
    elif 70000 <= money < 90000:
        return "500", "5"
    elif 90000 <= money < 100000:
        return "500", "6"
    elif 100000 <= money:
        return "500", "7"
# initialize
driver = webdriver.Firefox()
driver.get("http://b45tttonline.com/games/crash/index")
mail = driver.find_element_by_id("mail")
mail.send_keys("alibetbi@yahoo.com")


passi = driver.find_element_by_id("pass")
passi.send_keys("12345a")
but = driver.find_elements_by_class_name("action-button.form-button")
driver.implicitly_wait(5)
but[0].click()
driver.implicitly_wait(100)
shru = driver.find_element_by_id("play_button")
driver.implicitly_wait(10000)
sleep(10)
shru.click()
sleep(10)
jackpot_chance = 8
while True:
    try:
        # money_raw = driver.find_element_by_class_name("top_left_chips.chips-amount")
        # m = int(money_raw.get_attribute("innerHTML").split()[0].replace(",", ""))
        # amount_val, zarib_val = decide(m)
        # if jackpot_chance == 9 : zarib_val= str(int(zarib_val)*2.5)
        #
        # if amount_val == "quit":
        #     break
        amount = driver.find_elements_by_class_name("game-amount")
        amount[0].clear()
        amount[0].send_keys("3000")
        ##
        zarib = driver.find_elements_by_class_name("cashout-amount")
        zarib[0].clear()
        zarib[0].send_keys("1.03")

        shart = driver.find_elements_by_class_name("place-bet.lang_66")
        shart[0].click()
        sleep(5)
        # jackpot_chance += 1
        # jackpot_chance %= 10
        # print("zarib", zarib_val)
        # print("jackpot_chance", jackpot_chance)
    except:
        pass
driver.close()