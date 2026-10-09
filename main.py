import requests


class CurrencyConverter:

  def __init__(self):
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
    self.rate = requests.get(url).json()[0]["rate"]

  def convert(self, uah):
    return uah / self.rate


if __name__ == "__main__":
  converter = CurrencyConverter()
  amount = float(input("Введіть суму в гривнях: "))
  print(f"Сума в доларах: {converter.convert(amount):.2f} USD")