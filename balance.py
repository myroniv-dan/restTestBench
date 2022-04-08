import logging
import operator
from collections import defaultdict
from functools import partial
from itertools import takewhile, count, accumulate
from operator import truth, itemgetter

import requests
from retry import retry
from tqdm import tqdm


def default_response_handler(response):
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return None
    else:
        response.raise_for_status()


@retry(tries=5, delay=1, jitter=(1, 3))
def load_page_data(page_index, url, response_handler=default_response_handler):
    url = url.replace("PAGE", str(page_index))
    response = requests.get(url)
    return response_handler(response)


def stream_pages(url: str):
    try:
        yield from takewhile(truth, map(partial(load_page_data, url=url), count(1)))
    except requests.exceptions.HTTPError as e:
        logging.error(f"unexpected HTTP error: {e}")
        return {}


def display_date_balance(date2running_daily_balance: dict):

    if date2running_daily_balance:
        print("running daily balances:")
        for date, balance in date2running_daily_balance.items():
            print(f"{date} | {balance}")
    else:
        print("there was no data :(")


def compute_running_daily_balance(date2balance: dict):
    return dict(zip(date2balance.keys(), accumulate(date2balance.values(), operator.add)))


def make_daily_balance_aggregator():
    def add_transaction_to_accumulator(transaction: dict):
        date, amount = itemgetter("Date", "Amount")(transaction)
        date2balance[date] += float(amount)

    def aggregate_transactions(page):
        transactions = page["transactions"]
        for transaction in transactions:
            add_transaction_to_accumulator(transaction)

    def aggregate_daily_balances(pages):
        for page in tqdm(pages, desc="accumulating data"):
            aggregate_transactions(page)

        return date2balance

    date2balance = defaultdict(float)

    return aggregate_daily_balances
