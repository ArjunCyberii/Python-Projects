def listt():
    car=["AUDI","BMW","BENZ","RR","FARARY"]
    print(type(car)) # IT show the what type is "CAR" variale

    #"Append" a value , the value in any type like int,string,boolen,flot ect
    car.append("WW")
    car.append(1)
    car.append(True)
    car.append(0.12)
    
    print(car)

    #"Insert" a value , inset a value in a specific place usinf index number ,
    # index number starts from 0.
    bike=["TVS","HONDA","RoyalEnfield","HERO"]
    bike.insert(0,"BMW")# hello inset in the first place 
    bike.insert(4,"FZ")
    print(bike)

    #"POP" this is used for remove a value from the list
    laptop=["Lenova","HP","DELL","MSI"]
    laptop.pop(0)
    laptop.pop(2)
    print(laptop)

    #"EXTEND" this is used for merge two list
    a=[1,2]
    b=[3,4]
    a.extend(b)
    
    print(a)
listt()

def tuplee():
    #the tuple is allow any type of variable and allow duplicate
    # BUT WE CANT Modify
    #But we can change the tuple into list and then change
    car=("BMW","BENZ")
    print(car)
    bike=list(car)
    print(bike)
    bike.append("Hello")
    bike.insert(0,33)
    bike.pop(2)
    print(bike)
tuplee()

def sett():
    frutes={}

