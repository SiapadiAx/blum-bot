# blum-bot
blum bot auto claim/tap multiple account https://t.me/BlumCryptoBot

<img width="712" alt="2024-06-16 10_32_21-main py - tapbot - Visual Studio Code" src="https://github.com/maldiharyojudanto/blum-bot/assets/76139419/7fb223ad-e590-458f-bc61-9d20e635ccba">

## Features
- Auto create token (login by query_id)
- Auto daily check-in
- Auto start/claim farming
- Auto complete tasks
- Auto play drop game
- Auto claim refferal balance
- Auto refresh token

## Requirement
- Python 3.8+

## How to run
1. Clone/download this repository
2. > pip install -r requirements.txt
3. > python main.py

## How to get query_id?
1. Open telegram web/desktop
2. Go to Settings - Advanced - Experimental settings - Enable webview inspecting
3. Open bot https://t.me/BlumCryptoBot
4. Press F12 or right click then select inspect element
5. Go to Application tab - Session storage - Select blum - Select '__telegram__initParams' (copy value start with ```query_id=```)
6. Separate query_id with the newline (for multiple account)
