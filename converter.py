import tkinter as tk  # Modules included

from tkinter import ttk 

root = tk.Tk()  #function for create GUI


class Europe_to_USA(): #This class contains functions which convert Europen units to American units
    
    

    def cm_to_inch(self,deger):  #CM to inches conversion
        
        return deger * 0.3937 

    
    def cm_to_feet(self,deger):  # CM to feet conversion
        
        return deger * 0.328
        
        
    
    def metre_to_yard(self,deger): #M to yard conversion
        
        return deger * 1.0936
        
        
    
    def km_to_Smil(self,deger): # KM to statute mile conversion
        
        return deger * 0.621
        
        
    
    def km_to_Nmil(self,deger): # KM to nautical mile conversion
        
        return deger * 0.539
        
        
    
    def kg_to_lbs(self,deger): # KG to lbs conversion
        
        return deger * 2.2046
        
        
    
    def gr_to_ons(self,deger): #Gr to ons conversion
        
        
        return deger * 0.0352
        
        
    
    def lt_to_Kgalon(self,deger): # Lt to dry gallon conversion
        
        return deger * 0.2270
        
         
    
    def lt_to_Sgalon(self,deger): # Lt to liquid gallon conversion
        
        return deger * 0.2641
        
        
    
    def Celcius_to_Fahrenheit(self,deger): # Celcius to Fahrenheit conversion
        
        return (deger * 1.8) + 32
        
        
    
    def m_to_fathom(self,deger): # Meter to fathom conversion
        
        return deger * 0.547
        
        
    
class USA_to_Europe(): #This class contains functions which convert American  units to Europen units
    
    
    def inch_to_cm(self,deger): #Inch to centimeter conversion
            
        return deger * 2.54
            
        
    def feet_to_cm(self,deger): #Feet to CM conversion
            
        return deger * 30.48
            
        
    def yard_to_metre(self,deger): #Yard to Cm conversion
            
        return deger * 0.9144
            
        
    def Smil_to_km(self,deger): # Statute mile to Km conversion
            
        return deger * 1.609
            
        
        
    def Nmil_to_km(self,deger): # Nautical mile to km conversion
            
        return deger * 1.852
            
        
        
    def lbs_to_kg(self,deger): #Lbs to kg conversion
            
        return deger * 0.45    
        
    def ons_to_gr(self,deger): #Ons to gr conversion
            
        return deger * 28.3495
            
        
        
    def Kgalon_to_lt(self,deger): # dry gallon to liter conversion
            
        return  deger * 4.4048
            
    def Sgalon_to_lt(self,deger): # Liquid gallon to liter conversion
            
        return  deger * 3.7854
            
        
        
    def Fahrenheit_to_Celcius(self,deger): #Fahrenheit to celcius conversion
            
        return (deger - 32) * (5/9)
            
        
       
    def fathom_to_metre(self,deger): #Fathom to meter conversion
            
        return deger * 1.8288
            
        
        
