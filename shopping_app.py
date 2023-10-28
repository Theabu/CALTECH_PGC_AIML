
userDb = {} #keep track of user objects . this can contain user/admin
sessid=0 #session id
loggedinusers= 0
ProductDb = {} #keep track of product objects 
CateoryDb = {1:"Boots", 
             2:"Coats", 
             3:"Jackets",
             4:"Caps"}
def welcmTxt():
    wlcmtxt = "Welcome to the Demo Marketplace"
    print(wlcmtxt)
#add product to DB
def addProduct(product):
    if product: 
        ProductDb[product.id] = product
        print(f"{product.name} added to product catalogue")
    return
#retrieve user from DB
def removeProduct():
    if name:
        return userDb[name]
def printProduct():
    for key,value in ProductDb.items():
        print(key, ':', value.name)

class product:
    id = ""
    name = ""  #admin/user
    categoryid= ""
    price=0
    
    def __init__(self,id,name,catid,price):
        self.name = name
        self.id = id
        self.categoryid = catid
        self.price = price

#add user to DB
def addUser(user):
    if user: 
        userDb[user.name] = user
        print(f"{user.name} added as {user.role}")
    return
#retrieve user from DB
def getUser(name):
    if name:
        return userDb[name]
#login
def login(name,password):
    if userDb[name].login(password):
        print(f"{userDb[name].name} logged in as {userDb[name].role} ")
        return 
    print("Username/Password did not match" )

#logout
def logout(name):
    return userDb[name].logout()

#Payment API
def payment(amount):
    print("select payment option")
    paymode=input("1) Net Banking\n2) PayPal\n3) UPI\n")
    print(f"You will be shortly redirected to the portal for Unified Payment Interface to make a payment of Rs {amount}")

class user:
    name = ""
    role = ""  #admin/user
    password= ""
    loggedin = False
    cart=[]
    
    sessId = 0
    
    
    def __init__(self,username,password,role):
        global sessid
        self.name = username
        self.password = password
        self.role = role
        self.sessId = sessid
    def login(self,password):
        global sessid
        global loggedinusers
        if self.password == password :
            self.loggedin = True
            loggedinusers = loggedinusers + 1
            sessid=sessid+1
        return self
    def logout(self):
        global loggedinusers
        if self.loggedin:
            self.loggedin = False
            loggedinusers = loggedinusers - 1
            return True
        return False
    def isAdmin(self):
        if self.role == "admin":
            return True
        return False
    def viewProductCat(self):
        if self.loggedin:
            print(f"Displaying Ptoduct Catalogue {self.role}")
            for key,value in ProductDb.items():
                print(f"{key} , {value.name} , {value.price}")
        else:
            print("user not logged in")
    #admin only
    def addCategory(self,id,name): 
        if self.loggedin and self.role == "admin":
            CateoryDb[id] = name
            print("success: new category added")
        else:
            print("Error:Only logged in admin can modify Category Db")
        
    def removeProduct(self,id):
        if self.loggedin and self.role == "admin":
            ProductDb.pop(id)
            print("success:product removed from catalog")
        else:
            print("Error:Only logged in admin can modify product catalogue")
        pass
    def addProduct(self,id,name,catid,price):
        if self.loggedin and self.role == "admin":
            adi_shoe = product(id,name,catid,price)
            ProductDb[id] = adi_shoe
            print("success:product added to catalog")
        else:
            print("Error:Only logged in admin can modify product catalogue")
            
            
        pass
    def updateProduct(sessId):
        pass
    #user only
    def viewCart(self,withname=False):
        print(self.cart)
        if withname:
            for item in self.cart:
                print(item[0],ProductDb[item[0]].name," qty: ",item[1])
    def addToCart(self,a=[]):
        self.cart.append(a)
        pass
    def removeFromCart(self,pid=0,qty=0):
        i = 0
        for items in self.cart:
            if items[0] == pid:
                if qty:
                    items[1] = qty
                else:
                    del self.cart[i]
            i=i+1 
                
        
    def checkout(self):
        fprice=0
        for items in self.cart:
            fprice = fprice + items[1]*ProductDb[items[0]].price 
        return fprice
    
    #
    def setRole(self,role):
        self.role = role
    def setPass(self,passwd):
        self.password = passwd
    
