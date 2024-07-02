from abc import ABC, abstractmethod

class Hcost(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def cost_etm(cst):
        pass
amtH=0
def cost_etm(cst):
    return (amtH+cst)
def get(price):
    print("your total payment :: ",price)

csthc, csths, csthp = 0, 0, 0
class Haircare():
    def __init__(self):
        pass
    def hairspa(self):
        spa = {1: 1000, 2: 2020, 3: 1500, 4: 2200, 5: 3000, 6: 4500, 7: 799}
        print("\n.......HairSpa.......\n")
        print("""1. Hair breakage ----- 1000 Rs.
2. Thinning hair ----- 2020 Rs.
3. Hair fall ----- 1500 Rs.
4. Dry and dull hair ----- 2200 Rs.
5. Rough hair ----- 3000 Rs.
6. Dry and itchy scalp ----- 4500 Rs.
7. Dandruff ----- 799 Rs.
""")
        print("......................................................")
        hcp = int(input("Enter your choice :: "))
        if hcp in spa:
            cst = spa[hcp]
            csthp = cost_etm(cst)
            get(csthp)

    def hair_Style(self):
        style = {1: 3999, 2: 1599, 3: 2599, 4: 1999}
        print("\n..................Hair_Style..................\n")
        print("""1. straight ----- 3999 Rs.
2. wavy ----- 1599 Rs.
3. curly ----- 2599 Rs.
4. tight curls ----- 1999 Rs.
""")
        print("......................................................")
        hcs = int(input("Enter your choice :: "))
        if hcs in style:
            cst = style[hcs]
            csths = cost_etm(cst)
            get(csths)

    def hair_cutting(self):
        cut = {1: 1999, 2: 799, 3: 1500, 4: 599, 5: 2000, 6: 1800}
        print("\n.......Hair_Cutting.......\n")
        print("""1. blunt chops without layers ------ 1999 Rs.
2. medium neck-length bobs ------ 799 Rs.
3. shorter pixies ----- 1500 Rs.
4. one-length haircuts ----- 599 Rs.
5. modern shags ----- 2000 Rs.
6. textured haircuts ----- 1800 Rs.""")
        print("......................................................")
        hct = int(input("Enter your choice :: "))
        if hct in cut:
            cst = cut[hct]
            csthc = cost_etm(cst)
            get(csthc)

