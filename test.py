import datetime
import unittest

import balance


PAGE = [
    {
        "totalCount": 38,
        "page": 1,
        "transactions": [
            {
                "Date": "2013-12-19",
                "Ledger": "Business Meals & Entertainment Expense",
                "Amount": "-35.7",
                "Company": "NESTERS MARKET #x0064 VANCOUVER BC",
            },
            {
                "Date": "2013-12-21",
                "Ledger": "Travel Expense, Nonlocal",
                "Amount": "-8.1",
                "Company": "BLACK TOP CABS VANCOUVER BC",
            },
            {
                "Date": "2013-12-22",
                "Ledger": "Phone & Internet Expense",
                "Amount": "-110.71",
                "Company": "SHAW CABLESYSTEMS CALGARY AB",
            },
            {
                "Date": "2013-12-21",
                "Ledger": "Business Meals & Entertainment Expense",
                "Amount": "-9.88",
                "Company": "GUILT & CO. VANCOUVER BC",
            },
            {
                "Date": "2013-12-20",
                "Ledger": "Travel Expense, Nonlocal",
                "Amount": "-7.6",
                "Company": "VANCOUVER TAXI VANCOUVER BC",
            },
            {
                "Date": "2013-12-20",
                "Ledger": "Business Meals & Entertainment Expense",
                "Amount": "-120",
                "Company": "COMMODORE LANES & BILL VANCOUVER BC",
            },
            {
                "Date": "2013-12-20",
                "Ledger": "Business Meals & Entertainment Expense",
                "Amount": "-177.5",
                "Company": "COMMODORE LANES & BILL VANCOUVER BC",
            },
            {
                "Date": "2013-12-20",
                "Ledger": "Equipment Expense",
                "Amount": "-1874.75",
                "Company": "NINJA STAR WORLD VANCOUVER BC",
            },
            {
                "Date": "2013-12-19",
                "Ledger": "",
                "Amount": "20000",
                "Company": "PAYMENT - THANK YOU / PAIEMENT - MERCI",
            },
            {
                "Date": "2013-12-19",
                "Ledger": "Web Hosting & Services Expense",
                "Amount": "-10.99",
                "Company": "DROPBOX xxxxxx8396 CA 9.99 USD @ xx1001",
            },
        ],
    }
]

DATE_BALANCE = {
    "2013-12-22": -110.71,
    "2013-12-21": -17.98,
    "2013-12-20": -2179.85,
    "2013-12-19": 19953.309999999998
}

RUNNING_DAILY_BALANCE = {
    "2013-12-22": -221.42,
    "2013-12-21": -35.96,
    "2013-12-20": -4359.7,
    "2013-12-19": 39906.62
}


def format_date2balance(date2balance):
    return {datetime.datetime.strptime(d, '%Y-%m-%d'): b for d, b in date2balance.items()}


class TestTransactions(unittest.TestCase):
    def test_daily_balance_aggregator(self):
        assert format_date2balance(DATE_BALANCE) == balance.make_daily_balance_aggregator()(PAGE)

    def test_running_total_aggregator(self):
        assert format_date2balance(RUNNING_DAILY_BALANCE) == balance.make_daily_balance_aggregator()(PAGE * 2)


if __name__ == "__main__":
    unittest.main()
