import pyotp
import json
import time



def read_json():
    with open('bitskins.json', 'r') as file_json:
        bitskins_2FA = json.load(file_json)
        secret_token = str(bitskins_2FA['bitskins'])
    return secret_token


def two_factor_aunteficator_code():
    while True:
        try:
            secret_token = read_json()
            right_now_my_two_factor_aunteficator_code = str(secret_token)
            if right_now_my_two_factor_aunteficator_code == str(secret_token):
                right_now_my_token = pyotp.TOTP(right_now_my_two_factor_aunteficator_code)
                print(f'You are 2FA --> {right_now_my_token.now()} , {time.ctime()}', time.sleep(5))
                return two_factor_aunteficator_code()
        except KeyboardInterrupt:
            print('STOP program')


two_factor_aunteficator_code()