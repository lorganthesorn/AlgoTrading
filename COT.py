import quandl

soyBeansFuturesAndOptions = ['005602_CITS_ALL', '005602_CITS_ALL_NT', '005602_CITS_ALL_OI', '005602_CITS_CHG'],
all = quandl.get(soyBeansFuturesAndOptions[0])

