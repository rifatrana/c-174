from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root = tk()
root.geometry("900x500")
#----------------Burger_image---------
burger = ImageTk.PhotoImage(Image.open(""))
Burger_image=Label(root)
Burger_image["image"]=burger
Burger_image.place(relx=0.7, rely=0.5,anchor=CENTER)
#----------------Heading Rdonalds---------
label_heading=Label(root,text="Rdonalds", font=("time",40,"bold"),fg="Orange")
label_heading.place(relx=0.12, rely=0.1,anchor=CENTER)
#----------------Label_Select_Dish----------
label_select_dish=Label(root,text="Select Dish",font=("times",15))
label_select_dish.place(relx=0.06, rely=0.2,anchor=CENTER)
#-----------------drop down_main dish---------
dish=["burger","iced_americano"]
dish_dropdown = ttk.Combobox(root ,state = "readonly",value = dish)
dish_dropdown.place(relx=0.25, rely=0.2, anchor=CENTER)
#----------------Label_Select_Add-Ons-----------
label_select_addons=Label(root,text="Select Add-Ons",font=("times",15))
label_select_addons.place(relx=0.08, rely=0.5,anchor=CENTER)
#----------------drop_down_toppings---------------
toppings=[]
toppings_dropdown = ttk.Combobox(root,state = "readonly",values = toppings)
toppings_dropdown.place(relx=0.25, rely=0.5, anchor=CENTER)
#-----------------Amount--------------
dish_amount=Label(root,font=("times",15,"bold"))
dish_amount.place(relx=0.2,rely=0.75,anchor=CENTER)

class parent():
    def _init_(self):
        print("This is parent class")
        
    def menu(bish):
       if dish=="burger":
           print("You can add following toppings")
           print("More cheese | Add jalapeno")
       elif dish=="iced_americano":
          print("You can add following toppings")
          print("Add chocolate flavour | Add caramel flavour")
       else:
          print("please enter valid dish")
          
    def final_amount(dish, add_ons):
       if dish=="burger" and add_ons=="cheese":
           print("you need to pay 250 USD")
       elif dish=="burger" and add_ons=="jalepeeno":
           print("you need to pay 350 USD")
       elif dish=="iced_americano" and add_ons=="chocolate":
           print("you need to pay 250 USD")
       elif dish=="iced_americano" and add_ons=="caramel":
           print("you need to pay 450 USD")
              
class child1(parent):
    
    def _init_(self,dish):
        self.new_dish = dish
        
    def get_menu(self):
       parent.menu(self.new_dish)
       
class child2(parent):
    
   def _init_(self,dish,addons) :
        self.new_dish = dish
        self.addons = addons
        
   def get_final_amount(self):
            parent.final_amount(self.new_dish,self.addons)
            
child1_object=child1("burger")
child1_object.get_menu()
            
child2_object=child2("burger","jalepeeno")    
child2_object.get_final_amount

btn_addons = Button(root,text="Check Add-Ons",command=child1_object.get_menu,
                    bg="Blue", fg="white",relief = FLAT)
btn_amount = Button(root,text="Amount",command=child1_object.get_final_amount,
                    bg="Blue", fg="white",relief = FLAT)
btn_amount.place(relx=0.04,rely=0.6, anchor=CENTER)

root.mainloop()            
        