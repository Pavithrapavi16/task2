print("Property type \n1.Apartment \n2.Condo  \n3.BoatHouse \n4.Land")
selection=input("select any one:")
S=["balcony","airconditioning","internet access","gym","garden","pools","rooms","music","buildings","garage","hotels"]
choice=input()
Apartment=["balcony","airconditioning", "internet acess"]
Condo=("aaa","abc" ,"acc")
boatHouse=("baa", "bab", "bcc")
Land=("caa", "cab","cac")
if selection=="1":
    if choice=="balcony" or choice=="airconditioning" or choice=="internetaccess":
        print("property type : {0}-{1}".format("Apartment",choice))
    else:
       print("invalid selection") 
elif selection=="2":
    if choice=="gym" or choice=="garden" or choice=="pools":
        print("property type : {0}-{1}".format("Condo",choice))
    else:
       print("invalid selection") 
elif selection=="3":
    if choice=="rooms" or choice=="music":
        print("property type : {0}-{1}".format("BoatHouse",choice))
    else:
       print("invalid selection") 
elif selection=="4":
    if choice=="buildings" or choice=="garage" or choice=="hotels":
        print("property type : {0}-{1}".format("Land",choice))
    else:
       print("invalid selection") 
else:
    print("not a valid selection")
