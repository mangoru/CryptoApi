import requests
import os
import time
from pydub import AudioSegment
from pydub.playback import play

# This data was produced from the CoinDesk Bitcoin Price Index (USD).
# Non-USD currency data converted using hourly conversion rate from openexchangerates.org
print('This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org')

LIMIT = 60.0e+3 # limite para que suene la alarma
SONG = "ultra-mega-stonks.mp3" # cancion de la alarma
BASE = "PEN" # codigo de la moneda de tu pais
FILE = f'data_{BASE}.csv' # nombre del archivo

STONKS = AudioSegment.from_file(SONG, format="mp3")
ULR = f'https://api.coindesk.com/v1/bpi/currentprice/{BASE}.json' # CoinDesk API URL
COLUMNS = f'\nUSD, {BASE}, DATE\n'


if not os.path.exists(FILE):
    with open(FILE,'w+') as f:
        f.write(COLUMNS)
        print(COLUMNS)

while True:
    r = requests.get(ULR)
    data = r.json()
    with open(FILE,'a+') as f:
        cad = f'{data["bpi"]["USD"]["rate_float"]}, {data["bpi"][BASE]["rate_float"]},"{data["time"]["updated"]}"\n'
        f.write(cad)
        print(cad)
        if data["bpi"]["USD"]["rate_float"] >= LIMIT:
            play(STONKS)
            
    time.sleep(60)