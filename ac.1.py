print("============================")
print("     Welcome to cat ride    ")
print("============================")
print()

print("step 1:pick your vehicle")
print("1 - bike ")
print("2 - mario's cart ")
print()

choice = int(input("enter 1 or 2: "))
print()

if choice == 1:
    print("Step 2:pick bike type")
    print(" 1 - Scooty")
    print(" 2 - Mountain Bike")
    print()

    bike_type = int(input("enter 1 or 2: "))
    print()

    if bike_type==1:
        print("u piked   : scooty")
        print("top speed : 80km")
        print("best for  : yong yong city roads")
    else:
        print("u piked   : Mountain Bike")
        print("top speed : 40km/h")
        print("best for  : cat ear mountain rode")

elif choice == 2:
    print("step 2: pick ur car type")
    print(" 1 - sedan")
    print(" 2 - suv")
    print()

    ct=int(input("enter 1 or 2: "))
    print()

    if ct==1:
        print("u picked sedan")
        print("seats : 5 passengers")
        print("best for: cat picnic")

    else:
         print("u picked suv")
         print("seats :7 passengers")
         print("best for:adventuerrr")
else:
        print("that was not a valid choice.")
        print("pls enter 1or 2.")
print()
print("=================")
print(" ur ride is over ")
print("=================")
        