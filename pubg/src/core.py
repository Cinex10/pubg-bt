
from src.browser import Browser
import time

def process(email_address, password, player_id, redeem_code):

    browser = Browser()

    browser.visit_page()
    time.sleep(3)
    try:
        #
        #browser.implicitly_wait(10)
        browser.sign_in(email_address=email_address, password=password)
    except:
        raise Exception("Failed to sign in")

    try:
        browser.switch_player_id(player_id=player_id)
    except Exception as err:
        raise Exception(str(err))

    try:
        redeem_status = browser.redeem_code(redeem_code=redeem_code)
        time.sleep(5)
        # redeem_status = browser.redeem_code2(redeem_code=redeem_code)
        if redeem_status==True:
            return 'Successfully redeemed code'
        else:

            raise Exception(redeem_status)
    except Exception as err:
        raise Exception(str(err))


