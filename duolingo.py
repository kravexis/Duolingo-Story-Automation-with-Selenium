from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

# ----------------------------------
# Settings and Drivers
# ----------------------------------

driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)
wait_5 = WebDriverWait(driver, 5)
click = EC.element_to_be_clickable

# ----------------------------------
# Opening on the Website
# ----------------------------------

driver.get('Link to Unit 41, Level 4, Story: Lucy and the Dinosaurs')
sleep(1)


# ----------------------------------
# Useful Functions
# ----------------------------------

def login(driver, email, senha):
    email_input = wait.until(click((By.XPATH,"//input[@data-test='email-input']")))
    email_input.click()
    email_input.send_keys(email)

    key_input = wait.until(click((By.XPATH,"//input[@data-test='password-input']")))
    key_input.click()
    key_input.send_keys(senha)

    enter_btn = wait.until(click((By.XPATH,"//button[@class='_3fmUm _1rcV8 _1VYyp _1ursp _7jW2t _1QN-w']")))
    enter_btn.click()
    sleep(3.5)
    
def start(driver):
    start_btn = wait.until(click((By.XPATH,"//button[@data-test='story-start']")))
    start_btn.click()
    
def proceed(driver):
    first_btn = wait.until(click((By.XPATH,"//button[@data-test='stories-player-continue']")))
    first_btn.click() 
    
def proceeds(driver, many):
    for i in range(0, many):
        proceed(driver)
        
def choose_options(driver):
    for i in range(3):
        try:
            btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"(//button[@data-test='stories-choice'])[{i+1}]"))
                )
            btn.click()
        except Exception:
             continue

def history_end(driver, wait_time=2):
    while True:
        try:
            proceed_btn = wait_5.until(click((By.XPATH,"//button[@data-test='stories-player-continue']")))
            proceed_btn.click()
        except TimeoutException:
            done_button = wait_5.until(click((By.XPATH,"//button[@data-test='stories-player-done']")))
            done_button.click()
            sleep(1)
            break
        
def tap_pt_en_buttons(driver):
    buttons = [
    ('olá', 'hello', ''),
    ('redação', 'report', ''),
    ('livros', 'books', ''),
    ('dinossauros', 'dinosaurs', ''),
    ('escola', 'school', ''),
    ('velha', 'old', ''),
    ('por que', 'why', ''),
    ('lê', 'read', ''),
    ('falar', 'talk', ' to'),
    ('abre', 'opens', ''),
    ('porta', 'door', ''),
    ('escritora', 'writer', ''),
    ('ótima', 'great', ''),
    ('pesquisa', 'research', ''),
    ('muito', 'very', '')
 ]
    for pt, en, to in buttons:
        try:
            pt_btn = driver.find_elements(By.XPATH,f"//button[@data-test='{pt}-challenge-tap-token']")
            
            if not pt_btn:
                continue
            
            pt_btn[0].click()
            sleep(.25)
            
            en_btn = driver.find_element(By.XPATH,f"//button[@data-test='{en}-challenge-tap-token{to}']")
            en_btn.click()
            sleep(0.2)
            
            
        except Exception as e:
            print(f"Erro em {pt}/{en}: {e}")
            continue

# ----------------------------------
# Login
# ----------------------------------

login(driver, 'your e-mail', 'your key')


# ----------------------------------
# Doing the Mission
# ----------------------------------


proceeds(driver, 6)
choose_options(driver)
proceed(driver)

# ----------------------------------
# Fixed Buttons
# ----------------------------------

my_btn = wait.until(click((By.XPATH,"//button[@data-test='my-challenge-tap-token']")))
dyr_btn = wait.until(click((By.XPATH,"//button[@data-test='Do read-challenge-tap-token you']")))
blog_btn = wait.until(click((By.XPATH,"//button[@data-test='blog-challenge-tap-token']")))

dyr_btn.click()
my_btn.click()
blog_btn.click()


proceeds(driver, 4)


research_btn = wait.until(click((By.XPATH,"//button[@data-test='research-challenge-tap-token']")))
research_btn.click()


proceed(driver)
choose_options(driver)
proceeds(driver, 7)
choose_options(driver)
proceed(driver)


sleep(1.3)

tap_pt_en_buttons(driver)
        
history_end(driver)

