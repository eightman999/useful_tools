import datetime

LE = "\n"
L1 = "\t"
L2 = "\t\t"
L3 = "\t\t\t"
L4 = "\t\t\t\t"
CPLM = "©"

# EXAMPLE
# print(Copyright("Eightman"))  # 出力: ©Eightman2021

def Copyright(name):
    date = datetime.date.today()
    if name is None:
        return "ERROR mane is None"
    cpl = CPLM + str(name) + str(date.year)
    return cpl

# EXAMPLE
# dic = {"A": "1", "B": "2", "C": "3"}
# text = "A B C"
# print(multi_replace(text, dic))  # 出力: 1 2 3

def multi_replace(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

# EXAMPLE
# replacer = replace_m("A B C")
# result = replacer.rep("A", "1").rep("B", "2").rep("C", "3").get_text()
# print(result)  # 出力: 1 2 3

class replace_m:
    def __init__(self, text):
        self.text = text

    def rep(self, old, new):
        self.text = self.text.replace(old, new)
        return self

    def get_text(self):
        return self.text