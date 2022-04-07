from balance import stream_pages, display_date_balance, compute_running_daily_balance, make_daily_balance_aggregator

URL = "https://resttest.bench.co/transactions/PAGE.json"


def main():
    pages = stream_pages(url=URL)
    aggregate_daily_balances = make_daily_balance_aggregator()
    display_date_balance(compute_running_daily_balance(aggregate_daily_balances(pages)))


if __name__ == "__main__":
    main()
