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

async def createToken(session, query):
    url = "https://gateway.blum.codes/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"

    payload = "{\"query\":\"%s\",\"variables\":{}}" % query

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
            resp = await session.post(url, headers=headers, data=payload)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to createToken, HTTP error, try again ... {e}")
            continue
    

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
    url = "https://gateway.blum.codes/v1/friends?pageSize=1000"

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
            elif response.status_code == 412: # Task is not done"
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

async def playGame(session, token):
    url = "https://game-domain.blum.codes/api/v1/game/play"

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
            elif response.status_code == 400:
                # print(response.json())
                return response.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to playGame, HTTP error, try again ...  {e}")
            continue

async def claimGame(session, token, gameid):
    url = "https://game-domain.blum.codes/api/v1/game/claim"

    payload = json.dumps({
        "gameId": f"{gameid}",
        "points": int(os.getenv("GAME_POINT"))
    })

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
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
            response = await session.post(url, headers=headers, data=payload)

            if response.status_code == 200:
                # print(response.json())
                break
            if response.status_code == 400:
                continue
            if response.status_code == 404:
                break
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to claimGame, HTTP error, try again ...  {e}")
            continue

# function to print out the all information
def statusPrint(username, cekin_status, balance, farm_status, tasks_status, reff_status, rline, statplay):
    if rline == True: # will activated the (end="\n")
        print(f"[{username}] | Daily check-in : {cekin_status} | Balance : {Fore.GREEN}{balance['availableBalance']}{Style.RESET_ALL} | Status : {farm_status} | Tasks : {tasks_status} | Auto play game : {statplay} | Refferals : {reff_status}", end='\n')
    else:
        print(f"[{username}] | Daily check-in : {cekin_status} | Balance : {Fore.GREEN}{balance['availableBalance']}{Style.RESET_ALL} | Status : {farm_status} | Tasks : {tasks_status} | Auto play game : {statplay} | Refferals : {reff_status}")

# this coroutine will run the others courutine and the main of program
async def runAll(username, token):

    # create async session with httpx
    async with httpx.AsyncClient(timeout=30) as session:

        # Run all GET and await
        timenow = await getTimeNow(session, token)
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
            cekin_status = f"{Fore.GREEN}Done{Style.RESET_ALL}"

        tasks_status = "-"
        for key in task_list:
            if key['type'] == "SOCIAL_SUBSCRIPTION" and key['status'] == "NOT_STARTED":
                await startClaimTasks(session, key['id'], token)
                tasks_status = f"{Fore.YELLOW}Tasks started{Style.RESET_ALL}"
            else:
                continue

        for key in task_list:
            if key['status'] == "READY_FOR_CLAIM" or key['status'] == "DONE" and key['title'] != "Subscribe to Blum Telegram":
                await clickClaimTasks(session, key['id'], token)
                tasks_status = f"{Fore.YELLOW}Available to claim{Style.RESET_ALL}"
            else:
                continue
        
        for i in task_list:
            if i['kind'] == "QUEST":
                for k in i['subTasks']:
                    # print(k['id'])
                    await startClaimTasks(session, k['id'], token)
                
                for k in i['subTasks']:
                    # print(k['id'])
                    await clickClaimTasks(session, k['id'], token)

        jumlah_task_selesai = 0
        for key in task_list:
            if key['status'] == "FINISHED":
                jumlah_task_selesai = jumlah_task_selesai + 1
        
        if jumlah_task_selesai > 10:
            tasks_status = f"{Fore.GREEN}More than 10 completed{Style.RESET_ALL}"
        else:
            tasks_status = f"{Fore.YELLOW}Less than 10{Style.RESET_ALL}"
        
        reff_status = "-"
        if reff_list['friends'] != []:
            if reff_bal['canClaim'] == True:
                reff_status = f"{Fore.YELLOW}Claiming{Style.RESET_ALL}"
                await claimReffBal(session, token)
            else:
                reff_status = f"{Fore.GREEN}{len(reff_list['friends'])}{Style.RESET_ALL}"
        else:
            reff_status = 0

        if os.getenv("AUTO_PLAY_GAME") == "true":
            statplay = "On"
            playgame = await playGame(session, token)
            if 'gameId' in playgame:
                idgame = playgame['gameId']
                await claimGame(session, token, idgame)
            else:
                pass

        if 'farming' in balance:
            if timenow['now'] > balance['farming']['endTime']:
                statusPrint(username, cekin_status, balance, f"{Fore.YELLOW}Available to claim{Style.RESET_ALL}", tasks_status, reff_status, True, statplay)
                await claimBalance(session, token)
            else:
                statusPrint(username, cekin_status, balance, f"{Fore.YELLOW}Farming{Style.RESET_ALL}", tasks_status, reff_status, False, statplay)
        else:
            statusPrint(username, cekin_status, balance, f"{Fore.YELLOW}Farming started{Style.RESET_ALL}", tasks_status, reff_status, False, statplay)
            await startFarming(session, token)

