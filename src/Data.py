import datetime as dt

class Data:
    def __init__(self, dia=-1, mes=-1, ano=-1, hora=-1, min=-1, seg=-1):
        if dia != -1 and mes != -1 and ano != -1 and hora != -1 and min != -1 and seg != -1:
            self.data = dt.datetime(ano, mes, dia, hora, min, seg)
        else:
            self.data = dt.datetime.now()