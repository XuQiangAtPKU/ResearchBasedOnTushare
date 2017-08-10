import datetime
from util.penDataProcess import ProcessData, ProcessDataArr
if __name__ == '__main__':
    startDate = datetime.date(2017, 4, 1);
    endDate = datetime.date(2017, 5, 1);
    currCode = '300367'
    ProcessDataArr(currCode, startDate, endDate);
    # ProcessData(currCode, str(startDate));