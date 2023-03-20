from product import product
def getChoices(choices):
    s = ""
    s += "0.) Exit\n"
    n=1
    for ch in choices:
        s += str(n)+  ".) "+ ch + "\n"
        n+=1
    return s
def getInt(s):
    n = None
    try:
        n = int(s)
    except Exception as e:
        pass
    return n

def makeMenu(prompt,choices): 
    n = None
    while n == None or n < 1 or n > len(choices):
        print(getChoices(choices))
        c = input(prompt+"\n")
        n = getInt(c)
        if n == 0:
            return None
        elif n == None or n < 1 or n > len(choices):
            print("Invalid choice.\n")
    return n-1
main_menu=['create','read','update','delete']
updateselection=['product name','product id(pk)']
result= makeMenu('Select action for the Product',main_menu)
print(result)
if result==0: #create
    u = product()
    d = {}
    d['name'] = input('Enter Product Name: ')
    d['description'] = input('Enter Product Description: ')
    d['price'] = input('Enter the Product price: ')
    d['stock'] = input('Enter Product Stock: ')
    u.set(d)
    u.insert()
    print(u.data)

if result==1: #read
    u=product()
    readmenu=['read by id','read by name','read all']
    readresult=makeMenu('How would you like to read',readmenu)
    if readresult==0:
        idresult=input("Enter the id: ")
        u.getById(idresult)
    if readresult==1:
        nameresult=input("Enter the product name: ")
        u.getByProduct(nameresult)
    if readresult==2:
        u.getAll()
    print(u.data)

if result == 2: #update
    u=product()
    u.getAll()
    user_index = makeMenu('Select Action',u.toList())
    u.getById(user_index+1)
    #print(u.data[user_index])
    updateresult = makeMenu('How do you want to update?',u.fields)
    if updateresult==0:
        nameupdate=input('Enter the name to be updated: ')
        u.data[0]['name']=nameupdate
        u.update()
    if updateresult==1:
        descupdate=input('Enter the description to be updated: ')
        u.data[0]['description']=descupdate
        u.update()
    if updateresult==2:
        priceupdate=input("Enter the price to be updated: ")
        u.data[0]['price']=priceupdate
        u.update()
    if updateresult==3:
        stockupdate=input("Enter the stock to be updated: ")
        u.data[0]['stock']=stockupdate
        u.update()
    print('Updated')

if result== 3: #delete
    u=product()
    id=input("Enter the Id: ")
    u.deleteById(id)
