# Logo
logo = """
\033[1;32m____  _____       _       ______   _____  ____    ____     ______   
\033[1;32m|_   \|_   _|     / \     |_   _ `.|_   _||_   \  /   _|  .' ___  |  
  \033[1;33m|   \ | |      / _ \      | | `. \ | |    |   \/   |   / .'   \_|  
  \033[1;32m| |\ \| |     / ___ \     | |  | | | |    | |\  /| |   | |    ___  
 \033[1;33m_| |_\   |_  _/ /   \ \_  _| |_.' /_| |_  _| |_\/_| |_  \ `.___]  | 
\033[1;32m|_____|\____||____| |____||______.'|_____||_____||_____|  `._____.'                                                

╭───────────────────────── < ~ COUNTRY ~  > ─────────────────────────╮
│ 【•】 YOUR COUNTRY  ➤ INDIA                                        │
│ 【•】 YOUR REGION   ➤ BIHAR                                        │
│ 【•】 YOUR CITY     ➤ PATNA                                        │
╰────────────────────────────< ~ COUNTRY ~  >────────────────────────╯
"""
print(logo)

import os
import random
import time
import requests

# Facebook Graph API endpoint
thread_id = input("\033[1;32m \033[1;91m\033[1;41m\033[1;33m1NT3R T9RG3T 1D\033[;0m\033[1;91m\033[1;92m\033[38;5;46m =>>")

url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'

# Token file paths
token_file_paths = input("\033[1;32m \033[1;91m\033[1;41m\033[1;33mENT3R T0K3N F1L3 PUT\033[;0m\033[1;91m\033[1;92m\033[38;5;46m =>>").split(',')

# Message file path
message_file_path = input("\033[1;32m \033[1;91m\033[1;41m\033[1;33m3NT3R G9L1 FIL3 PUT\033[;0m\033[1;91m\033[1;92m\033[38;5;46m =>>")

# Haters name
haters_name = input("\033[1;32m \033[1;91m\033[1;41m\033[1;33m3NT3R H9T3R N9M3\033[;0m\033[1;91m\033[1;92m\033[38;5;46m =>>")

# Delay between messages
delay_between_messages = int(input("\033[1;32m \033[1;91m\033[1;41m\033[1;33mENT3R S3COND SPE3D\033[;0m\033[1;91m\033[1;92m\033[38;5;46m =>>"))

# Read tokens from files
access_tokens = []
token_names = []
for token_file_path in token_file_paths:
    with open(token_file_path.strip(), "r") as token_file:
        for i, token in enumerate(token_file.readlines()):
            access_tokens.append(token.strip())
            token_names.append(f"Token {i+1}")

# Read messages from file
messages = []
with open(message_file_path, "r") as message_file:
    messages = message_file.readlines()

def get_account_name(token):
    try:
        response = requests.get(f'https://graph.facebook.com/v15.0/me?access_token={token}')
        data = response.json()
        return data['name']
    except Exception as e:
        return "Unknown"

def send_message(token, message, thread_id, haters_name):
    try:
        message_url = f"{url}"
        message_params = {
            "access_token": token,
            "message": f"{haters_name} {message}"
        }
        message_response = requests.post(message_url, params=message_params)
        if message_response.status_code == 200:
            current_time = time.strftime("%H:%M:%S")
            print(f"""
\033[1;32m
✪✭══════════•『 \033[1;32m \033[1;91m\033[1;41m\032[1;32m𝗬𝗢𝗨𝗥 𝗦𝗠𝗦 𝗦𝗘𝗡𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗨𝗙𝗨𝗟 🎉\033[;0m\033[1;91m\033[1;92m\033[38;5;46m 』•══════════✭✪
""")
            account_name = get_account_name(token)           
            print(f"\033[1;32m[+] ✪✭═══════•『 \033[1;32m\033[1;91m\033[1;41m\033[1;32m𝗬𝗢𝗨𝗥 𝗦𝗠𝗦 𝗦𝗘𝗡𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗨𝗙𝗨𝗟 🎉\033[;0m\033[1;91m\033[1;92m\033[38;5;46m 』•═══════✭✪ =>> Thread ID: {thread_id} => Token: {token_names[access_tokens.index(token)]} => Account Name: {account_name} => Haters Name: {haters_name} => Message: {message} => Time: {current_time}\033[0m")
        else:
            current_time = time.strftime("%H:%M:%S")
            print(f"""
 \033[1;32m 
✪✭══════════•『 \033[1;32m \033[1;91m\033[1;41m\032[1;32m𝗬𝗢𝗨𝗥 𝗦𝗠𝗦 𝗦𝗘𝗡𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗨𝗙𝗨𝗟 🎉\033[;0m\033[1;91m\033[1;92m\033[38;5;46m 』•══════════✭✪
""")
            print(f"\033[1;32mM3SS4G3 F9IL3D H0 GYA HAI => Thread ID: {thread_id} =>Token: {token_names[access_tokens.index(token)]} => Haters Name: {haters_name} => Message: {message} => Time: {current_time}\033[0m")
    except Exception as e:
        print(str(e))

def process_messages_thread():
    try:
        while True:
            random_token = random.choice(access_tokens)
            random_message = random.choice(messages).strip()
            send_message(random_token, random_message, thread_id, haters_name)
            time.sleep(delay_between_messages)
    except Exception as e:
        print(str(e))

process_messages_thread()
