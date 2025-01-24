import datetime

LE = "\n"
L1 = "\t"
L2 = "\t\t"
L3 = "\t\t\t"
L4 = "\t\t\t\t"
CPLM = "©"

def Copyright(name):
    date = datetime.date.today()
    if name is None:
        return "ERROR mane is None"
    cpl = CPLM + str(name) + str(date.year)
    return cpl


