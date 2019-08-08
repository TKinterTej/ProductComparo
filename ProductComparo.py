
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox               #These are libraries that were imported into the Python program
import tkinter
import time
import tkinter.filedialog

def Help():
    Help = Tk()
    Help.geometry('577x70')
    Help.configure(bg='Yellow')         #Here, the function 'Help' is defined as a window with a set size, colour, and a label infroming the user about
                                        #The way the Tab buttons work if called.
    Help.title("HELP")
    text1 = "Choose File to get options:\n Close and Exit to leave program;\nSave As to save program. Thank you for using PriceComparo!"
    Label(Help,text=text1,bg='Green',relief=SUNKEN,font='Arial 14 bold').grid(row=0,column=0)

def File_Save():                                        #Define 'File_Save'
    file = Tk()
    file.geometry('300x50')
    file.configure(bg='Red')
    file.title('Save Details')
    name = (userName)
    product = (productName)
    price = (bestPrice)
    rating = (bestRated)
    shippingOpt = (bestShippOpt)
    details = ('Thanks for using PriceComparo %s; here is the breakdown of your %s:\nThe best price is $: %s\nThe best rated is : %s stars\nThe best Shipping Option costs $: %s' % (name,product,price,rating,shippingOpt))
    fileName = input("Please enter the name of your desired file save.")
    fileExtension = input("Please enter the file extension fo your desired file save. Ex. .py or .txt")
    fileOpen = open('%s %s' % (fileName,fileExtension),'w+')
    fileOpen.write(details)
    lbl1 = Label(file,bg='Green',font='Cooper 12 bold',relief=GROOVE,text='Your file is saved as %s %s' % (fileName,fileExtension)).grid(row=0,column=0)

                                                        #Here, the global variables which hold the product details are created. A product description is created, which then allows
                                                        #The user to enter file specifications, and then open the file later on.

def Save():                                             #Define 'Save'
    root = Tk()
    root.geometry("300x50")
    root.configure(bg='Blue')
    root.title("Program Options")                       #Creation and customization of the Tab buttons window in the overall function 'Save'
    menubar=Menu(root,bg='Blue')
    text=Text(root,bg='Blue')
    text.pack()
    filemenu=Menu(menubar,tearoff=0,bg='Blue')
    filemenu.add_command(label="Save as...", command=File_Save)
    filemenu.add_command(label="Close", command=root.destroy)
    filemenu.add_separator()                            #Program creates Save as and Close dropdowns, and defines their commands.

    filemenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
                                                        #Program creates the 'File' dropdown, and 'Help' dropdowns.
    helpmenu=Menu(menubar,tearoff=0,bg='Red')
    helpmenu.add_command(label="Help",command=Help)
    menubar.add_cascade(label="Help",menu=helpmenu)

    root.config(menu=menubar)                           #Program finishes of the creation of the window.
    root.mainloop()

def Sorter():                                           #Define 'Sorter'

    global userName,productName,bestPrice,bestRated,bestShippOpt


    name         =      []
    product      =      []
    prices       =      []                              #Creation of empty lists for storing the user's information.
    reviews      =      []
    shippingOpts =      []

    nameValues     =   e1.get()
    productValues  =   e2.get()
    priceValues    =   e3.get()                         #Storing the entry values into their corresponding variables.
    reviewValues   =   e4.get()
    shippingValues =   e5.get()

    name.append(nameValues)
    name1 = (name[0].split(','))
    name1.sort()
    userName = name1[0]

    product.append(productValues)
    product1 = (product[0].split(','))
    product1.sort()
    productName= product1[0]

    prices.append(priceValues)
    prices1 = (prices[0].split(','))                #Program splits the entries into items by commas, and appends their values into their corresponding lists.
    prices1.sort()
    bestPrice = prices1[0]
    prices1.sort()

    reviews.append(reviewValues)
    reviews1 = (reviews[0].split(','))
    reviews1.sort()
    bestRated = reviews1[-1]
    reviews1.sort()

    shippingOpts.append(shippingValues)
    shippingOpts1 = (shippingOpts[0].split(','))
    shippingOpts1.sort()
    bestShippOpt = shippingOpts1[0]
    shippingOpts1.sort()




    tab = Tk()
    tab.title("Product Breakdown")
    tab.configure(background="Blue")                    #New window 'tab' created.


                                                        #Labels are created, and each outputs the values of the product by price,reviews, and shipping options.

    Label(tab, text=("Product Breakdown of your",(product[0])),bg='Red',font='Cooper 24 bold underline',relief=GROOVE).grid(row=0)
    Label(tab, text=("The best price for your",(product1[0]),"costs $:",(prices1[0])),bg="Yellow",font="Showcard 10 bold underline",relief=GROOVE,width=45).grid(row=1,column=0)
    Label(tab, text=("The best rated",(product1[0]),"is rated: %s stars" % (reviews1[-1])),bg='Yellow',font='Showcard 10 bold underline',relief=GROOVE,width=45).grid(row=2,column=0)
    Label(tab, text=("The best shipping option for a",(product1[0]),"costs $: %s" % (shippingOpts1[0])),bg='Yellow',font='Showcard 10 bold underline',relief=GROOVE,width=45).grid(row=3,column=0)
    Label(tab, text=("Thanks for using PriceComparo",(name1[0]),"!!!"),bg='Red',font='Showcard 12 bold underline',relief=RIDGE,width=36).grid(row=4,column=0)

                                                        #Buttons created, where 'Quit' destorys window 'tab', and 'Save Results' calls function 'Save'.
    Button(tab, text='Quit',bg="Red",font="Cooper 12 bold underline italic", command=tab.destroy,relief=RAISED).grid(row=6, column=0, sticky=W, pady=4)
    Button(tab, text='Save Results',bg='Green',font='Cooper 12 bold underline italic',command=Save,relief=RAISED).grid(row=6, column=1, sticky=W, pady=4)

    tab.geometry('630x250+350+250')                     #Size set for window 'tab'.
    tab.mainloop()


