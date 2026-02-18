fruits=["Apple","Banana","Orange","Kiwi","Mango","Strawberries","Papaya","Avocado"]
cost_price=[90,90,80,100,120,100,70,130]   
sell_price=[110,100,100,120,150,130,90,150]    
stock_qty=[20,30,35,10,40,25,15,10]
sold_qty=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
user_ids=[]
user_names=[]
user_mobile=[]
user_total=[]
while True:

    print("\n--INVENTORY MANAGEMENT-----")
    print("1.Owner")
    print("2.User")
    print("3.Exit")
    role=int(input("Select role: "))
    if role==1:
        while True:
            print("\n-- OWNER SECTION---")
            print("1.Add items to inventory")
            print("2.Remove item")
            print("3.Update item")
            print("4.View Inventory")
            print("5.View User Details")
            print("6.View Report")
            print("7.Total revenue itemized profit")
            print("8.Exit")
            ch=int(input("Enter your choice: "))
            if ch==1:
                fruit=input("Which fruit name: ")
                if fruit in fruits:
                    print("The fruit already exist in inventory")
                else:
                    price=float(input("Enter cost price: "))
                    selling_price=float(input("Enter selling price:"))
                    quantities=int(input("Enter quantity: "))

                    fruits.append(fruit)
                    cost_price.append(price)
                    sell_price.append(selling_price)
                    stock_qty.append(quantities)
                    sold_qty.append(0)
                    print(fruit,"added successfully")
            elif ch==2:
                fruit=input("Enter which fruit to remove: ")
                if fruit in fruits:
                    i=fruits.index(fruit)
                    fruits.pop(i)
                    cost_price.pop(i)
                    sell_price.pop(i)
                    stock_qty.pop(i)
                    sold_qty.pop(i)

                    print(fruit,"removed successfully")
                    print(fruits)
                else:
                    print(fruit,"is not available")
            elif ch==3:
                fruit=input("Enter fruit name to update: ")
                if fruit in fruits:
                    i=fruits.index(fruit)
                    sell_price[i]=float(input("Enter new price: "))
                    stock_qty[i]=int(input("Enter new quantity"))
                    print("updated successfully")
                else:
                    print(fruit,"Not found!")



            elif ch==4:
                print("*"*10,"INVENTORY","*"*10)
                if len(fruits)==0:
                    print("Inventory is empty")
                else:
                    
                    for i in range(len(fruits)):
                        print(fruits[i],"|Price:",sell_price[i],"per KG|Qty:",stock_qty[i],"KG")
            elif ch==5:
                print("*"*10,"USERS DETAILS","*"*10)
                if len(user_ids)==0:
                    print("No users yet")
                else:
                    for i in range(len(user_ids)):
                        print("User ID:",user_ids[i])
                        print("Name:",user_names[i])
                        print("Mobile:",user_mobile[i])
                        print("Total Purchase:",user_total[i])
            elif ch==6:
                print("*"*10,"SALES REPORT","*"*10)
                for i in range(len(fruits)):
                    print(fruits[i],"|Sold:",sold_qty[i],"KG")

            elif ch==7:
                print("*"*10,"REPORT","*"*10)
                total_revenue=0
                total_profit=0
                for i in range(len(fruits)):
                    revenue=sell_price[i]*sold_qty[i]
                    profit=(sell_price[i]-cost_price[i])*sold_qty[i]
                    total_revenue+=revenue
                    total_profit+=profit
                    print(fruits[i])
                    print("Sold:",sold_qty[i],"KG")
                    print("Revenue:",revenue)
                    print("Profit:",profit)
                    print("*"*25)
                    print("Total Revenue:",total_revenue)
                    print("Total Profit:",total_profit)
            elif ch==8:
                print("Done")
                break

            else:
                print("Choose correct option")
    elif role==2:
        cart=[]
        cart_qty=[]
        while True:
            print("\n---USER MENU---")
            print("1.Add to cart")
            print("2.Remove from cart")
            print("3.Modify cart")
            print("4.View cart")
            print("5.Billing")
            print("6.Exit")
            ch=int(input("Enter your choice: "))
            if ch==1:
                fruit=input("Enter fruit: ")
                if fruit in fruits:
                    if fruit in cart:
                        print(fruit,"already in cart")
                    else:
                        i=fruits.index(fruit)
                        qty=int(input("How much qunatity: "))
                        if qty<=stock_qty[i]:
                            cart.append(fruit)
                            cart_qty.append(qty)
                            stock_qty[i]=stock_qty[i]-qty
                            sold_qty[i]=sold_qty[i]+qty
                            print(fruit,"added to cart")
                            print("Available quantity now:",stock_qty[i],"KG")
                        else:
                            print("Insufficient stock")
                else:
                    print(fruit,'is not available')

            elif ch==2:
                fruit=input("Which fruit name:")
                if fruit in cart:
                    i=cart.index(fruit)
                    qty=cart_qty[i]
                    f_index=fruits.index(fruit)
                    stock_qty[f_index]=stock_qty[f_index]+qty
                    sold_qty[f_index]=solde_qty[f_index]-qty
                    cart.pop(i)
                    cart_qty.pop(i)
                    print(fruit,"removed from cart")
                else:
                    print(fruit,"not in cart")
            elif ch==3:
                fruit=input("Enter fruit name: ")
                if fruit in cart:
                    i=cart.index(fruit)
                    new_qty=int(input("Enter new quantity in KG:"))
                    f_index=fruits.index(fruit)
                    diff=new_qty-cart_qty[i]
                    if diff<=stock_qty[f_index]:
                        cart_qty[i]=new_qty
                        stock_qty[f_index]=stock_qty[f_index]-diff
                        sold_qty[f_index]=sold_qty[f_index]+diff
                        print("Cart updated")
                    else:
                        print("No enough stock")
                else:
                    print(fruit,"not in cart")
            elif ch==4:
                print("*"*10,"CART","*"*10)
                if len(cart)==0:
                    print("Cart is empty")
                else:
                    for i in range(len(cart)):
                        print(cart[i],"| Quantity:",cart_qty[i],"KG")
                    
            elif ch==5:
                print("*"*20,"BILLING","*"*20)
                u_name=input("Enter user name: ")
                while True:
                    
                    mobile_no=input("Enter user mobile no:")
                    if len(mobile_no)==10:
                        mobile_no=int(mobile_no)
                        break
                total=0
                for i in range(len(cart)):
                    cost=sell_price[fruits.index(cart[i])]
                    amt=cost*cart_qty[i]
                    total=total+amt
                    print(cart[i],"| Qty:",cart_qty[i],"KG | Amount:",amt)
                print("Total Bill:",total)
                user_ids.append(len(user_ids)+1)
                user_names.append(u_name)
                user_mobile.append(mobile_no)
                user_total.append(total)
                cart.clear()
                cart_qty.clear()
                print("Thank you for shopping!")
                
            elif ch==6:
                print("Shopping Done")
                break

            else:
                print("Choose correct option")
    elif role==3:
        print("Exit from system")
        break
else:
    print("Please choose correct role")
