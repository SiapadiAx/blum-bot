# blum-bot
blum bot auto claim/tap https://t.me/BlumCryptoBot

<img width="607" alt="2024-06-11 22_07_09-tokens txt - blum-bot - Visual Studio Code" src="https://github.com/maldiharyojudanto/blum-bot/assets/76139419/aea9cc1e-3b00-4791-a092-999048bb2963">

## Features
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

## How to get token?
1. Open telegram web/desktop
2. Go to Settings - Advanced - Experimental settings - Enable webview inspecting
3. Open bot
4. Press F12 or right click then select inspect element
5. Go to Network tab - Fetch/XHR - Header - Authorization (copy token after Baarer/start with eyJxxx)
6. Separate tokens with newline (for multiple account)
