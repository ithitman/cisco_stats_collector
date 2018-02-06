"""
This script is to report Total PNL across all open trades and also more specifically each instrument.
It inputs the data into grapfana for web view.
"""
import gdax
b64secret = 'sVvgznt/WcvmtZfTlWcjm0VSjoYvxiWZtK/2MyibEmRCgZoxLfMzrhNtuLbG9lWtHpTBdZRC/FsTl3oHTvQ30w=='
passphrase = 'z3isqrr7wqa4c2wap95jc3di'
key = 'cfd0914b17d3f753ba821ed80361bee8'

auth_client = gdax.AuthenticatedClient(key, b64secret, passphrase)
b = auth_client.get_accounts()
print b
i = 0
while i < len(b):
    print('For Currency ' + b[i]["currency"] + '. Available - ' + b[i]["available"] + ' Balance - ' + b[i]["balance"])
    balance = b[i]["balance"]
    if (float(balance) > 0):
        'Live currenct -- ' + b[i]["currency"]
    i+=1


"""
while i < len(b):
    print('For Currency ' + b[i]["currency"] + '. Available - ' + b[i]["available"] + ' Balance - ' + b[i]["balance"])
    balance = b[i]["balance"]
    if (float(balance) > 0):
        'Live currenct -- ' + b[i]["currency"]
    i+=1
"""
#auth_client.get_product_ticker('BTC-USD')
#print auth_client.get_orders()

#definition to get all open trades

#definition to get current price of an instrument

#definition to get pnl for each instrument

#definition to get account status, total amount of each asset



