Internal_Types = [
    "Land",
    "Air",
    "Naval"
]

Group_By_types = [
    "archetype",
    "type"
]

Interface_Categories = [
    "interface_category_land",
    "interface_category_armor",
    "interface_category_capital_ships",
    "interface_category_screen_ships",
    "interface_category_other_ships",
    "interface_category_air"
]

common_resources = {
    "steel": 0,
    "oil": 0,
    "rubber": 0,
    "aluminium": 0,
    "tungsten": 0,
    "chromium": 0
}

equipment_name = ""
year = 0
picture = ""
can_be_produced = {}
is_archetype = False
is_buildable = False
active = False
type = ""
group_by = ""
priority = 0
interface_category = ""
resources = {}
modifiers = {} #modifires are stats
archetype = ""
module_slots = {}
default_modules = {}
archetypes = {}
visual_level = 0


def build_new_archetype():
    archetype = {}
    archetype["equipment_name"] = equipment_name
    archetype["year"] = year
    archetype["picture"] = picture
    archetype["can_be_produced"] = can_be_produced
    archetype["is_archetype"] = is_archetype
    archetype["is_buildable"] = is_buildable
    archetype["active"] = active
    archetype["type"] = type
    archetype["group_by"] = group_by
    archetype["priority"] = priority
    archetype["interface_category"] = interface_category
    archetype["resources"] = resources
    archetype["modifiers"] = modifiers
    archetypes["archetype_name"] = equipment_name
    archetypes["archetype"] = archetype
    return archetype

def build_new_archetype_from_dict(archetype_dict):
    archetype = {}
    archetype["equipment_name"] = archetype_dict["equipment_name"]
    archetype["year"] = archetype_dict["year"]
    archetype["picture"] = archetype_dict["picture"]
    archetype["can_be_produced"] = archetype_dict["can_be_produced"]
    archetype["is_archetype"] = archetype_dict["is_archetype"]
    archetype["is_buildable"] = archetype_dict["is_buildable"]
    archetype["active"] = archetype_dict["active"]
    archetype["type"] = archetype_dict["type"]
    archetype["group_by"] = archetype_dict["group_by"]
    archetype["priority"] = archetype_dict["priority"]
    archetype["interface_category"] = archetype_dict["interface_category"]
    archetype["resources"] = archetype_dict["resources"]
    archetype["modifiers"] = archetype_dict["modifiers"]
    archetypes["archetype_name"] = equipment_name
    archetypes["archetype"] = archetype
    return archetype

def build_new_archetype_from_values(equipment_name, year, picture, can_be_produced, is_archetype, is_buildable, active, type, group_by, priority, interface_category, resources, modifiers):
    archetype = {}
    archetype["equipment_name"] = equipment_name
    archetype["year"] = year
    archetype["picture"] = picture
    archetype["can_be_produced"] = can_be_produced
    archetype["is_archetype"] = is_archetype
    archetype["is_buildable"] = is_buildable
    archetype["active"] = active
    archetype["type"] = type
    archetype["group_by"] = group_by
    archetype["priority"] = priority
    archetype["interface_category"] = interface_category
    archetype["resources"] = resources
    archetype["modifiers"] = modifiers
    archetypes["archetype_name"] = equipment_name
    archetypes["archetype"] = archetype
    return archetype

def create_new_equipment():
    equipment = {}
    equipment["equipment_name"] = equipment_name
    equipment["year"] = year
    equipment["picture"] = picture
    equipment["archetype"] = archetype
    equipment["active"] = active
    equipment["type"] = type
    equipment["priority"] = priority
    equipment["visual_level"] = visual_level
    equipment["interface_category"] = interface_category
    equipment["resources"] = resources
    equipment["modifiers"] = modifiers
    return equipment

def create_new_equipment_from_dict(equipment_dict):
    equipment = {}
    equipment["equipment_name"] = equipment_dict["equipment_name"]
    equipment["year"] = equipment_dict["year"]
    equipment["picture"] = equipment_dict["picture"]
    equipment["archetype"] = equipment_dict["archetype"]
    equipment["active"] = equipment_dict["active"]
    equipment["type"] = equipment_dict["type"]
    equipment["priority"] = equipment_dict["priority"]
    equipment["visual_level"] = equipment_dict["visual_level"]
    equipment["interface_category"] = equipment_dict["interface_category"]
    equipment["resources"] = equipment_dict["resources"]
    equipment["modifiers"] = equipment_dict["modifiers"]
    return equipment

def create_new_equipment_from_values(equipment_name, year, picture, archetype, active, type, priority,visual_level, interface_category, resources, modifiers):
    equipment = {}
    equipment["equipment_name"] = equipment_name
    equipment["year"] = year
    equipment["picture"] = picture
    equipment["archetype"] = archetype
    equipment["active"] = active
    equipment["type"] = type
    equipment["priority"] = priority
    equipment["visual_level"] = visual_level
    equipment["interface_category"] = interface_category
    equipment["resources"] = resources
    equipment["modifiers"] = modifiers
    return equipment

