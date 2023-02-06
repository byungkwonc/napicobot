import pybithumb
import time

con_key = "90634f4f04183c3d5fbb3960566df585"
sec_key = "b60e48d7b12d41725bc9b5506670a7b3"

bithumb = pybithumb.Bithumb(con_key, sec_key)
#for ticker in pybithumb.get_tickers() :
#    balance = bithumb.get_balance(ticker)
#    print(ticker, ":", format(balance[0],'f'))
#    time.sleep(0.1)

bcha = bithumb.get_balance("BCHA")
ltc = bithumb.get_balance("LTC")
xrp = bithumb.get_balance("XRP")
bsv = bithumb.get_balance("BSV")
etc = bithumb.get_balance("ETC")
bch = bithumb.get_balance("BCH")

print("비트코인 캐시 에이비씨", bcha)
print("라이트코인", ltc)
print("리플", xrp)
print("비트코인네스브이", bsv)
print("이더리움 클래식", etc)
print("비트코인 캐시", bch)