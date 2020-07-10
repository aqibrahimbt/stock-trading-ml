# Different Stock Market API's (Requirements/Limitations/Usage)


## Marketstack
- json based API
- maximum 1000 req/month
- usable over requests
``requests.get('https://api.marketstack.com/v1/tickers/aapl/eod', access_key=YOUR_KEY)``


- 72 diff. API's worlwide


## IEXCloud
- json, csv or psv based REST API
- maximum 50.000 req/month
- U.S. only
- probably 15 mins delayed (unsure)


``requests.get('https://cloud.iexapis.com/')``


## Yahoo
- indeed still (again) in service 
- possibly unlimited amount of req?
``pip install yfinance``


## Additional Data Sources
- https://github.com/wilsonfreitas/awesome-quant#data-sources