#API for adding/updating/removing users and performing login/logout


        
def PrintUsers():
    print("******Print USER DB **********")
    print(f"Total registered users = {len(userDb)}")
    print(f"Total logged in users = {loggedinusers}")
    for user in userDb.values():
        print(f"username : [{user.name}] , role [{user.role}]")

def main():
    # req1: display Welcome Message
    welcmTxt()
    print()
    print()
    #req2: add users to User DB with their username , password and role . Ideally user input is needed here . 
    print("** CREATING USERS**")
    print()

    addUser(user("Abhinav","poiu","admin"))
    addUser(user("Vikrant","poiv","user"))
    addUser(user("Aditya","poix","user"))
    addUser(user("Hari","poin","user"))
    
    #req2: admin login 
    
    print("**ADMIN/USER LOGIN**")
    print()
    if userDb["Abhinav"].login("poiu").loggedin:
        print("Abhinav logged in as ",userDb["Abhinav"].role)
    
    #  user login
    
    if userDb["Vikrant"].login("poiv").loggedin:
        print("Vikrant logged in as ",userDb["Vikrant"].role)
    
    # Create Sample Product catalog
    print()  
    print("**CREATING PRODUCT CATALOGUE**")
    print()
    addProduct(product(1,"adidas shoe",1,100))
    addProduct(product(2,"Reeebok shoe",1,200))
    addProduct(product(3,"Leather jacket",3,800))
    
    # view product catalog
    print()
    print("**VIEW PRODUCT CATALOGUE WITH USER AND ADMIN ACCOUNTS**")
    print()
    userDb["Abhinav"].viewProductCat()
    userDb["Vikrant"].viewProductCat()
    
    # user rights 
    # add product to cart 
    print()
    print("**ADD PRODUCT TO CART WITH USER ACCOUNT**")
    print()
    userDb["Vikrant"].addToCart([1,4])
    userDb["Vikrant"].addToCart([2,8])
    userDb["Vikrant"].addToCart([3,9])
    print()
    userDb["Vikrant"].viewCart()
    
    #remove product from cart 
    print()
    print("**REMOVE ITEM FROM CART WITH USER ACCOUNT**")
    print()
    userDb["Vikrant"].removeFromCart(pid=1)
    userDb["Vikrant"].viewCart()
    
    
 
    #req2: admin login rights
    print()
    print("**ADMIN LOGIN RIGHTS VALIDATION **")
    print()
    userDb["Abhinav"].login("poiu")
    if userDb["Abhinav"].loggedin:
        print()
        print("login success")
    print()
    print("**ADMIN ADD TO PRODUCT CATALOG**")
    userDb["Abhinav"].addProduct(1,"adidas shoe",1,100)
    userDb["Abhinav"].viewProductCat()
    
    print()
    print("**ADMIN REMOVE TO PRODUCT CATALOG**")
    userDb["Abhinav"].removeProduct(1)
    userDb["Abhinav"].viewProductCat()
    

    #non admin trying to modify product catalog
    print("**Vikrant [non admin] trying to modify product caltalog**")
    userDb["Vikrant"].login("poiv").addProduct(1,"Reebok shoe",1,300)
    print()
    print("CHECKOUT")
    print()
    #Check out and calcultate payment amount
    print("**DISPLAY ITEMS IN CART**") 
    userDb["Vikrant"].viewCart(withname=True)
    fprice = userDb["Vikrant"].checkout()
    print()
    print(f"TOTAL AMOUNT TO PAY = {fprice}")
    
    print()
    print("PAYMENT")
    payment(fprice)


main()

