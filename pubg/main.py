
from src.core import process
import time

# TODO: fix confirmation screen


def main() :

    email_address='nijoj40533@saierw.com'
    password='mMzZ8H922M6xL82c'
    player_id=512590258
    redeem_code='6ZgSBMaT2n2a36202f'

    start_time = time.ctime()

    try:
        result = process(
            email_address=email_address,
            password=password,
            player_id=player_id,
            redeem_code=redeem_code
        )
        print("SUCCESS: ", result)
    except Exception as error:
        print("ERROR: ", str(error))
        time.sleep(10000)
    finally:
        time.sleep(10000)


    print(start_time)
    print(time.ctime())


if __name__=="__main__":
    main()

