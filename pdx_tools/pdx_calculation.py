armor_magic_number = 7.43902439024

# In Hoi4, 12inch VC steel armor's armor value is 41. In this case, armor_magic_number is 7.43902439024
def armor_convert(armor_thickness):
    return armor_thickness / armor_magic_number

