#Scrape http://news.curtin.edu.au/events/parkd-curtin/ to get details of what food trucks are in Tech Park today.

#
# Imports
#
from lxml import html # For dealing with HTML
import requests # For getting the page
import time # Get date

#
# Constants
#

#Page to request
Site = "http://news.curtin.edu.au/events/parkd-curtin/"
Area = "Tech Park"
#Area = "Hexagon" #Can be useful to test multiple truck conditions

#
# Scrape
#


def get_Date_Ref (Page_Tree, Date_Today):

    Truck_Dates = {
    "Date1" : Page_Tree.xpath('//*[@id="post-14399"]/div/h2[1]/text()')[0],
    "Date2" : Page_Tree.xpath('//*[@id="post-14399"]/div/h2[2]/text()')[0],
    "Date3" : Page_Tree.xpath('//*[@id="post-14399"]/div/h2[3]/text()')[0],
    "Date4" : Page_Tree.xpath('//*[@id="post-14399"]/div/h2[4]/text()')[0],
    "Date5" : Page_Tree.xpath('//*[@id="post-14399"]/div/h2[5]/text()')[0]
    }

    for Date_Ref, Date_Truck in Truck_Dates.items():
        if Date_Truck == Date_Today:
            return(Date_Ref)


def get_Truck_Data_Full (Date_Ref):
    if Date_Ref == 'Date1':
        return('//*[@id="post-14399"]/div/ul[1]/')
    elif Date_Ref == 'Date2':
        return('//*[@id="post-14399"]/div/ul[2]/')
    elif Date_Ref == 'Date3':
        return('//*[@id="post-14399"]/div/ul[3]/')
    elif Date_Ref == 'Date4':
        return('//*[@id="post-14399"]/div/ul[4]/')
    elif Date_Ref == 'Date5':
        return('//*[@id="post-14399"]/div/ul[5]/')
    else:
        return(null)


def get_Tech_Park(Page_Tree, Truck_Data, Area):
    for li_Numb in range(1,20):
        Line_Path = Truck_Data + "li[" + str(li_Numb) + "]/text()"
        try:
            Data_Line = Page_Tree.xpath(Line_Path)[0]
            if Area in Data_Line:
                Data_Line = Data_Line.split('–')
                return(Data_Line[1])
        except IndexError:
            return(null)
            break


def get_Truck_Website(Page_Tree):
    Truck_Websites = dict()
    for Line_Numb in range(1,50):
        Line_Text = '//*[@id="post-14399"]/div/p[9]/a[' + str(Line_Numb) + ']/text()'
        Line_URL = '//*[@id="post-14399"]/div/p[9]/a[' + str(Line_Numb) + ']/@href'
        try:
            Name = Page_Tree.xpath(Line_Text)[0]
            URL = Page_Tree.xpath(Line_URL)[0]
            Truck_Websites[Name] = URL
        except IndexError:
            return(Truck_Websites)
            break        


def Tech_Park_Trucks_With_URL (Truck_Websites, Tech_Park_Trucks):
    Tech_Park_Trucks_With_URL = dict()
    for Truck in Tech_Park_Trucks.split(','):
        for Website_Key in Truck_Websites:
            if Website_Key in Truck:
                Tech_Park_Trucks_With_URL[Truck] = Truck_Websites.get(Website_Key)
    return(Tech_Park_Trucks_With_URL)


def main ():
    #Get Page and convert
    Page = requests.get(Site)
    Page_Tree = html.fromstring(Page.content)

    #Match todays date against page and match ref in dict
    Date_Ref = get_Date_Ref(Page_Tree, time.strftime("%A %d %B"))

    #Get all Trucks for today
    Truck_Data = get_Truck_Data_Full(Date_Ref)

    #Get Tech Park truccks for today
    Tech_Park_Trucks = get_Tech_Park(Page_Tree, Truck_Data, Area)

    #Get Dict with all possible trucks and their websites
    Truck_Websites = get_Truck_Website(Page_Tree)

    #Match Trucks to URL's
    Todays_Trucks_With_Urls = Tech_Park_Trucks_With_URL(Truck_Websites, Tech_Park_Trucks)

    #Print end result if run on it's own
    if __name__ == "__main__":
        print(Todays_Trucks_With_Urls)

    #Returns Dict
    return(Todays_Trucks_With_Urls)


if __name__ == "__main__":
    main()