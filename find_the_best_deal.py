#***This is a sample program for using RxPY to find and buy the best deal (cheapest iphonex)***


#First install RxPY by using pip install rx

#import Rx module
from rx import Observable , Observer

#create an observer class to observe the process
class myObserver(Observer):
    def on_next(x):
        print("Received an order to buy phone from :",x)
    def on_error(e):
        print("error! seller has no name but phone price is :",e)
    def on_completed():
        print("Find the best deal Completed")

#demo data
bestDeal = [
    {'iphonex': "", "price": 100},
    {'iphonex': "phanit", "price": 1200},
    {'iphonex': "leo", "price": 700},
    {'iphonex': "socheata" ,"price": 670}
]
def get_the_deal(observer):
    for phone in bestDeal:
        if(phone['iphonex'] == "" and phone['price']<=700):
            myObserver.on_error(phone['price'])
        elif (phone['price'] <= 700):
            myObserver.on_next(phone['iphonex'])
    myObserver.on_completed()

s = Observable.create(get_the_deal)
#subscribe mathod take an observer and is handling on_next , on_error , on_completed
s.subscribe(myObserver)

