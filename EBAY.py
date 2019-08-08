from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
import tkinter
from tkinter import*

def webScrapeEbay():

    name         =      []
    product      =      []

    nameValues     =   e1.get()
    productValues  =   e2.get()

    name.append(nameValues)
    name1 = (name[0].split(','))
    name1.sort()

    product.append(productValues)
    product1 = (product[0].split(','))
    product1.sort()

    api = finding(appid='TejvirBa-l-PRD-239332c4a-8904990b', config_file=None)
    api_request = { 'keywords': product1[0] }
    response = api.execute('findItemsByKeywords', api_request)
    soup = BeautifulSoup(response.content,'lxml')

    totalentries = int(soup.find('totalentries').text)
    items = soup.find_all('item')

    print()
    print()

    for item in items:
        cat = item.categoryname.string.lower()
        title = item.title.string.lower()
        price = int(round(float(item.currentprice.string)))
        url = item.viewitemurl.string.lower()
        listingtype = item.listingtype.string.lower()
        condition = item.conditiondisplayname.string.lower()

        print(name[0],', here are the details on a',product[0],'from Ebay.com')
        print('\n')
        print('Product Category:\n' + cat + '\n')
        print('Product Title:\n' + title + '\n')
        print('Product Price:\n' + 'USD' + ' ' + str(price) + '\n')
        print('Product URL:\n' + url + '\n')
        print('Product Listing Type:\n' + listingtype + '\n')
        print('Product Condition:\n' + condition + '\n')
        print('------------------------------------------------------------------')



intro = Tk()
intro.title("Ebay Web Scrapper")
intro.configure(background='Yellow')                     #Window 'master' is created
image = PhotoImage(file='giphy.gif')
picture = Label(intro, image=image).grid(row=10,column=1)

text = Text(intro)

                                                        #Various labels created which indicate the title, intended user input, and instructions.
Label(intro, text="EbayWebScrappo",bg='Blue',font='Showcard 24 italic underline',relief=SUNKEN).grid(row=0, column=1)
Label(intro, text="Name",background='purple',font='Times 12 bold underline',relief=RIDGE).grid(row=1)
Label(intro, text="Product Keywords",background='purple',font='Times 12 bold underline',relief=RIDGE).grid(row=2)


                                                        #Entry boxes are created and placed on the window grid.
e1 = Entry(intro, width=30)
e2 = Entry(intro, width=30)


                                                        #Entry boxed placed on window grid.
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)


                                                        #Buttons created: 'Quit' destorys window, and 'Sorter' calls in function 'Sorter'
Button(intro, text='Quit',bg="Red",font="Cooper 12 bold underline italic", command=intro.destroy,relief=RAISED).grid(row=6, column=0, sticky=W, pady=4)
Button(intro, text='Results',bg="Green",font="Cooper 12 bold underline italic", command=webScrapeEbay,relief=RAISED).grid(row=6, column=2, sticky=W, pady=4)

intro.geometry('605x450+300+250')
intro.mainloop()




