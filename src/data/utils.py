from datetime import datetime


def no_days(start):
    """
    
    :param start:(str) provide the start date  
    :param end: (str) provide the end date 
    :return: (int) no of days between two dates(including the start date)
    """

    end = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    return abs((end - start).days + 1)
