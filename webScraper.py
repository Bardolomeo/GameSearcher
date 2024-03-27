from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

green = "\033[32m"
cyan = "\033[36m"
white = "\033[37m"
yellow = "\033[33m"
purple = "\033[35m"
red = "\033[31m"

print_flag = 0
search_data = {"cost" : "", "game" : "", "deep" : 50}
def selenium_ini() -> webdriver.Chrome:
    driver_path = "./chromedriver.exe"
    browser_path = "./Brave/brave.exe"
    option = webdriver.ChromeOptions()
    option.binary_location = browser_path
    option.add_argument("--incognito")
    option.add_argument("--disable-logging")
    option.add_argument("--headless")
    service = webdriver.ChromeService(driver_path)
    browser = webdriver.Chrome(service=service, options=option)
    return browser
    

def search_game_normal(names, name, prices):
    if int(name.text.lower().find(search_data["game"].lower())) != -1 or search_data["game"] == "":
            print(cyan + name.text + white + "    " + green + prices[names.index(name)].text + white)
            name_formatted = name.text.replace(' ', '-').lower()
            name_formatted_nospecial = ''.join(e for e in name_formatted if (e.isalnum() or e == '-'))
            buy_game = purple + '(' + red + 'https://www.allkeyshop.com/blog/buy-'+ name_formatted_nospecial + '-cd-key-compare-prices/'+ purple + ')' + white
            print(buy_game)
            global print_flag
            print_flag = 1
            sleep(0.5)


def print_start():
    print(green + "###############################################################")
    print("#                                                             #")
    print("#  "+ white +"🎮 GameSearcher🎮"+ green +"                                          #")
    print("#                                                             #")
    print("#  "+white+"Find your favorite games within your budget effortlessly."+green+"  #")
    print("#  "+white+"Just input the game's name and your price range."+green+"           #")
    print("#                                                             #")
    print("#                                                             #")
    print("#  "+white+">" +yellow+" Deep"+white+" = how many page will the program scrap"+green+"              #")
    print("#                                                             #")
    print("#  "+white+"> '-1' as "+yellow+"Price Range"+white+" = Search without looking at prices"+green+"   #")
    print("#                                                             #")
    print("#  "+white+"> No "+yellow+"Game Name"+white+" = lists all games within that price range"+green+"   #")
    print("#                                                             #")
    print("#  "+white+"> Type 'free' in "+yellow+"Price Range"+white+" if you want to check that"+green+"     #")
    print("#                                                             #")
    print("#  "+white+"> The program will search for a match of "+yellow+"Game Name         "+green+"#\n#"+ white+"    even if only partial"+green+"                                     #")
    print("#                                                             #")
    print("###############################################################")
    print(white)
    sleep(1)

def scrape(browser):
    for i in range(1, 50):
        sleep(0.01)
        url = "https://www.allkeyshop.com/blog/catalogue/category-pc-games-all/max-price-" + search_data["cost"] + '/' + 'page-' + str(i) + '/'
        browser.get(url)
        prices = browser.find_elements(By.CLASS_NAME, "search-results-row-price")
        names = browser.find_elements(By.CLASS_NAME, "search-results-row-game-title")
        for name in names:
                search_game_normal(names, name, prices)
    if print_flag == 0:
        print(yellow + "\nNo results found :(\n" + white)
                

browser = selenium_ini()
print_start()
while search_data["cost"].isdigit() == False:
    search_data["cost"] = input("\033[33mPrice Range: \033[37m")
    if search_data["cost"] == "free":
        search_data["cost"] = "0"
    if search_data["cost"] == "-1":
        search_data["cost"] = "1000"

search_data["game"] = input("\033[33mGame Name: \033[37m")
tmp_deep = "null"
while ((tmp_deep.isdigit() == False or int(tmp_deep) > 501) and tmp_deep != ""):
    tmp_deep = input("\033[33mDeep (default 50): \033[37m")
if tmp_deep == "":
    tmp_deep = "50"
search_data["deep"] = int(tmp_deep)
scrape(browser)