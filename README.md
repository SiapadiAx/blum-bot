# blum-bot
blum bot auto claim/tap multiple account https://t.me/BlumCryptoBot

<img width="607" alt="2024-06-11 22_07_09-tokens txt - blum-bot - Visual Studio Code" src="https://github.com/maldiharyojudanto/blum-bot/assets/76139419/aea9cc1e-3b00-4791-a092-999048bb2963">

## Features
- Auto create token
- Auto daily check-in
- Auto start/claim farming
- Auto complete tasks
- Auto claim refferal balance
- Auto refresh token

## Requirement
- Python 3.11

## How to run
1. Clone/download this repository
2. > pip install -r requirements.txt
3. > python main.py

## How to get query_id?
1. Open telegram web/desktop
2. Go to Settings - Advanced - Experimental settings - Enable webview inspecting
3. Open bot
4. Press F12 or right click then select inspect element
5. Go to Application tab - Session storage - Select blum - Select __telegram__initParams (copy value start with ```query_id=```)
6. Separate query_id with newline (for multiple account)
