import pandas as pd
import csv
import math
csv_filename = 'nifty_data.csv'
timeframe = 10
rows = []
with open(csv_filename) as file:
        data = list(csv.DictReader(file)) #Converted into list of OrderedDict
        min_low = math.inf
        max_high = -math.inf
        first_open = 0.0
        last_close = 0.0
        last_volume = 0.0
        for i in range(0, len(data)):
            max_high = max(max_high, float(data[i]['HIGH']))
            min_low = min(min_low, float(data[i]['LOW']))
            if i%timeframe == 0:
                first_open = data[i]['OPEN']
                date = data[i]['DATE']
                time = data[i]['TIME']
            if (i+1)%timeframe == 0:
                 last_close = data[i]['CLOSE']
                 last_volume = data[i]['VOLUME']
                 
                 rows.append({'NIFTY_F1', date, time, first_open, max_high, min_low,last_close,last_volume})
                 
                 min_low = math.inf
                 max_high = -math.inf
            i += timeframe

df = pd.DataFrame(rows, columns=['BANKNIFTY','DATE','TIME','OPEN','HIGH','LOW','CLOSE','VOLUME'])
df.to_json('nifty_data_timeframe_{}.json'.format(timeframe), orient = 'split', compression = 'infer', index = 'true')
print(df)

        