from urllib.request import urlopen
from json import loads
from datetime import datetime
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = urlopen("https://api.forecast.io/forecast/<your api key here>/37.8267,-122.423", context=ctx)
fc = url.read().decode('utf-8')
url.close()
jfc = loads(fc)

for idx in range(len(jfc["hourly"]["data"])):
    if ( jfc["hourly"]["data"][idx]["precipProbability"] > 0 ):
        print( jfc["hourly"]["data"][idx]["precipProbability"],datetime.fromtimestamp(jfc["hourly"]["data"][idx]["time"]).strftime('%Y-%m-%d %H:%M:%S') )


