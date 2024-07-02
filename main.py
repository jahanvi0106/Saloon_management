from Saloon import About
from Saloon import Makeover
from Saloon import Hareccare
from Saloon import Skincare



print("\n__________________About____________________")
About.info()

print("\n______________________________________________________________________________________________")
print("""\n____________________________Your Requirements..?________________________________
1. Hair Care
2. Skin Care
3. Makeover""")
Req = int(input("Enter your requirement no. :: "))
if Req == 1:
    ho = Hareccare.Haircare()
    print("\n_______________________Hair Care_______________________\n")
    print("""_____________________Which service you want???________________________
1. Hair Spa
2. Hair Style
3. Hair Cutting""")
    hReq = int(input("Enter your Service no. :: "))
    if hReq == 1:
        ho.hairspa()
    elif hReq == 2:
        ho.hair_Style()
    elif hReq == 3:
        ho.hair_cutting()
elif Req == 2:
    so = Skincare.Skincare()
    print("\n_______________________Skin Care_______________________\n")
    print("""_____________________Which service you want???________________________
1. skin_treatment
2. massage""")
    sReq = int(input("Enter your Service no. :: "))
    if sReq == 1:
        so.skin_treatment()
    elif sReq == 2:
        so.massage()

elif Req == 3:
    print("\n_______________________Makeover_______________________\n")
    mo = Makeover.Makeover()
    print("""_____________________Which service you want???________________________
1. Bride
2. Regular""")
    mReq = int(input("Enter your Service no. :: "))
    if mReq == 1:
        mo = Makeover.Bride()
        mo.bd()
    elif mReq == 2:
        mo = Makeover.Regular()
        mo.rg()


