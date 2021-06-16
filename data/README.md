### description of the folders


#### About the Dataset

|Entries | Details | Source |
|--- | --- | ---|
|CRIX | capitalization-weighted market index for cryptocurrencies | Retrieved at: http://data.thecrix.de/data/crix.json
|MArketCap | Market capitalization of Bitcoin | CoinGecko API |
|Stocktwits Sent |  Daily sentiment score of BTC related StockTwits messages | Messages retrieved using StockTwits public API, converted into unigrams and bigrams, then graded their sentiment|
|Reddit Posts Sent |  Daily sentiment score of BTC reated reddit submission | Textual data on Reddit retrieved using Reddit Pushshift API, also converted into unigrams and bigrams, then graded their sentiment
| Reddit Comments Sent | Daily sentiment score of BTC reated reddit comments | same as above
| Trade Volume | Bitcoin Trade Volume | CoinGecko API
| Search Volume | Daily bitcoin google search volume | Google trend- Pytrend
| Stocktwits Volume | Daily message volume on StockTwits | Stocktwits Public api
|Posts  Comments Volume | Daily submission volume on Reddit | reddit Pushfit api
|Comments Volume | Daily comment  volume on Reddit | reddit Pushfit api


```bash



├─ data                      
│  ├─ 00_external            <- Contain rules for sentiment analysis & text processing
│  ├─ 01_raw                 <- Immutable text messages retrieved from stockTwits/reddit
│  └─ 02_processed           <- Data used to developed models
│     ├─ direct              <- Direct sentiment indicators
│     ├─ indirect            <- Indirect sentiment indicators
│     ├─ crix.json           <- Target variable
│     └─ final_dataset.csv

