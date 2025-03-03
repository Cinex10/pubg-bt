import requests


headers={"Content-Type":"application/json", "Accept":"application/json","X-Authorization": "HnweAEO5T7SArZCiy5SjzOx9cZ96qGEejaiIkvyZLZW1PrBZX64ofs5lO6s6UCmK","X-Device":"hetzner-server-1-new-code-1"}


def handle_success(success_message: str,code:str,code_id:int,email:str,config,base_url) -> None:
    requests.post(url=base_url+"/api/v1/pubg/redeem",json={"code":code,"code_id": code_id, "email": email, "status": "redeemed"}, headers=headers)
    print("making success api call")
def handle_failure(error_message: str,code:str,code_id: int,email:str,config,base_url) -> None:

    if error_message=='Invalid Player ID':
        requests.post(url=base_url+"/api/v1/pubg/redeem",json={"code":code,"code_id": code_id, "email": email, "status": "open_to_request"}, headers=headers)
        invalid_player_id(error_message)
    elif error_message=='Redemption code is redeemed by someone else':
        requests.post(url=base_url+"/api/v1/pubg/convert-to-manual",json={"code":code,"code_id": code_id, "note": "Code is already redeemed"}, headers=headers)
        code_redeemed_by_someone_else(error_message)
    elif 'Redeem code is already used' in error_message or 'You have already redeemed' in error_message or 'This redemption code has already been used' in error_message:
        requests.post(url=base_url+"/api/v1/pubg/redeem",json={"code":code,"code_id": code_id, "email": email, "status": "redeemed"}, headers=headers)
        already_redeemed_by_user(error_message)
    else:
        requests.post(url=base_url+"/api/v1/pubg/redeem",json={"code":code,"code_id": code_id, "email": email, "status": "open_to_request"}, headers=headers)
        print('open to request api call')
        unknown_error(error_message)



def invalid_player_id(error_message: str) -> None:
    # implemen api logic
    print('making error api call:  api.invalid_player_id')

def code_redeemed_by_someone_else(error_message: str) -> None:
    # implemen api logic
    print('making error api call: api.code_redeemed_by_someone_else')

def already_redeemed_by_user(error_message: str) -> None:
    # implemen api logic
    print('making error api call: api.already_redeemed_by_user')

def unknown_error(error_message: str) -> None:
    # implemen api logic
    print('making error api call: "unknown error"')
    print("error: ",str(error_message))
