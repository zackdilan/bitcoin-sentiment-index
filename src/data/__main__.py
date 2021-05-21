#!/usr/bin/env python3
"""
Getting Messages from Stocktwit and Reddit
Run in terminal : `python -m src.data[args]`
"""
from . import stocktwits, reddit, others, utils
from .convert_ts import ts_to_unix
import pandas as pd
import argparse

# ap = argparse.ArgumentParser()
# # ap.add_argument('-w', '--whole', help='Boolean to specify : true-get whole crypto data, false - get data'
# #                                       ' only for some specific coins(must provide other arguments))', type=bool,
# #                 required=True, default=True)
# # ap.add_argument('-s', '--stocktwit', nargs='+', help='Specify the stocktwit cash tag of the coins  eg. '
# #                                                      'BTC.X-- Bitcoin', default=None)
# # ap.add_argument('-r', '--reddit', nargs='+', help='Specify the subreddit tag of the coins  eg. '
# #                                                   'Bitcoin ', default=None)
# ap.add_argument('-c', '--coin', help='Specify the coin of study eg')
# ap.parse_args()

if __name__ == '__main__':
    # Get StockTwits messages
    start = '2014-11-28 00:00:00'
    end = '2021-05-10 00:00:00'
    start_unix = ts_to_unix(start)
    end_unix = ts_to_unix(end)

    # st_cashtag = pd.read_csv('data/00_external/symbols.csv', header=None)[1]
    # symbols = st_cashtag[st_cashtag.str.endswith('.X')].to_list()
    symbol = 'BTC.X'  # cash tag for Bitcoin
    try:
        stocktwits.get_tweets(symbol, start, end,
                              file_name=f"data/01_raw/stocktwits/"
                                        f"{symbol[:-2]}_stocktwits.csv")
    except IndexError:
        print(f"No tweet with {symbol} exists on StockTwits.")
        print("------------")
    # print(
    #     f"Combining files containing tweets with a single cashtag to one "
    #     f"master file...")
    # print("------------")
    # combined_csv = pd.concat(
    #     [pd.read_csv(f"data/01_raw/stocktwits/{symbol[:-2]}.csv") for symbol in
    #      symbols], ignore_index=True)
    # combined_csv.to_csv("data/01_raw/stocktwits.csv")

    # Get Reddit comments & submissions
    subreddits = ['Bitcoin']
    start_unix = ts_to_unix(start)
    end_unix = ts_to_unix(end)

    for subreddit in subreddits:
        reddit.get_comments(subreddit, start_unix, end_unix,
                            file_name=f"data/01_raw/reddit/comments_"
                                      f"{subreddit}.csv")
        reddit.get_submissions(subreddit, start_unix, end_unix,
                               file_name=f"data/01_raw/reddit/submissions_"
                                         f"{subreddit}.csv")

    # # Get trade volume
    # others.get_trade_volume(start_unix, end_unix,
    #                         file_name=f'data/02_processed/indirect'
    #                                   f'/trade_volume.csv')
    others.get_bitcoin_trade_volume(days=utils.no_days(start, end),
                                    file_name=f'data/02_processed/indirect'
                                              f'/bitcoin_trade_volume.csv')


    # Get daily Google Trends
    others.get_google_trends('bitcoin', start_unix, end_unix,
                             file_name=f'data/02_processed/indirect'
                                       f'/google_trends.csv')
