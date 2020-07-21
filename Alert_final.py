
from twilio.rest import Client 
import requests
from bs4 import BeautifulSoup
from pygame import mixer
import datetime

'''
This is a program created by Aiyaz on 20/07/2020 which fetches required stock prices from yahoo finance website and if meats certain condition it will send sms to your number
'''

def stockprice(stockname):
    '''
    This is a function which fetches stock price from yahoo wesite and takes stock code name as a required input
    #1 The url is splited in a way we can acces any stock through the same url
    #2 It requires --(requests)-- module, The requests module gets the data from the given website that is yahoo and converts it into text
    #3 Then the beautifulsoup module is used to convert that text(recieved from requests) to an python readable format which from html or xhtml
    #4 Then by using find_all we can find a certian div and then a class in that div and than the required span with contains the stock price
    #5 and than by appying .text at the end we get the extact live stockprice only then it will return that stock price
    #6 "replace" is used for 4 and more digit prices because they contain "," in them so it can't be converted to float
    '''

    url = "https://in.finance.yahoo.com/quote/"+stockname+".NS?p="+stockname+".NS&.tsrc=fin-tre-srch"

    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text , 'lxml')

    price0 = soup.find_all("div", {"class":"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find("span").text
    price0 = price0.replace(",","")
    price0 = float(price0)
    # print(f"[{datetime.datetime.now()}]  {price0}") #This is to check that it is working or not by continuously printing prices with time
    return price0
        

def sms(stockname , level):
    '''
    #1 This is a function which i got from (https://www.twilio.com/console) a company which allows us to send sms on the given mobile number.
    #2 This function requires ---(from twilio.rest import Client)--- 
    #3 This function requires some informations like  account_sid,auth_token which we will get from that same website
    #4 Now you can edit the body and give your number than it will send that msg to your number if function executed
    #5 The requied position in this funcitons are only for the body of the msg 
    '''
    account_sid = 'ACf6e7a923569e9fc634867ccfb54ed50d'
    auth_token = '3da6d0e4e0962799c84309dce6a9fcfd'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body= f"{stockname} has crossed the level of rs.{level}",
                        from_='+12019755266',
                        to='+918104357733'
                    )


def musicalert(file):
    '''
    This fuction is for the music alarm then the desired contion is satisfied it imports mixer from pygame
    '''
    a = 0
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(4)
    if a== 1:
        mixer.music.stop()


def greaterthanalert(stockname,level):
    '''
    #1 This function requires name of the stock and level of the stock crossing above which the program will be executed
    #2 if the required level is crossed upward the sms function will get executed and alert music will play
    #3 By the use of a dictionary I have limited the sms function to run only for once
    #4 I have also used with open function with "a" to append the txt file to save the executed calls
    '''
    if item == stockname:
        if price >= level:
            if dict[item] == False:
                musicalert("alert.mp3")
                sms(item , level)
                with open("share_market.txt", "a") as f:
                    f.write(f"{stockname} has broken up {level} at [{datetime.datetime.now()}]\n")
                    print(f"Done call for {stockname}")
                    dict[item] = True


def lessthanalert(stockname,level):
    '''
    Same as greaterthanalert function but opposite
    '''
    if item == stockname:
        if price <= level:
            if dict[item] == False:
                musicalert("alert.mp3")
                sms(item , level)
                with open("share_market.txt", "a") as f:
                    f.write(f"{stockname} has broken down {level} at [{datetime.datetime.now()}]\n")
                    print(f"Done call for {stockname}")
                    dict[item] = True

 
if __name__ == "__main__":

    name_of_stocks = ["TITAN","KOTAKBANK","IBULHSGFIN","COALINDIA"]
    dict ={}
    file = "Share_alert.txt"
    for item in name_of_stocks:
        dict[item]= False
    
    print("                 WELCOME\n         Your alert for stocks is on...")

    '''
    #1 name_of_stocks takes the stock code name which is to be tracked
    #2 dict is an empty dictionary which is filled by the for loop with the given stock name as false(stockname:False)
    #3 The below while loop will continue to run the program till its stopped manually or pc is closed it contains stockprice functions (1st func above) to get the live price
    #4 Than the function contaning conditions will execute continously and if the sms is executed the stockname in dictionary will become True (stockname:True)and the loop for that stock will stop 
    '''
    while True:

        for item in name_of_stocks:
            try:
                price = stockprice(item)
                greaterthanalert("TITAN" , 1021)
                greaterthanalert("KOTAKBANK",1364)
                greaterthanalert("IBULHSGFIN" , 241)
                greaterthanalert("COALINDIA" , 139.6)

            except:
                continue

