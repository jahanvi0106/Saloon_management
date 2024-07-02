import abc
from abc import ABC, abstractmethod
class sCost(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def cost_etm(cst):
        pass
amtS=0
def cost_etm(cst):
    return (amtS + cst)
def get(price):
    print("your total payment :: ",price)


cstm, cstst = 0, 0

class Skincare(ABC):
    def __init__(self):
        pass
    def skin_treatment(self):
        st = {1: 834, 2: 1995, 3: 2989, 4: 3990}
        print("""\n1. Chemical Peels ------ Rs. 834
2. Laser Resurfacing ------ Rs. 1995
3. Laser Skin Rejuvenation ------ Rs. 2989
4. Acne Blue Light Therapy ------ Rs. 3990""")
        print("\n____________________________________________________")
        stc = int(input("Enter your choice :: "))
        if stc in st:
            cst = st[stc]
            cstst = cost_etm(cst)
            get(cstst)

    def massage(self):
        m = {1: 4999, 2: 3999, 3: 4500, 4: 2500}
        print("""\n1. Craniosacral Therapy ------ Rs. 4999
2. Deep Tissue Massage ------ Rs. 3999
3. Hot Stone Massage ------ Rs. 4500
4. Myofascial Massage ------ Rs. 2500""")
        print("\n____________________________________________________")
        msc = int(input("Enter your choice :: "))
        if msc in m:
            cst = m[msc]
            cstm = cost_etm(cst)
            get(cstm)






