from lark import Lark, Transformer

from pdx_tools.pdx_equipent_modules import add_module, navy_module, module_name

sample_pdx_code = """
equipment_modules = {
	limit = {
		has_dlc = "Man the Guns" 
	}
#   ###  ##  #  # ###     ###   ##  ### ### ### ###  #   # 
#    #  #    #  #  #      #  # #  #  #   #  #   #  #  # #  
#    #  # ## ####  #      ###  ####  #   #  ##  ###    #   
#    #  #  # #  #  #      #  # #  #  #   #  #   #  #   #   
### ###  ##  #  #  #      ###  #  #  #   #  ### #  #   #   



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



class pdx_navy_equipment_modules_parse(Transformer):
    navy_module[module_name] = {}
    def equipment_modules(self, tree):
        token = tree[0].value
        return str(token)

pdx_parser = Lark(open("./pdx.lark"),
                  parser='lalr',
                  transformer=pdx_navy_equipment_modules_parse()
                  )



print(pdx_parser.parse(sample_pdx_code).pretty())

