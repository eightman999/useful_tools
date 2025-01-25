from lark import Lark, Transformer, Token

# Larkの文法を定義
grammar = """
    start: "equipment_modules" "=" "{" module+ "}"
    module: NAME "=" "{" prop+ "}"
    prop: "category" "=" NAME
        | "abbreviation" "=" ESCAPED_STRING
        | "sfx" "=" NAME
        | "critical_parts" "=" "{" NAME ("," NAME)* "}"
        | "add_stats" "=" "{" stat_pair+ "}"
        | "multiply_stats" "=" "{" stat_pair+ "}"
        | "add_average_stats" "=" "{" stat_pair+ "}"
        | "can_convert_from" "=" "{" stat_pair+ "}"
    stat_pair: NAME "=" (SIGNED_NUMBER | NAME)

    %import common.CNAME -> NAME
    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
"""

# Transformerクラスを定義して、パース結果を処理
class NavyEquipmentTransformer(Transformer):
    def __init__(self):
        self.navy_modules = {}

    def start(self, items):
        return self.navy_modules

    def module(self, items):
        module_name = items[0]
        module_props = items[1:]

        # 初期化
        module_data = {
            "category": None,
            "abbreviation": None,
            "sfx": None,
            "critical_parts": [],
            "can_convert_from": {},
            "add_average_stats": {},
            "multiply_stats": {},
            "add_stats": {}
        }

        for prop in module_props:
            if prop is None:
                continue
            key, value = prop
            if key == "category":
                module_data["category"] = str(value)  # 文字列に変換
            elif key == "abbreviation":
                module_data["abbreviation"] = value.strip('"')
            elif key == "sfx":
                module_data["sfx"] = value
            elif key == "critical_parts":
                module_data["critical_parts"] = [str(v) for v in value]  # 文字列に変換
            else:
                module_data[key] = value

        self.navy_modules[module_name] = module_data

    def prop(self, items):
        if len(items) < 2:
            return None  # エラーハンドリング：itemsに要素が足りない場合
        key = items[0]
        value = items[1]
        if key in ["category", "abbreviation", "sfx", "critical_parts"]:
            print(key)
            print(f"{key}: [{value}]")
            return key, [value]
        else:
            return key, value

    def stat_pair(self, items):
        key = items[0]
        value = items[1]
        if isinstance(value, str):
            return key, value
        else:
            return key, float(value)

    def critical_parts(self, items):
        # critical_partsの値を文字列に変換してリストで返す
        return "critical_parts", [str(v) for v in items]

    def add_stats(self, items):
        return "add_stats", {key: value for key, value in items}

    def multiply_stats(self, items):
        return "multiply_stats", {key: value for key, value in items}

    def add_average_stats(self, items):
        return "add_average_stats", {key: value for key, value in items}

    def can_convert_from(self, items):
        # can_convert_fromのキーと値を文字列に変換
        return "can_convert_from", {str(k): v for k, v in items}

# パーサーの作成
parser = Lark(grammar, parser='lalr', transformer=NavyEquipmentTransformer())

# サンプルテキスト
sample_text = """
equipment_modules = {
    ship_light_battery_1 = {
        abbreviation = "saa"
        category = ship_light_battery
        sfx = sfx_ui_sd_module_turret
        add_stats = {
            lg_attack = 1
            build_cost_ic = 90
        }
        multiply_stats = {
            naval_speed = -0.01
        }
        add_average_stats = {
            lg_armor_piercing = 1
        }
        can_convert_from = {
            module_category = ship_light_battery
            convert_cost_ic = 60
        }
        critical_parts = { damaged_light_guns }
    }
}
"""

# パーサーを実行して結果を取得
parsed_data = parser.parse(sample_text)

# 結果を表示
# print(parsed_data)