import datetime
import re

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
    import re
    pattern = re.compile(r'\b(' + '|'.join(map(re.escape, dic.keys())) + r')\b')
    return pattern.sub(lambda x: dic[x.group()], text)


# replacer = replace_m("A B C")
# result = replacer.rep("A", "1").rep("B", "2").rep("C", "3").get_text()
# print(result)  # 出力: 1 2 3

class replace_m:
    def __init__(self, text):
        self.text = text
        self.replacements = []  # 置換操作を蓄積

    def rep(self, old, new):
        """個別の置換を蓄積して適用"""
        self.replacements.append((old, new))
        return self  # チェーン可能にする

    def rep_all(self, dic):
        """辞書を用いた一括置換"""
        pattern = re.compile(r'\b(' + '|'.join(map(re.escape, dic.keys())) + r')\b')
        self.text = pattern.sub(lambda x: dic[x.group()], self.text)
        return self

    def get_text(self):
        """蓄積された rep の適用を一括で行う"""
        for old, new in self.replacements:
            self.text = re.sub(rf'\b{re.escape(old)}\b', new, self.text)
        return self.text
# # EXAMPLE
#
# text = "(101,202,303)"
# dic = {"101": "303", "202": "101", "303": "202"}
#
# # 期待通りの結果になる
# replacer = replace_m(text)
# res = replacer.rep_all(dic).get_text()
# print(res)  # "(303,101,202)"
#
# res_1 = multi_replace(text, dic)
# print(res_1)  # "(303,101,202)"
#
# res_2 = replacer.rep("101", "303").rep("202", "101").rep("303", "202").get_text()
# print(res_2)  # "(303,101,202)"