class Ekran(): # Class for GUI widgets
    
    def __init__(self,master):
        
        self.master = master
        
        self.dönüştür=Europe_to_USA() # object from Europe_to_USA class
        
        self.convert=USA_to_Europe() # object from USA_to_Europe class
        
        master.title("Units Converter") # Application Name
 
        
        giris = tk.Label(self.master,text="Enter a value: ",font=(32)) # User Enter a value
        
        giris.grid(row=0,column=6)
        
        self.e1=tk.Entry(self.master)
        
        self.e1.grid(row = 0, column = 8, columnspan = 4, padx = 5, pady = 5)
        
        
        # In one group are collected buttons that convert from European units to American units
        
        self.lf=tk.LabelFrame(self.master,text="Europe to USA",labelanchor="n") 
        
        self.lf.grid(row=1, columnspan=7,sticky="E",padx=5, pady=5, ipadx=5, ipady=5)
        
        # In one group are collected buttons that convert from American units to European units
        
        self.lf2=tk.LabelFrame(self.master,text="USA to Europe",labelanchor = "n")
        
        self.lf2.grid(row=1, column = 22, columnspan = 7,sticky="E",padx=5, pady=5, ipadx=5, ipady=5)

        
        # Create buttons for to convert European units to American units
        
        b1=self.createButton("cm->inch")
        b2=self.createButton("cm->feet")
        b3=self.createButton("m->yard")
        b4=self.createButton("km->Statute mile")
        b5=self.createButton("km->Nautical mile")
        b6=self.createButton("kg->lbs")
        b7=self.createButton("gr->ons")
        b8=self.createButton("lt->Dry gallon")
        b9=self.createButton("lt->Liquid gallon")
        b10=self.createButton("Celcius->Fahrenheit")
        b11=self.createButton("m->fathom")
        b1.grid(row=1,column=0)
        b2.grid(row=1,column=1)
        b3.grid(row=1,column=2)
        b4.grid(row=2,column=0)
        b5.grid(row=2,column=1)
        b6.grid(row=2,column=2)
        b7.grid(row=3,column=0)
        b8.grid(row=3,column=1)
        b9.grid(row=3,column=2)
        b10.grid(row=4,column=0)
        b11.grid(row=4,column=1)
    
        #Create a list for to convert American units to European units
        
        lb=tk.Listbox(self.lf2,highlightcolor="blue",bg="lightgreen")
        
        #Create listbox objects
        
        lb.insert(1,"inch->cm")
        
        lb.insert(2,"feet->cm")
        
        lb.insert(3,"yard->m")
        
        lb.insert(4,"Statute mile->km")
        
        lb.insert(5,"Nautical mile->km")
        
        lb.insert(6,"lbs->kg")
        
        lb.insert(7,"ons->gr")
        
        lb.insert(8,"Dry gallon->lt")
        
        lb.insert(9,"Liquid gallon->lt")
        
        lb.insert(10,"Fahrenheit->Celcius")
        
        lb.insert(11,"fathom->m")
        
        lb.grid(row=1,column=20)
        
        
        tk.Button(self.lf2,text="Convert",command=lambda:self.click(lb.get(lb.curselection()))).grid(row=7,column=20)
        
        
    def createButton(self, val, width = 15): # Create buttons for functions
        return tk.Button(self.lf, text = val, command = lambda:self.click(val), width = width,activebackground="lightgreen",activeforeground="red",bg="yellow")
    
   
    def click(self,deger): #the required funciton is called
        
            
            
            if deger == "cm->inch":
                
               sonuc =self.dönüştür.cm_to_inch(float(self.e1.get()))
              
               
            elif deger =="cm->feet":
                
               sonuc=self.dönüştür.cm_to_feet(float(self.e1.get()))
               
              
            elif deger =="m->yard":
                
                sonuc=self.dönüştür.metre_to_yard(float(self.e1.get()))
                
            elif deger =="km->Statute mile":
                
                sonuc = self.dönüştür.km_to_Smil(float(self.e1.get()))
                
            elif deger =="km->Nautical mile":
                
                sonuc = self.dönüştür.km_to_Nmil(float(self.e1.get()))
                
            elif deger =="kg->lbs":
                
                sonuc = self.dönüştür.kg_to_lbs(float(self.e1.get()))
                
            elif deger =="gr->ons":
                
                sonuc=self.dönüştür.gr_to_ons(float(self.e1.get()))
               
            elif deger == "lt->Dry gallon":
                
                sonuc = self.dönüştür.lt_to_Kgalon(float(self.e1.get()))
                
            elif deger == "lt->Liquid gallon":
                
                 sonuc = self.dönüştür.lt_to_Sgalon(float(self.e1.get()))
                 
            elif deger =="Celcius->Fahrenheit":
                
                sonuc = self.dönüştür.Celcius_to_Fahrenheit(float(self.e1.get()))
                
            elif deger == "m->fathom":
                
                sonuc = self.dönüştür.m_to_fathom(float(self.e1.get()))
                
            elif deger == "inch->cm":
                
                sonuc = self.convert.inch_to_cm(float(self.e1.get()))
                
            elif deger == "feet->cm":
                
                sonuc = self.convert.feet_to_cm(float(self.e1.get()))
                
            elif deger == "yard->m":
                
                sonuc = self.convert.yard_to_metre(float(self.e1.get()))
                
            elif deger == "Statute mile->km":
                
                sonuc = self.convert.Smil_to_km(float(self.e1.get()))
            
            elif deger == "Nautical mile->km":

                sonuc = self.convert.Nmil_to_km(float(self.e1.get()))
                
            elif deger == "lbs->kg":
                
                sonuc = self.convert.lbs_to_kg(float(self.e1.get()))
                
            elif deger == "ons->gr":
                
                sonuc = self.convert.ons_to_gr(float(self.e1.get()))
                
            elif deger == "Dry gallon->lt":
                
                sonuc = self.convert.Kgalon_to_lt(float(self.e1.get()))
                
            elif deger == "Liquid gallon->lt":
                
                sonuc = self.convert.Sgalon_to_lt(float(self.e1.get()))
                
            elif deger == "Fahrenheit->Celcius":
                
                sonuc = self.convert.Fahrenheit_to_Celcius(float(self.e1.get()))
                
                
            elif deger == "fathom->m":
                
                sonuc = self.convert.fathom_to_metre(float(self.e1.get()))
            
            result = tk.Label(self.master,text="Result: ",font=(32)) # the result is printed on the screen
            
            result.grid(row=11,column=6)
            
            #  the result is printed on the screen
        
            self.screen = tk.Text(self.master, state = "normal", width = 20, height = 2, background = "white", foreground = "blue")
    
            self.screen.grid(row =11, column = 7, columnspan = 4)
        
            self.screen.configure(state = "normal") 
            
            self.screen.insert(tk.END,sonuc)
            
            
   
Ekran(root) # GUI object Sent to class 

root.mainloop() #function for create GUI
        