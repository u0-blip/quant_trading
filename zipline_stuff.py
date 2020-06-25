apikey = 9AQgPq87PWxxSRCQsDVb

need to change the 
C:\Users\peter\Anaconda3\envs\trade\lib\site-packages\zipline\data\benchmarks.py

to
+    IEX_TOKEN = 'pk_c88b455c96e54a6b965aa23c1797f5ad'  # FIXME: move to param
     r = requests.get(
-        'https://api.iextrading.com/1.0/stock/{}/chart/5y'.format(symbol)
+        'https://cloud.iexapis.com/stable/stock/{}/chart/5y?token={}'.format(
+            symbol, IEX_TOKEN)
     )


import pandas as pd
from trading_calendars import get_calendar

def get_benchmark_returns(symbol, first_date, last_date):
    cal = get_calendar('NYSE')
    
    dates = cal.sessions_in_range(first_date, last_date)

    data = pd.DataFrame(0.0, index=dates, columns=['close'])
    data = data['close']

    return data.sort_index().iloc[1:]

    
loader.py
data = get_benchmark_returns(symbol, first_date, last_date)

