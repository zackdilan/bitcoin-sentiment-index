#### Dataset collection

##### Directory Structure
```bash
├─ src                       <- Source code
│  ├─ data                   <- Package of modules that retrieve raw data
│  │  ├─ __init__.py         
│  │  ├─ __main__.py         <- Run in terminal: $ python -m src.data
│  │  ├─ convert_ts.py       <- Functions to convert between different formats of time
│  │  ├─ others.py           <- Get messages from other sources (google volume, trading volume, FT articles)
│  │  ├─ reddit.py           <- Get messages from reddit
│  │  ├─ stocktwits.py       <- Get messages from stockTwits 
│  │  ├─ utils.py            <- helper functions
|  |  └─ README.md           <- this file

```



