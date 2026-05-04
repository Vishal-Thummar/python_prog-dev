spice_mix = set()
print(f"Initial Spice mix Id : {id(spice_mix)}")
print(spice_mix)
spice_mix.add("Ginger")
print(f"Spice mix after adding Ginger : {spice_mix} and Id : {id(spice_mix)}")
spice_mix.add("Cardamom")
print(f"Spice mix after adding Cardamom : {spice_mix} and Id : {id(spice_mix)}")
print(spice_mix)


# Initial Spice mix Id : 4515011872
# set()
# Spice mix after adding Ginger : {'Ginger'} and Id : 4515011872
# Spice mix after adding Cardamom : {'Ginger', 'Cardamom'} and Id : 4515011872
# {'Ginger', 'Cardamom'}