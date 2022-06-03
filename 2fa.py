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
"""How it work:-
You are 2FA --> 013940 , Sat Jun  4 01:53:48 2022
You are 2FA --> 013940 , Sat Jun  4 01:53:53 2022
You are 2FA --> 013940 , Sat Jun  4 01:53:58 2022
You are 2FA --> 618399 , Sat Jun  4 01:54:03 2022
You are 2FA --> 618399 , Sat Jun  4 01:54:08 2022
You are 2FA --> 618399 , Sat Jun  4 01:54:13 2022
You are 2FA --> 618399 , Sat Jun  4 01:54:18 2022
You are 2FA --> 618399 , Sat Jun  4 01:54:23 2022
You are 2FA --> 618399 , Sat Jun  4 01:54:28 2022
You are 2FA --> 607248 , Sat Jun  4 01:54:33 2022
You are 2FA --> 607248 , Sat Jun  4 01:54:38 2022
You are 2FA --> 607248 , Sat Jun  4 01:54:43 2022
You are 2FA --> 607248 , Sat Jun  4 01:54:48 2022
You are 2FA --> 607248 , Sat Jun  4 01:54:53 2022
You are 2FA --> 607248 , Sat Jun  4 01:54:58 2022
You are 2FA --> 791157 , Sat Jun  4 01:55:03 2022
You are 2FA --> 791157 , Sat Jun  4 01:55:08 2022
You are 2FA --> 791157 , Sat Jun  4 01:55:13 2022
You are 2FA --> 791157 , Sat Jun  4 01:55:18 2022
You are 2FA --> 791157 , Sat Jun  4 01:55:23 2022
"""
