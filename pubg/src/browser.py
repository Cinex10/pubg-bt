import pdb
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import os


DETECT_PAGE_LOADED_XPATH='//div[@class="Banner_title__dnHBH"]'
SIGN_IN_BUTTON_SELECTOR='div.MobileNav_sign_in__qA2oK'
SIGN_IN_BUTTON_SELECTOR2='div.Button_icon_text__C-ysi'

IFRAME_XPATH='//iframe[contains(@src,"https://www.midasbuy.com/apps/login/home/sa")]'
CONTINUE_SIGN_IN_BUTTON_XPATH='/html/body/div/div[1]/div/div[3]/div[1]/div/div[4]/div'
EMAIL_ADDRESS_FIELD_XPATH='/html/body/div/div[1]/div/div[3]/div[1]/div/div[3]/div/div/div/div[1]/p/input'
PASSWORD_INPUT_FIELD_XPATH='/html/body/div/div[1]/div/div[3]/div[1]/div[1]/div[2]/div[2]/div/input'
FINAL_SIGN_IN_BUTTON_XPATH='/html/body/div/div[1]/div/div[3]/div[1]/div[2]/div'


PLAYER_ID_LOCATION_XPATH='//span[@class="UserTabBox_id__u8hgT"]'
SIGN_IN_BUTTON_XPATH='//div[@class="MobileNav_sign_in__qA2oK"]'
PLAYER_ID_SWITCH_INITIATE_BUTTON_SELECTOR='div.UserTabBox_user_head__65f05 > span'
PLAYER_ID_SWITCH_INITIATE_BUTTON_SELECTOR_NONE = 'div.Banner_user_tab_box__Bp6NY > div > div > div'
PLAYER_ID_INPUT_FIELD_XPATH='/html/body/div[2]/div/div[5]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/input | //*[@id="root"]/div/div[5]/div[2]/div[1]/div/div[3]/div/div/div[1]/input'
PLAYER_ID_SWITCH_OK_BUTTON_SELECTOR='div.BindLoginPop_btn_wrap__eiPwz > div > div > div > div'


REDEEM_CODE_INPUT_BOX_XPATH = '/html/body/div[2]/div/div[7]/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/input'
REDEEM_INITIATE_BUTTON_SELECTOR = '#root > div > div.container_wrap > div.redeem_modules_box.default_box > div > div.RedeemStepBox_step_box__kecmM.RedeemStepBox_redeem_step__Cb6tE > div.RedeemStepBox_mess__6gbK6 > div.RedeemStepBox_btn_wrap__wEKY9 > div > div > div > div'
# /html/body/div[2]/div/div[6]/div[8]/div[2]/p
SUBMIT_REDEEM_CODE_BUTTON_XPATH='/html/body/div[2]/div/div[7]/div[7]/div[2]/div/div[6]/div[1]/div/div/div/div/div'
SUBMIT_REDEEM_CODE_BUTTON_XPATH2='/html/body/div[2]/div/div[7]/div[7]/div[2]/div/div[7]/div[1]/div/div/div/div/div'

REDEEM_ERROR_NOTICE_XPATH='/html/body/div[2]/div/div[7]/div[3]/div/div[2]/div[2]/div[1]/div[3]/div'
REDEEM_SUCCESS_NOTICE_XPATH = '/html/body/div[2]/div/div[3]/div/div[1]/div/div[1]'

from selenium.webdriver.chrome.service import Service

