from molmass import ELEMENTS, Element

Compound = input("Enter your compound *SEE USAGE INSTRUCTIONS IN README*: ")

Elements = [e for e in Compound if e.isalpha()]

Tracking = {}
for element in Elements:
    Tracking[element] = 0


for e in Elements:
    try:
        if Compound[Compound.index(e)+1].isnumeric():
            Tracking[e] += int(Compound[Compound.index(e)+1])
        else:
            Tracking[e] += 1
    except:
        Tracking[e] += 1

print(Tracking)
molarmass = 0

for e in set(Elements):
    print(ELEMENTS[e].mass)
    molarmass += ELEMENTS[e].mass * Tracking[e]
    print(molarmass)

print(f"Your molar mass: {round(molarmass, 3)}")