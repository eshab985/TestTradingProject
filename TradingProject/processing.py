import math
import pandas as pd
from django.templatetags.static import static
import csv
from threading import Thread
import os
import json
def executor(csv_file, timeframe):
     res = list()
     thread = Thread(target=create_json, args = (csv_file, int(timeframe), res))
     thread.start()

     thread.join()
     return res

def oddeven(timeframe, res):
    print('oddeven')
    if timeframe%2 == 0:
        res.append('Even')
    else:
        res.append('Odd')
def create_json(csv_file, timeframe, res):
    rows = []
    module_dir = os.path.dirname(__file__)  # get current directory
    url = os.path.join(module_dir, 'TradingProject/'+csv_file)
    
    with open(url) as file:
            data = list(csv.DictReader(file)) #Converted into list of OrderedDict
            print(data[0])
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
    #print(rows)
    df = pd.DataFrame(rows, columns=['BANKNIFTY','DATE','TIME','OPEN','HIGH','LOW','CLOSE','VOLUME'])
    print(df)
    json_filename = 'nifty_data_timeframe_{}.json'.format(timeframe)
    r = df.to_json()
    print('****JSON Output****:')
   
 
    # Writing to sample.json
    with open("json_output.json", "w") as outfile:
        outfile.write(r)
   
    return r
    