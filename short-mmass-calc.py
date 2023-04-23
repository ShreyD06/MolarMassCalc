import re
try:
  from molmass import ELEMENTS
  get_molar_mass = lambda elem: ELEMENTS[elem].mass    # If molmass is installed, use that
except ImportError:
  get_molar_mass = {'H': 1, 'O': 16, 'C': 12, 'Zn': 65.4}.get   # Fallback to manual dictionary

c = input("Compound: ")
l = re.findall(r'([A-Z][a-z]*)(\d*)', c)   # Split list into element-name, count (or empty string) tuples
molmass = sum(int(n if n else 1) * get_molar_mass(elem) for elem, n in l)  # Adds up elements in l
print(molmass)
