navy_modules = []
navy_module={}
critical_parts = {}
can_convert_from = {}
add_average_stats = {}
multiply_stats = {}
add_stats = {}
sfx = ""
category = ""
abbreviation = ""
module_name = ""

def can_convert_from_modulecategory(module_category, cost):
    can_convert_from = {
        "module_category": module_category,
        "convert_cost_ic": cost
    }
    return can_convert_from

def can_convert_from_module(module, cost):
    can_convert_from = {
        "module": module,
        "convert_cost_ic": cost
    }
    return can_convert_from

def create_module(module_name, category, abbreviation, sfx, critical_parts, can_convert_froms, add_average_stats, multiply_stats, add_stats):
    navy_module[module_name] = {
        "category": category,
        "abbreviation": abbreviation,
        "sfx": sfx,
        "critical_parts": critical_parts,
        "can_convert_froms": can_convert_froms,
        "add_average_stats": add_average_stats,
        "multiply_stats": multiply_stats,
        "add_stats": add_stats
    }

    return navy_module

