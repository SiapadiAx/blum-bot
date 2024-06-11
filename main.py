import httpx
import asyncio
import time
from colorama import Fore, Style, init
import os
import json
import datetime
from dotenv import load_dotenv

init()
load_dotenv() 

# coroutine to get time at the moment (UNIX timestamp)
async def getTimeNow(session, token):
    url = "https://game-domain.blum.codes/api/v1/time/now"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            response = await session.get(url, headers=headers)

            if response.status_code == 200:
                # print(response.json())
                return response.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getTime, HTTP error, try again ... {e}")
            continue

# coroutine to get the username
async def getUsername(session, token):
    url = "https://gateway.blum.codes/v1/user/me"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            response = await session.get(url, headers=headers)

            if response.status_code == 200:
                # print(response.json())
                return response.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getUsername, HTTP error, try again ... {e}")
            continue

# coroutine for get the balance and farming status 
async def getBalance(session, token):
    url = "https://game-domain.blum.codes/api/v1/user/balance"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            response = await session.get(url, headers=headers)

            if response.status_code == 200:
                # print(response.json())
                return response.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getBalance, HTTP error, try again ... {e}")
            continue

# this to daily check-in if available then POST (daily)
async def dailyCheck(session, token, method):
    url = "https://game-domain.blum.codes/api/v1/daily-reward?offset=-420"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            if method == "GET":
                response = await session.get(url, headers=headers)

                if response.status_code == 200:
                    # print(response.json())
                    return response.json()
                else:
                    return {}
            else:
                response = await session.post(url, headers=headers)
                if response.status_code == 200:
                    # print(response.json())
                    break
                else:
                    continue
        except httpx.HTTPError as e:
            print(f"Error to dailyCheck, HTTP error, try again ... {e}")
            continue

# coroutine to check tasks (return the list of task and the status)
async def getTasks(session, token):
    url = "https://game-domain.blum.codes/api/v1/tasks"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            response = await session.get(url, headers=headers)

            if response.status_code == 200:
                # print(response.json())
                return response.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getTasks, HTTP error, try again ... {e}")
            continue

# coroutine to check the list of refferals
async def getReffList(session, token):
    url = "https://gateway.blum.codes/v1/friends"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            response = await session.get(url, headers=headers)

            if response.status_code == 200:
                # print(response.json())
                return response.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getReffList, HTTP error, try again ... {e}")
            continue

# coroutine to check the balance available in the refferal page
async def getReffBal(session, token):
    url = "https://gateway.blum.codes/v1/friends/balance"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            response = await session.get(url, headers=headers)

            if response.status_code == 200:
                # print(response.json())
                return response.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getReffBal, HTTP error, try again ... {e}")
            continue

# coroutine to start the farming (this coroutine will be excute if the button start available)
async def startFarming(session, token):
    url = "https://game-domain.blum.codes/api/v1/farming/start"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            response = await session.post(url, headers=headers)

            if response.status_code == 200:
                # print(response.json())
                return response.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to startFarming, HTTP error, try again ... {e}")
            continue

# coroutine to claim the balance if ready
async def claimBalance(session, token):
    url = "https://game-domain.blum.codes/api/v1/farming/claim"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            response = await session.post(url, headers=headers)

            if response.status_code == 200:
                # print(response.json())
                return response.json()
            elif response.status_code == 425: # to early claim
                # print(response.json()) 
                break
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to claimBalance, HTTP error, try again ... {e}")
            continue

