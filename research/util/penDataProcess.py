from util.connectionPool import mongoConnection
from util.processBar import ProgressBar
import datetime
import json
import tushare as ts
import pandas as pd

def ProcessData(code, date):
    client = mongoConnection.GetClient();
    db = client.stock;
    penCollection = db.pen_data;
    data = ts.get_tick_data(code, date=date);
    dataLength = len(data['time']);
    if(dataLength < 10):
        raise Exception("Invalid volume", dataLength);
    data['code'] = pd.Series([code] * dataLength);
    data['time'] =pd.Series([date + ' '] * dataLength) + data['time'];
    data['type'] = data['type'].apply(lambda x: 1 if x == '买盘' else -1);
    data['change'] = data['change'].apply(lambda x: float(0) if x == '--' else float(x));
    records = json.loads(data.to_json(orient='records'));
    penCollection.insert(records);



def ProcessDataArr(code, startDate, endDate):
    days = (endDate - startDate).days;
    bar = ProgressBar(total = days);
    output = open('log', 'a');
    for i in range(days):
        currDate = startDate + datetime.timedelta(days= i)
        bar.move();
        bar.log(str(currDate))
        if currDate.weekday() > 4:
            continue;
        try:
            ProcessData(code, str(currDate));
        except Exception as e:
            output.write(str(currDate) + '\n');
            output.write("Exception: " +str(e) + '\n');
    output.close();