loading = Tk()
loading.configure(bg = 'dark violet',relief=GROOVE)     #Creation of initilaizing window, and customization of the window with colours and pictures
loading.title('Initialization')
Label(loading,text='Please Wait While PriceComparo Initializes...',bg='Purple',relief=RAISED,font='Cooper 12 bold underline italic').grid(row=50,column=2)
image = PhotoImage(file='loading.gif')
Label(loading,image = image).grid(row=10,column=2)
loading.geometry('338x200')
loading.after(500, lambda: loading.configure(bg='Red'))
loading.after(1000, lambda: loading.configure(bg='Blue'))
loading.after(1500, lambda: loading.configure(bg='Green'))
loading.after(2000, lambda: loading.configure(bg='Yellow'))
loading.after(2500, lambda: loading.configure(bg='Purple'))#Here, the switching of the window 'loading' occurs using the 'after' method, before the window is destroyed after 5s
loading.after(3000, lambda: loading.configure(bg='Orange'))#500 Represents half-second, which is the time interval for window colour switching.
loading.after(3500, lambda: loading.configure(bg='White'))
loading.after(4000, lambda: loading.configure(bg='Black'))
loading.after(4500, lambda: loading.configure(bg='Brown'))
loading.after(5000, lambda: loading.destroy())


loading.mainloop()

intro = Tk()
intro.title("Price Comparison")
intro.configure(background='medium sea green')                     #Window 'master' is created
image = PhotoImage(file='check_it_off_your_list_7934.gif')
picture = Label(intro, image=image).grid(row=10,column=1)

text = Text(intro)

                                                        #Various labels created which indicate the title, intended user input, and instructions.
Label(intro, text="PriceComparo",bg='Purple',font='Showcard 24 italic underline',relief=SUNKEN).grid(row=0, column=1)
Label(intro, text="Name",background='purple',font='Times 12 bold underline',relief=RIDGE).grid(row=1)
Label(intro, text="Product",background='purple',font='Times 12 bold underline',relief=RIDGE).grid(row=2)
Label(intro, text="Prices",background='purple',font='Times 12 bold underline',relief=RIDGE).grid(row=3)
Label(intro, text="Reviews",background='purple',font='Times 12 bold underline',relief=RIDGE).grid(row=4)
Label(intro, text="Shipping Opts.",background='purple',font='Times 12 bold underline',relief=RIDGE).grid(row=5)
Label(intro, text="The centre\n for product comparisons!",background='Red',font='Times 10 italic bold underline',relief=GROOVE).grid(row=6, column=1)
Label(intro, text="Enter the product details\n, and get a full breakdown\nof your product!\n \nVersion 1.1", background='Red',font='Times 10 bold',relief=GROOVE).grid(column=2, row=3)
Label(intro, text="Ex. Tom/ PS4/395.95,385.85/\n4.7,4.3/3.99,6.78\n",background='Purple',font='Times 10 bold',relief=GROOVE).grid(column=2, row=1)

                                                        #Entry boxes are created and placed on the window grid.
e1 = Entry(intro, width=30)
e2 = Entry(intro, width=30)
e3 = Entry(intro, width=30)
e4 = Entry(intro, width=30)
e5 = Entry(intro, width=30)

                                                        #Entry boxed placed on window grid.
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)

                                                        #Buttons created: 'Quit' destroys window, and 'Sorter' calls in function 'Sorter'
Button(intro, text='Quit',bg="Red",font="Cooper 12 bold underline italic", command=intro.destroy,relief=RAISED).grid(row=6, column=0, sticky=W, pady=4)
Button(intro, text='Sorter',bg="Yellow",font="Cooper 12 bold underline italic", command=Sorter,relief=RAISED).grid(row=6, column=2, sticky=W, pady=4)


intro.geometry('650x600+300+250')                       #Set intro window geometry and mainloop it.
mainloop()





