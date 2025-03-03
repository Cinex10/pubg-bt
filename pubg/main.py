
from src.core import process
from src import api

import time
import requests
import sys
import configparser
import os




def main() -> None:
    # get arguments list
    #arguments = sys.argv[1:]
    # get merchant  name
    #merchant=arguments[0]
    #config = configparser.ConfigParser()
    #path = os.getcwd()
    # read config file
    #config.read( f"{path}\\config.ini")
    #base_url = config.get(merchant, 'base_url')

    #headers={"Content-Type":"application/json", "Accept":"application/json","X-Authorization": "HnweAEO5T7SArZCiy5SjzOx9cZ96qGEejaiIkvyZLZW1PrBZX64ofs5lO6s6UCmK","X-Device":"hetzner-server-1-new-code-1"}
    #r = requests.get(url=base_url+"/api/v1/pubg/retry/99001", headers=headers)
    #print(r.json())
    #if(r.json()['success'] == False):
        #exit()

    email_address='nijoj40533@saierw.com'#r.json()['email']
    password='mMzZ8H922M6xL82c'#r.json()['password']
    player_id=5205701849#r.json()['player_id']
    redeem_code='VVVcek832M285db259'#r.json()['code']
    code_id = 0#r.json()['code_id']

    start_time = time.ctime()

    try:
        result = process(
            email_address=email_address,
            password=password,
            player_id=player_id,
            redeem_code=redeem_code
        )
        print("SUCCESS: ", result)
        #api.handle_success(success_message=result,code=redeem_code,code_id=code_id,email=email_address,config=config,base_url=base_url)
    except Exception as error:
        print("ERROR: ", str(error))
        #api.handle_failure(error_message=str(error).strip(),code=redeem_code,code_id=code_id,email=email_address,config=config,base_url=base_url)


    print(start_time)
    print(time.ctime())


if __name__=="__main__":
    main()

