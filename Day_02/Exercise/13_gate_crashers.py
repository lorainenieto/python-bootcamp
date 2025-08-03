invited = {"Ana", "Ben", "Carlo", "Dani"}
attended = {"Ben", "Carlo", "Ely"}

#Who are all the involved members?
involved = invited.union(attended)
print(f"Involved Members: {involved}")
#Who was absent
absent = invited - attended
print(f"Absent:{absent}")
#Who gatecrashed
gatecrashed = attended - invited
print(f"Not enrolled but attended: {gatecrashed}")
#Who was invited and attended
intersect = invited.intersection(attended)
print(f"Attended properly: {intersect}")




















