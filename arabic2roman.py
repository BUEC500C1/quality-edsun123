from flask import Flask
import pytest
#app = Flask(__name__)
#
#@app.route("/")
def hello_world():
    return "Hello World!"
        
#if __name__ == "__main__":
#    app.run()
    
    
def arabic2roman(num):
    
    if(isinstance(num,int)!=True):
        print("bad input")
        return False
    #an array of numbers up to 1000
    dec = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    # an array of roman numerals
    rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    
    #initialize empty string
    result=''
    
    #keeps track of index
    index = 0
    
    #as long number is greater than 0, we conduct a for loop that  
    #depending on the index, we add to the resulting string with rom[index] and subtract from num wih dec[index]
    #then increments by 1
    while num > 0:
        for __ in range (num // dec[index]):
            result+=rom[index]
            num -=dec[index]
        index+=1
    # returns result string
    return result
