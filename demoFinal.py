#GUI in python
#use the tkinter library for GUI components
from tkinter import *
#create a window to display our widgets
window = Tk()

 
#WINDOW SIZE
window.geometry("600x1000")

#WINDOW TITLE
window.title('COVID VACCINATION INFORMATION')


#CONFIDENTIAL LABEL
label_1 = Label(window, text= 'All information will be kept confidential', width=30, font=('bold', 20))
label_1.place(x=100, y=20)


label_2 = Label(window, text='Name', width=30, font=('bold', 15))
label_2.place(x=-50, y=80)
userName = StringVar()
nameEntry = Entry(window, textvariable=userName)
nameEntry.configure(width=40)
nameEntry.place(x=140,y=80)



label_3 = Label(window, text='E-mail', width=30, font=('bold', 15))
label_3.place(x=-50, y=120)

userEmail = StringVar()

emailEntry = Entry(window, textvariable=userEmail)

emailEntry.configure(width=40)

emailEntry.place(x=140,y=120)



label_n = Label(window, text='Phone #', width=30, font=('bold', 15))
label_n.place(x=-50, y=160)

userPhone = StringVar()

PhoneEntry = Entry(window, textvariable=userPhone)

PhoneEntry.configure(width=40)

PhoneEntry.place(x=140,y=160)





label_v = Label(window, text='Vaccination', width=30, font=('bold', 15))
label_v.place(x=-40, y=200)

vacList = ['Pfizer', 'Johnson & Johnson', 'Moderna']

vac = StringVar()
vac.set('Company')

dropDownList = OptionMenu(window, vac, *vacList)
dropDownList.place(x=160, y=200)





label_v = Label(window, text='Shot', width=30, font=('bold', 15))
label_v.place(x=-40, y=240)

ShotList = ['first', 'second', 'booster']
#create a variable to hold the contents of the option selected
Shot = StringVar()
Shot.set('Number')

dropDownList = OptionMenu(window, Shot, *ShotList)
dropDownList.place(x=160, y=240)









label_4 = Label(window, text='Side Effects', font=('italic', 18))
label_4.place(x=250, y = 270)

#create a check box
PAIS = IntVar()
paisBox = Checkbutton(window, text='Pain at injection site', variable=PAIS, onvalue=1, offvalue=0)
paisBox.place(x=50, y=300)
#create a check box
PDA = IntVar()
PdaBox = Checkbutton(window, text='Pain down arm', variable=PDA,  onvalue=1, offvalue=0)
PdaBox.place(x=200, y=300)
#create a check box
fev = IntVar()
fevBox = Checkbutton(window, text='Fever', variable=fev,  onvalue=1, offvalue=0)
fevBox.place(x=325, y=300)



#create a check box
head = IntVar()
headBox = Checkbutton(window, text='Headache', variable=head, onvalue=1, offvalue=0)
headBox.place(x=395, y=300)
#create a check box
Naus = IntVar()
NausBox = Checkbutton(window, text='Nausea', variable=Naus, onvalue=1, offvalue=0)
NausBox.place(x=50, y=320)
#create a check box
Rash = IntVar()
RashBox = Checkbutton(window, text='Rash', variable=Rash, onvalue=1, offvalue=0)
RashBox.place(x=200, y=320)

#create a check box
Hives = IntVar()
HivesBox = Checkbutton(window, text='Hives', variable=Hives,  onvalue=1, offvalue=0)
HivesBox.place(x=325, y=320)
#create a check box
Swell = IntVar()
SwellBox = Checkbutton(window, text='Swelling', variable=Swell,  onvalue=1, offvalue=0)
SwellBox.place(x=395, y=320)
#create a check box
Chills = IntVar()
ChillsBox = Checkbutton(window, text='Chills', variable=Chills,  onvalue=1, offvalue=0)
ChillsBox.place(x=50, y=340)

BA=IntVar()
BABox = Checkbutton(window, text='Body ache', variable=BA,  onvalue=1, offvalue=0)
BABox.place(x=200, y=340)
#create a check box
NoSymptoms = IntVar()
NoneBox = Checkbutton(window, text='None', variable=NoSymptoms,  onvalue=1, offvalue=0)
NoneBox.place(x=325, y=340)


def submitFunction():
    userName1 = userName.get()
    userPhone1= userPhone.get()
    userEmail1= userEmail.get()
    vac1=vac.get()
    Shot1=Shot.get()
    Shots=open("ShotReactions.txt",'w')
    Shots.write(userName1)
    Shots.write( '\n')
    Shots.write (userPhone1)
    Shots.write('\n' )
    Shots.write(userEmail1)
    Shots.write('\n')
    Shots.write(vac1)
    Shots.write('\n')
    Shots.write(Shot1)
    Shots.write('\n')
    if (Naus.get() == 1):
        Shots.write('Nausea; ')
        
    else:
        pass
    if (head.get() == 1):
        Shots.write('Headache; ')
        
    else:
        pass
    if (PAIS.get() == 1):
        Shots.write('Pain at injection site; ')
    else:
        pass
    if (PDA.get() == 1):
        Shots.write('Pain down arm; ')
        
    else:
        pass
    if (fev.get() == 1):
        Shots.write('Fever; ')
        
    else:
        pass
    if (Rash.get() == 1):
        Shots.write('Rash; ')
    else:
        pass
    if (Hives.get() == 1):
        Shots.write('Hives; ')  
        
    if (Swell.get() == 1):
            Shots.write('Swelling; ')
    else:
            pass
    if (Chills.get() == 1):
            Shots.write('Chills; ')
            
    else:
            pass
    if (BA.get() == 1):
            Shots.write('Body Ache; ')
    else:
            pass
    if (NoSymptoms.get() == 1):
            Shots.write('None') 
    userName.set('')
    userEmail.set('')
    userPhone.set('')
    vac.set('            ')
    Shot.set('          ')
    Naus.set(0)
    head.set(0)
    PAIS.set(0)
    PDA.set(0)
    fev.set(0)
    Rash.set(0)
    Hives.set(0)
    Swell.set(0)
    Chills.set(0)
    BA.set(0)
    NoSymptoms.set(0)
    
    Shots.close()

myButton = Button(window, text='Submit', width=20, bg='red', fg='green', 
command=submitFunction)
myButton.place(x=200, y=400)

def clearFunction():
    userName.set('')
    userEmail.set('')
    userPhone.set('')
    vac.set('            ')
    Shot.set('          ')
    Naus.set(0)
    head.set(0)
    PAIS.set(0)
    PDA.set(0)
    fev.set(0)
    Rash.set(0)
    Hives.set(0)
    Swell.set(0)
    Chills.set(0)
    BA.set(0)
    NoSymptoms.set(0) 
    
    
clearButton = Button(window, text='Start/Clear', width=5, bg='white', fg='black', 
command=clearFunction)
clearButton.place(x=500, y=30)


window.mainloop()



