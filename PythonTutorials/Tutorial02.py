"""

Pandas - what are the libraries in here?


"""
import pandas as pd
import datetime
import pandas_datareader as web



start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.now()


df = web.get_data_tiingo('GOOG', api_key=os.getenv('TIINGO_API_KEY'))
print(df.head())