# coroutine to run the refresh token
async def runRefresh(tokens, token, username, id):
    async with httpx.AsyncClient(timeout=30) as session:
        token_refresh = await refreshToken(session, token)
        tokenauth = token_refresh['access']
        tokenref = token_refresh['refresh']

        # To overwrite the token for each line
        tokens[id] = f"{username}|{tokenauth}|{tokenref}\n"
        with open('tokens.txt', 'w') as tf:
            tf.writelines(tokens)


async def runCreateToken():
    try:
        with open('query.txt', 'r') as qf:
            querys = qf.readlines()
            async with httpx.AsyncClient(timeout=30) as session:
                for i in range(len(querys)):
                    # print(querys[i].strip())
                    query = querys[i].strip()

                    token = await createToken(session, query)
                    userid = token['token']['user']['username']
                    token_acc = token['token']['access']
                    token_refresh = token['token']['refresh']

                    querys[i] = f"{userid}|{token_acc}|{token_refresh}\n"

                    with open('tokens.txt', 'w+') as tf:
                        tf.writelines(querys)
        print("Create token success!")
    except FileNotFoundError:
        qf = open('query.txt', 'w')
        print("Fill the query.txt first!")
        qf.write("query1\nquery2\netc...")
        qf.close()
        exit()

# coroutine main
async def main():
    os.system("cls" if os.name == "nt" else "clear") # remove the printed 

    print("Create token started")
    await runCreateToken()
    sekarang = time.time()
    nanti = time.time() + int(os.getenv("REFRESH_TOKEN"))

    while sekarang < nanti:
        print("""
 _     _                   _           _   
| |__ | |_   _ _ __ ___   | |__   ___ | |_ 
| '_ \| | | | | '_ ` _ \  | '_ \ / _ \| __|
| |_) | | |_| | | | | | | | |_) | (_) | |_ 
|_.__/|_|\__,_|_| |_| |_| |_.__/ \___/ \__|
        """)
        try:
            start = time.time()
            schedules = []

            # open tokens.txt
            with open('tokens.txt', 'r') as tf:
                tokens = tf.readlines() 
                for i in range(len(tokens)):
                    token = tokens[i].strip()
                    splittoken = token.split("|")
                    # print(splittoken)
                    tokenauth = splittoken[1]
                    username = splittoken[0]
                    schedules.append(asyncio.create_task(runAll(username, tokenauth)))
            
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
                        splittoken = token.split("|")
                        # print(splittoken)
                        tokenref = splittoken[2]
                        usernamenya = splittoken[0]
                        schedules_refresh.append(asyncio.create_task(runRefresh(tokens, tokenref, usernamenya, i)))
                # gather to run concurently
                await asyncio.gather(*schedules_refresh) # BOOOMMMM TO RUN
                time.sleep(5)
                nanti = time.time() + int(os.getenv("REFRESH_TOKEN"))
                
            os.system("cls" if os.name == "nt" else "clear") # remove the printed 
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