# coroutine to refresh token
async def refreshToken(session, token):
    url = "https://gateway.blum.codes/v1/auth/refresh"

    payload = {
        "refresh": f"{token}"
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            response = await session.post(url, headers=headers, data=json.dumps(payload))

            if response.status_code == 200:
                # print(response.json())
                return response.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to refreshToken, HTTP error, try again ...  {e}")
            continue

# coroutine to start the task if statement have been meet
async def startClaimTasks(session, id, token):
    url = f"https://game-domain.blum.codes/api/v1/tasks/{id}/start"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    
    while True:
        try:
            response = await session.post(url, headers=headers)

            if response.status_code == 200:
                # print(response.json())
                return response.json()
            elif response.status_code == 400: # task is already started
                # print(response.json())
                break
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to startClaimTasks, HTTP error, try again ... {e}")
            continue

# coroutine to click claim task if the task have been start/clicked
async def clickClaimTasks(session, id, token):
    url = f"https://game-domain.blum.codes/api/v1/tasks/{id}/claim"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            response = await session.post(url, headers=headers)

            if response.status_code == 200:
                # print(response.json())
                return response.json()
            elif response.status_code == 400: # task is already claimed
                # print(response.json())
                break
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to clickClaimTasks, HTTP error, try again ... {e}")
            continue

# coroutine to claim refferal balance if statement have been meet
async def claimReffBal(session, token):
    url = "https://gateway.blum.codes/v1/friends/claim"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            response = await session.post(url, headers=headers)

            if response.status_code == 200:
                # print(response.json())
                return response.json()
            elif response.status_code == 400: # too early clain
                # print(response.json())
                break
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to claimReffBal, HTTP error, try again ...  {e}")
            continue

# function to print out the all information
def statusPrint(username, cekin_status, balance, farm_status, tasks_status, reff_status, rline):
    if rline == True: # will activated the (end="\n")
        print(f"[{username['username']}] | Daily check-in : {cekin_status} | Balance : {Fore.GREEN}{balance['availableBalance']}{Style.RESET_ALL} | Status : {farm_status} | Tasks : {tasks_status} | Refferals : {reff_status}", end='\n')
    else:
        print(f"[{username['username']}] | Daily check-in : {cekin_status} | Balance : {Fore.GREEN}{balance['availableBalance']}{Style.RESET_ALL} | Status : {farm_status} | Tasks : {tasks_status} | Refferals : {reff_status}")

# this coroutine will run the others courutine and the main of program
async def runAll(token, i):

    # create async session with httpx
    async with httpx.AsyncClient(timeout=60) as session:

        # Run all GET and await
        timenow = await getTimeNow(session, token)
        username = await getUsername(session, token)
        daily = await dailyCheck(session, token, "GET")
        balance = await getBalance(session, token)
        task_list = await getTasks(session, token)
        reff_list = await getReffList(session, token)
        reff_bal = await getReffBal(session, token)
        
        # Run all POST and await
        cekin_status = "-"
        if 'days' in daily:
            cekin_status = f"{Fore.YELLOW}Available to claim{Style.RESET_ALL}"
            await dailyCheck(session, token, "POST")
        else:
            cekin_status = f"{Fore.GREEN}Completed{Style.RESET_ALL}"

        tasks_status = "-"
        for key in task_list:
            if key['type'] == "SOCIAL_SUBSCRIPTION" and key['status'] == "NOT_STARTED":
                await startClaimTasks(session, key['id'], token)
                tasks_status = f"{Fore.YELLOW}Tasks started{Style.RESET_ALL}"
            else:
                continue

        for key in task_list:
            if key['status'] == "DONE" and key['title'] != "Subscribe to Blum Telegram":
                await clickClaimTasks(session, key['id'], token)
                tasks_status = f"{Fore.YELLOW}Available to claim{Style.RESET_ALL}"
            else:
                continue

        jumlah_task_selesai = 0
        for key in task_list:
            if key['status'] == "CLAIMED":
                jumlah_task_selesai = jumlah_task_selesai + 1
        
        if jumlah_task_selesai >= 8:
            tasks_status = f"{Fore.GREEN}All task completed{Style.RESET_ALL}"
        else:
            tasks_status = f"{Fore.YELLOW}Loading{Style.RESET_ALL}"
        
        reff_status = "-"
        if reff_list['friends'] != []:
            if reff_bal['canClaim'] == True:
                reff_status = f"{Fore.YELLOW}Claiming{Style.RESET_ALL}"
                await claimReffBal(session, token)
            else:
                reff_status = f"{Fore.GREEN}{len(reff_list['friends'])}{Style.RESET_ALL}"
        else:
            reff_status = f"{Fore.RED}0{Style.RESET_ALL}"

        if 'farming' in balance:
            if timenow['now'] > balance['farming']['endTime']:
                statusPrint(username, cekin_status, balance, f"{Fore.YELLOW}Available to claim{Style.RESET_ALL}", tasks_status, reff_status, True)
                await claimBalance(session, token)
                statusPrint(username, cekin_status, balance, f"{Fore.GREEN}Claimed{Style.RESET_ALL}", tasks_status, reff_status, False)
            else:
                statusPrint(username, cekin_status, balance, f"{Fore.YELLOW}Farming{Style.RESET_ALL}", tasks_status, reff_status, False)
        else:
            statusPrint(username, cekin_status, balance, f"{Fore.YELLOW}Farming started{Style.RESET_ALL}", tasks_status, reff_status, False)
            await startFarming(session, token)

# coroutine to run the refresh token
async def runRefresh(tokens, token, id):
    async with httpx.AsyncClient(timeout=60) as session:
        token_refresh = await refreshToken(session, token)
        token_new = token_refresh['refresh']

        # To overwrite the token for each line
        tokens[id] = f"{token_new}\n"
        with open('tokens.txt', 'w') as tf:
            tf.writelines(tokens)

# coroutine main
async def main():
    os.system('cls') # remove the printed 

    sekarang = time.time()
    nanti = time.time() + int(os.getenv("REFRESH_TOKEN"))

    while sekarang < nanti:
        print("""
 _     _                                         _          _           _   
| |__ | |_   _ _ __ ___     ___ _ __ _   _ _ __ | |_ ___   | |__   ___ | |_ 
| '_ \| | | | | '_ ` _ \   / __| '__| | | | '_ \| __/ _ \  | '_ \ / _ \| __|
| |_) | | |_| | | | | | | | (__| |  | |_| | |_) | || (_) | | |_) | (_) | |_ 
|_.__/|_|\__,_|_| |_| |_|  \___|_|   \__, | .__/ \__\___/  |_.__/ \___/ \__|
                                     |___/|_|                               
        """)
        try:
            start = time.time()
            schedules = []

            # open tokens.txt
            with open('tokens.txt', 'r') as tf:
                tokens = tf.readlines() 
                for i in range(len(tokens)):
                    token = tokens[i].strip()
                    schedules.append(asyncio.create_task(runAll(token, i)))
            
            # gather to run concurently
            await asyncio.gather(*schedules) # BOOOMMMM TO RUN
            
            # delay before next running
            print("")
            finish = time.time()-start
            #################### Change the delay here ####################
            time_delay = int(os.getenv("REFRESH_CLAIM")) # set to 2 menit or 120 seconds
            refresh_token_at = datetime.datetime.fromtimestamp(nanti).strftime("%H:%M:%S")
            ###############################################################

            while time_delay: 
                mins, secs = divmod(time_delay, 60) 
                timer = '{:02d}:{:02d}'.format(mins, secs) 
                print(f"Execution time : {Fore.YELLOW}{round(finish, 2)}{Style.RESET_ALL} seconds | Refresh tokens after : {Fore.YELLOW}{refresh_token_at}{Style.RESET_ALL} | Refresh after : {Fore.YELLOW}{timer}{Style.RESET_ALL} seconds", end="\r")
                time.sleep(1) 
                time_delay -= 1

            sekarang = time.time()
            if sekarang >= nanti:
                print("\nToken refresh started!")
                schedules_refresh = []
                with open('tokens.txt', 'r') as tf:
                    tokens = tf.readlines() 
                    for i in range(len(tokens)):
                        token = tokens[i].strip()
                        schedules_refresh.append(asyncio.create_task(runRefresh(tokens, token, i)))
                # gather to run concurently
                await asyncio.gather(*schedules_refresh) # BOOOMMMM TO RUN
                time.sleep(3)
                nanti = time.time() + int(os.getenv("REFRESH_TOKEN"))
                
            os.system('cls') # remove the printed 
        except FileNotFoundError:
            tf = open('tokens.txt', 'w')
            tf.write('token1\ntoken2\ntoken3\netc')
            print('Please fill in tokens.txt first!')
            tf.close()
            exit()

if __name__ == "__main__":
    # start = time.time()

    # Set the policy to prevent "Event loop is closed" error on Windows - https://github.com/encode/httpx/issues/914
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

    # end = time.time()
    # print(f"\nExcution time for each request : {end-start}")