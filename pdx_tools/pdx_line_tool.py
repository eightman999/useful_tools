
pdx_define = {}

def pdx_commentout(sentence : str) -> str:
    return "#" + sentence

def pdx_simple_declaration(sentence : str) -> str:
    return "@ " + sentence

def pdx_declaration(def_ID,def_value):
    global pdx_define
    pdx_define[def_ID] = def_value
    return

def pdx_gui_coordinate(x,y):
    return f"{x} {y}"

def pdx_gui_size(width,height):
    return f"{width} {height}"