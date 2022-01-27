from argparse import ArgumentParser
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")

def get_followers(follower_url):
    driver.get(follower_url)

    buttons = driver.find_elements_by_xpath("//input[@value='Unfollow']")
    for btn in buttons:
        btn.click()

def do_login(user_name, pw):
    driver.get('https://github.com/login')

    # Click the sign in button
    driver.find_element(By.XPATH, "//input[@value='Sign in']").click()

    # Entering username
    driver.find_element(By.ID, "login_field").send_keys(user_name)

    # Entering password
    driver.find_element(By.ID, "password").send_keys(pw + '\n')

    print("---Login successfully---")


def main():

    parser = ArgumentParser()
    parser.add_argument("username", nargs="?", default="", help='Your Github username')
    parser.add_argument('password', nargs="?", help='The password of your Github account for login', default="")
    parser.add_argument('maxpage', nargs="?", help='Github page number', default='')
    args = parser.parse_args()

    do_login(args.username, args.password)

    for i in range(int(args.maxpage)):
        following_url = f'https://github.com/{args.username}?page={i + 1}&tab=following'
        get_followers(following_url)


if __name__ == '__main__':
    main()