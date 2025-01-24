import pykakasi


def nakaten_to_underbar(input):
    result = input.replace("・", "_")
    return result

def class_formatter(input):
    result = input.replace("kyuu", "_class")
    result = result.replace("kyu", "_class")
    result = result.replace("gata", "_class")
    result = result.replace("gou", "go_class")
    result = result.replace("go", "go_class")
    result = result.replace("kata", "_class")
    return result

def convert_name(kanji,tag,type):
    kakasi = pykakasi.kakasi()
    hepburn_list = kakasi.convert(kanji)
    hepburn = ''.join([item['hepburn'] for item in hepburn_list])
    result = "USH_"+ tag +"_"+type+"_"+ nakaten_to_underbar(hepburn)
    result = class_formatter(result)
    return result
