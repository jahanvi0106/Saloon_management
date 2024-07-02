import abc

from abc import ABC, abstractmethod
class Makeover():
    pass

class mCost(ABC):
    @abstractmethod
    def cost_etm(self):
        pass
amtM=0
def cost_etm(cst):
    return amtM+cst
costtt = 0
def get(price):
    print("your total payment :: ", price)

class Bride(Makeover):
    def __init__(self):
        pass
    def bd(self):
        ##dictionary for cost of packages
        cst_b = {1: 15999, 2: 29999, 3: 49999}
        print("\n______Provided Package______\n")
        print("""1. Silver
2. Gold
3. Platinum""")
        brd = int(input("Enter your choice ::  "))
        if brd in cst_b:
            cst = cst_b[brd]
            cstb = cost_etm(cst)
            get(cstb)

class Regular(Makeover):
    def __init__(self):
        pass
    def rg(self):
        t = []
        print("\n______Provided services______\n")
        print("""1. Hairstyle 
2.Makeup""")
        lsev = []
        a=1
        print("\nIf you want any service then choose 1 otherwise 0")
        while(a!=0):
            sev = int(input("Enter your requirement :: "))
            lsev.append(sev)
            a = int(input("Enter 0 or 1 :: "))
        if 1 in lsev:
            t.append(599)
            print("""\n1. Open hair with strings of Gajras
2. Mermaid side bun for the fun look
3. A bun and a braid
4. Cascading curls with purple blooms
5. Easy messy hairstyle
6. Stunning rose twists
7. A simple braid with a simple Gajra
8. If you want flower""")
            choice = int(input("Enter your hairstyle :: "))
            ex_choice = int(input("if you want flower than chosse 8 :: "))
            if ex_choice == 8:
                ### cost of flower
                cst_f = {1: 20, 2: 25, 3: 15, 4: 30, 5: 35}
                print("\n______________Flower_________________\n")
                print("""1. Rose ------ Rs 20 
2. Lotus ------ Rs 25
3.Jasmine ------ Rs 15
4.Tulip ------ Rs 30
5. Lavender ------ Rs 35""")
                flw = int(input("Enter which flower you want :: "))
                if flw in cst_f:
                    t.append(cst_f[flw])
        if 2 in lsev:
            cst_ms = {1: 1999, 2: 4999, 3: 5999}
            print("""\n___________which makeup you want_____________
1. Simple ------ Rs 1999
2. Party ------ Rs 4999
3. Marriage ----- Rs 5999""")
            mkc = int(input("Enter no you want :: "))
            if mkc in cst_ms:
                t.append(cst_ms[mkc])
        print(t)
        costtt = sum(t)
        get(costtt)







