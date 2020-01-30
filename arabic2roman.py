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
    dec = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    result=''
    index = 0
    
    while num > 0:
        for __ in range (num // dec[index]):
            result+=rom[index]
            num -=dec[index]
        index+=1
    return result

print(hello_world())
print(arabic2roman(1))
print("hello")