def build_new_modulable_archetype():
    archetype = {}
    archetype["equipment_name"] = equipment_name
    archetype["year"] = year
    archetype["picture"] = picture
    archetype["can_be_produced"] = can_be_produced
    archetype["is_archetype"] = is_archetype
    archetype["is_buildable"] = is_buildable
    archetype["active"] = active
    archetype["type"] = type
    archetype["group_by"] = group_by
    archetype["priority"] = priority
    archetype["interface_category"] = interface_category
    archetype["resources"] = resources
    archetype["modifiers"] = modifiers
    archetype["module_slots"] = module_slots
    archetype["default_modules"] = default_modules
    archetypes["archetype_name"] = equipment_name
    archetypes["archetype"] = archetype
    return archetype

def build_new_modulable_archetype_from_dict(archetype_dict):
    archetype = {}
    archetype["equipment_name"] = archetype_dict["equipment_name"]
    archetype["year"] = archetype_dict["year"]
    archetype["picture"] = archetype_dict["picture"]
    archetype["can_be_produced"] = archetype_dict["can_be_produced"]
    archetype["is_archetype"] = archetype_dict["is_archetype"]
    archetype["is_buildable"] = archetype_dict["is_buildable"]
    archetype["active"] = archetype_dict["active"]
    archetype["type"] = archetype_dict["type"]
    archetype["group_by"] = archetype_dict["group_by"]
    archetype["priority"] = archetype_dict["priority"]
    archetype["interface_category"] = archetype_dict["interface_category"]
    archetype["resources"] = archetype_dict["resources"]
    archetype["modifiers"] = archetype_dict["modifiers"]
    archetype["module_slots"] = archetype_dict["module_slots"]
    archetype["default_modules"] = archetype_dict["default_modules"]
    archetypes["archetype_name"] = equipment_name
    archetypes["archetype"] = archetype
    return archetype

def build_new_modulable_archetype_from_values(equipment_name, year, picture, can_be_produced, is_archetype, is_buildable, active, type, group_by, priority, interface_category, resources, modifiers, module_slots, default_modules):
    archetype = {}
    archetype["equipment_name"] = equipment_name
    archetype["year"] = year
    archetype["picture"] = picture
    archetype["can_be_produced"] = can_be_produced
    archetype["is_archetype"] = is_archetype
    archetype["is_buildable"] = is_buildable
    archetype["active"] = active
    archetype["type"] = type
    archetype["group_by"] = group_by
    archetype["priority"] = priority
    archetype["interface_category"] = interface_category
    archetype["resources"] = resources
    archetype["modifiers"] = modifiers
    archetype["module_slots"] = module_slots
    archetype["default_modules"] = default_modules
    archetypes["archetype_name"] = equipment_name
    archetypes["archetype"] = archetype
    return archetype

def create_new_modulable_equipment():
    equipment = {}
    equipment["equipment_name"] = equipment_name
    equipment["year"] = year
    equipment["picture"] = picture
    equipment["archetype"] = archetype
    equipment["active"] = active
    equipment["type"] = type
    equipment["priority"] = priority
    equipment["visual_level"] = visual_level
    equipment["interface_category"] = interface_category
    equipment["resources"] = resources
    equipment["modifiers"] = modifiers
    equipment["module_slots"] = module_slots
    equipment["default_modules"] = default_modules
    return equipment

def create_new_modulable_equipment_from_dict(equipment_dict):
    equipment = {}
    equipment["equipment_name"] = equipment_dict["equipment_name"]
    equipment["year"] = equipment_dict["year"]
    equipment["picture"] = equipment_dict["picture"]
    equipment["archetype"] = equipment_dict["archetype"]
    equipment["active"] = equipment_dict["active"]
    equipment["type"] = equipment_dict["type"]
    equipment["priority"] = equipment_dict["priority"]
    equipment["visual_level"] = equipment_dict["visual_level"]
    equipment["interface_category"] = equipment_dict["interface_category"]
    equipment["resources"] = equipment_dict["resources"]
    equipment["modifiers"] = equipment_dict["modifiers"]
    equipment["module_slots"] = equipment_dict["module_slots"]
    equipment["default_modules"] = equipment_dict["default_modules"]
    return equipment

def create_new_modulable_equipment_from_values(equipment_name, year, picture, archetype, active, type, priority,visual_level, interface_category, resources, modifiers, module_slots, default_modules):
    equipment = {}
    equipment["equipment_name"] = equipment_name
    equipment["year"] = year
    equipment["picture"] = picture
    equipment["archetype"] = archetype
    equipment["active"] = active
    equipment["type"] = type
    equipment["priority"] = priority
    equipment["visual_level"] = visual_level
    equipment["interface_category"] = interface_category
    equipment["resources"] = resources
    equipment["modifiers"] = modifiers
    equipment["module_slots"] = module_slots
    equipment["default_modules"] = default_modules
    return equipment

