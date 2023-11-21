import pandasdmx as sdmx
import pandas as pd
from sqlalchemy import create_engine

# define the source 1, will get exchange rate data from European Central Bank
ecb = sdmx.Request('ECB')
# ecb = Request('ECB')

# extract data from ECB with selected currency and period
data_response1 = ecb.data(resource_id = 'EXR', key={'CURRENCY': ['AUD', 'EUR']}, params = {'startPeriod': '2000-01', 'endPeriod': '2023-08'})
data1 = data_response1.data[0]
type(data1)

# flow_msg = ecb.dataflow()
# flow_msg.response.url
# flow_msg.response.headers
# flow_msg

# obtain the data with selection criteria
# dataflows = sdmx.to_pandas(flow_msg.dataflow)
# dataflows.head()
# dataflows[dataflows.str.contains('exchange', case=False)]
# exr_msg = ecb.dataflow('EXR')
# exr_msg.response.url

# set(s.key.FREQ for s in data.series)

# extract the monthly average data
monthly = [s for sk, s in data1.series.items() if sk.FREQ == 'M' and sk.EXR_SUFFIX == 'A']

cur_df = pd.concat(sdmx.to_pandas(monthly)).unstack()
cur_df.shape
cur_df.tail()
# print(cur_df)

# load data to database "Source" in table "ExchangeRate"
engine = create_engine("sqlite:////workspaces/made-template/data/sources.sqlite")
cur_df.to_sql('ExchangeRate', engine, index = False)


# define the source 2, will get tourist data from Australian Bureau of Statistics (ABS)
abs = sdmx.Request('ABS_XML')

# 还要修改怎么写，以及如何利用api的链接extract data from ABS with selected countries, period and person type 
data_response2 = abs.data('OAD_COUNTRY', key = key, params = params)
data2 = data_response2.data[0]
type(data2)