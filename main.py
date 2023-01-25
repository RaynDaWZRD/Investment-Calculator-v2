#Roth, Traditional, Growth, Dividend
investment_list = [{'AMZN':.1,'BAM':.1,'BRK/B':.15,'Cash':.05,'FTEC':.4,'PANW':.05,'PLTR':.05,'GOOGL':.1},#Roth
                   {'AMZN':.1,'BAM':.1,'BRK/B':.3,'Cash':.05,'FTEC':.1,'PANW':.05,'PLTR':.05,'GOOGL':.25},#Traditinal
                   {'AMZN':.1,'DDOG':.1,'PANW':.1,'PLTR':.1,'SCHD':.35,'GOOGL':.25}, #Growth
                   {'APPL':.051,'BAM':.091,'EL':.091,'IIPR':.071,'LVMUY':.111,'MSFT':.131,'NVDA':.131,'SPGI':.091,'TXRH':.121,'ULTA':.061,'UNP':.051}#Dividend
                  ]

def roth_calc(total_cash):
  for key, value in investment_list[0].items():
    allocation = value*total_cash
    allocation = round(allocation,2)
    print(f"Invest {allocation} in {key}")

def trad_calc(total_cash):
  for key, value in investment_list[1].items():
    allocation = value*total_cash
    allocation = round(allocation,2)
    print(f"Invest {allocation} in {key}")

def growth_calc(total_cash):
  for key, value in investment_list[2].items():
    allocation = value*total_cash
    allocation = round(allocation,2)
    print(f"Invest {allocation} in {key}")

def dividend_calc(total_cash):
  for key, value in investment_list[3].items():
    allocation = value*total_cash
    allocation = round(allocation,2)
    print(f"Invest {allocation} in {key}")


def investment_calc():
  account = input("What account are you using? ")
  account = account.lower()
  total_cash = round(float(input("Enter the total amount of cash to invest: ")),2)
  if account == "roth":
    roth_calc(total_cash)
  elif account == "traditional" or (account == 'trad') or (account == 'ira'):
    trad_calc(total_cash)
  elif (account == "growth") or (account == "main"):
    growth_calc(total_cash)
  elif (account == "dividend") or (account == "div"):
    dividend_calc(total_cash)

investment_calc()