class Browser:
    def __init__(self) -> None:
        options = Options()
        options.page_load_strategy = 'none'
        url = os.getcwd()
        pdb.set_trace()
        service = Service(f"{url}\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=options)
        # self.driver = webdriver.Chrome(options=options)

    def visit_page(self):
        self.driver.get('https://www.midasbuy.com/midasbuy/sa/redeem/pubgm')

    def sign_in(self, email_address, password):
        print('Sign In')
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DETECT_PAGE_LOADED_XPATH))
        )


        status = self.driver.execute_script(f"document.querySelector('{SIGN_IN_BUTTON_SELECTOR}').click();return 'clicked login button'")
        time.sleep(3)

        status = self.driver.execute_script(f"document.querySelector('{SIGN_IN_BUTTON_SELECTOR2}').click();return 'clicked login button'")
        print(status)

        iframe = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, IFRAME_XPATH))
        )


        self.driver.switch_to.frame(iframe)



        email_address_field=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, EMAIL_ADDRESS_FIELD_XPATH))
        )

        email_address_field.send_keys(email_address)
        continue_button = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, CONTINUE_SIGN_IN_BUTTON_XPATH))
                )
        self.driver.execute_script(
            'arguments[0].click()',
            continue_button
        )

        password_input_field = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH,PASSWORD_INPUT_FIELD_XPATH))
        )

        password_input_field.send_keys(password)

        self.driver.find_element(By.XPATH, FINAL_SIGN_IN_BUTTON_XPATH).click()
        print("Arrive ")
        time.sleep(3)
        passkey_button = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div/div[1]'))
                )

        self.driver.execute_script(
                    'arguments[0].click()',
                    passkey_button
                )



    def switch_player_id(self, player_id):
        try:
            player_id = int(player_id)
        except:
            raise Exception("Invalid Player ID")

        self.driver.switch_to.default_content()
        try:
            original_player_id = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, PLAYER_ID_LOCATION_XPATH))).text.strip()
        except:
            original_player_id = 'None'
        if str(player_id) in original_player_id:
            print('Current Player ID is same as provided player ID. Skipping the step.')
            return


        # print('original_player_id: ',original_player_id)
        WebDriverWait(self.driver, 15).until(
            EC.invisibility_of_element((By.XPATH, SIGN_IN_BUTTON_XPATH))
        )


        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DETECT_PAGE_LOADED_XPATH))
        )


        status = self.driver.execute_script(f"document.querySelector('{PLAYER_ID_SWITCH_INITIATE_BUTTON_SELECTOR if original_player_id!='None' else PLAYER_ID_SWITCH_INITIATE_BUTTON_SELECTOR_NONE}').click();return 'clicked player switch button';")

        print(status)

        player_id_input_field = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, PLAYER_ID_INPUT_FIELD_XPATH))
        )
        time.sleep(20)
        player_id_input_field.clear()
        player_id_input_field.send_keys(player_id)

        self.driver.execute_script(f"document.querySelector('{PLAYER_ID_SWITCH_OK_BUTTON_SELECTOR}').click();return 'clicked player switch OK button';")

        time.sleep(2)

        current_player_id = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, PLAYER_ID_LOCATION_XPATH))
        ).text.strip()
        # print('current_player_id: ', current_player_id)
        if original_player_id==current_player_id:
            raise Exception("Invalid Player ID")

        print('Player switch process complete')

    def redeem_code(self, redeem_code):
        time.sleep(2)
        print("redeem_code 1")
        redeem_code_input_box = self.driver.find_element(By.XPATH, REDEEM_CODE_INPUT_BOX_XPATH)
        redeem_code_input_box.clear()
        redeem_code_input_box.send_keys(redeem_code)

        print(1)
        self.driver.execute_script(
            f'document.querySelector("{REDEEM_INITIATE_BUTTON_SELECTOR}").click()'
        )

        time.sleep(5)
        print(2)
        if self.driver.execute_script("return document.readyState") != "complete":
            while True:
                if self.driver.execute_script("return document.readyState") == "complete":
                    break
            self.redeem_code(redeem_code)

        try:
            print(3)
            error_btn = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, REDEEM_ERROR_NOTICE_XPATH))
                    )
            if error_btn:
                return self.driver.find_element(By.XPATH, REDEEM_ERROR_NOTICE_XPATH).text
        except:...

        try:
            print(4)
            submit_redeem_btn = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, SUBMIT_REDEEM_CODE_BUTTON_XPATH))
            )
            self.driver.execute_script(
                'arguments[0].click()',
                submit_redeem_btn
            )

        except:...

        try:
            print(4)
            submit_redeem_btn2 = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, SUBMIT_REDEEM_CODE_BUTTON_XPATH2))
            )
            self.driver.execute_script(
                'arguments[0].click()',
                submit_redeem_btn2
            )

        except:...

        try:
            print(5)
            return self.driver.find_element(By.XPATH, REDEEM_ERROR_NOTICE_XPATH).text
        except:...


        try:
            print(6)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, REDEEM_SUCCESS_NOTICE_XPATH))
            )
            return True
        except:
            try:
                print(7)
                return self.driver.find_element(By.XPATH, REDEEM_ERROR_NOTICE_XPATH).text
            except:...
            return 'Failed to Redeem Code for UNKNOWN REASON'







    # def redeem_code2(self, redeem_code):

    #     print("redeem_code 2")
    #     redeem_code_input_box = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[7]/div[3]/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/input')
    #     redeem_code_input_box.send_keys(redeem_code)


    #     self.driver.execute_script(
    #         f'document.querySelector("{REDEEM_INITIATE_BUTTON_SELECTOR}").click()'
    #     )

    #     time.sleep(3)

    #     try:
    #         error_btn = WebDriverWait(self.driver, 5).until(
    #                     EC.presence_of_element_located((By.XPATH, REDEEM_ERROR_NOTICE_XPATH))
    #                 )
    #         if(error_btn):
    #             return self.driver.find_element(By.XPATH, REDEEM_ERROR_NOTICE_XPATH).text
    #     except:...

    #     try:
    #         submit_redeem_btn = WebDriverWait(self.driver, 15).until(
    #             EC.presence_of_element_located((By.XPATH, SUBMIT_REDEEM_CODE_BUTTON_XPATH))
    #         )
    #         self.driver.execute_script(
    #             'arguments[0].click()',
    #             submit_redeem_btn
    #         )
    #     except:

    #         submit_redeem_btn2 = WebDriverWait(self.driver, 15).until(
    #             EC.presence_of_element_located((By.XPATH, SUBMIT_REDEEM_CODE_BUTTON_XPATH2))
    #         )

    #         self.driver.execute_script(
    #             'arguments[0].click()',
    #             submit_redeem_btn2
    #         )
    #     time.sleep(3)

    #     try:
    #         return self.driver.find_element(By.XPATH, REDEEM_ERROR_NOTICE_XPATH).text
    #     except:...


    #     try:
    #         WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, REDEEM_SUCCESS_NOTICE_XPATH))
    #         )
    #         time.sleep(4)

    #         if  self.driver.find_element(By.XPATH, REDEEM_SUCCESS_NOTICE_XPATH).text == 'REDEEM SUCCESSFUL' or self.driver.find_element(By.XPATH, REDEEM_SUCCESS_NOTICE_XPATH).text == 'تم استبداله بنجاح':
    #             print('Success Inside If')

    #             return True

    #         return False
    #     except:
    #         try:
    #             return self.driver.find_element(By.XPATH, REDEEM_ERROR_NOTICE_XPATH).text
    #         except:...
    #         return 'Failed to Redeem Code for UNKNOWN REASON'

