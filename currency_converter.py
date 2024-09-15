import exchange_rates 

def convert_usd_to_eur(amount):
    return amount * exchange_rates.USD_TO_EUR

def convert_usd_to_gbp(amount):
    return amount * exchange_rates.USD_TO_GBP

def convert_usd_to_jpy(amount):
    return amount * exchange_rates.USD_TO_JPY

def main():
    usd_amount = 100
    eur_from_usd = convert_usd_to_eur(usd_amount)
    gbp_from_usd = convert_usd_to_gbp(usd_amount)
    jpy_from_usd = convert_usd_to_jpy(usd_amount)

    print(f"${usd_amount} = €{eur_from_usd}")
    print(f"${usd_amount} = €{gbp_from_usd}")
    print(f"${usd_amount} = €{jpy_from_usd}")

    if __name__ == "__main__":
        main()

