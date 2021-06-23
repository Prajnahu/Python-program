quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
seperators=""
a="abcdefghijklmnopqrstuvwxyz"
for i in quote:
    if i not in a:
        seperators=seperators+i
print(seperators)