from flask import Flask
import pytest
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"
        
if __name__ == "__main__":
    app.run()
    
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
    
def test_hello_world():
    assert hello_world() == "Hello World!"
    
def test_arabic2roman():
    assert arabic2roman(1) == "I"
    
def test_arabic2roman2():
    assert arabic2roman(4000) == "MMMM"
    
def test_arabic2roman3():
    assert arabic2roman(10) == "x"

def test_arabic2roman4():
    assert arabic2roman(2) == "II"
    
def test_arabic2roman5():
    assert arabic2roman(3) == "III"

def test_arabic2roman6():
    assert arabic2roman(5) == "V"
 
def test_arabic2roman7():
    assert arabic2roman(4) == "IV"
    
def test_arabic2roman8():
    assert arabic2roman(6) == "VI"
    
def test_arabic2roman9():
    assert arabic2roman(25) == "XXV"
    
def test_arabic2roman10():
    assert arabic2roman(50) == "L"
    
def test_arabic2roman11():
    assert arabic2roman(100) == "C"
    
def test_arabic2roman12():
    assert arabic2roman(11) == "XI"

def test_arabic2roman13():
    assert arabic2roman(12) == "XII"
    
def test_arabic2roman14():
    assert arabic2roman(9) == "IX"
    
def test_arabic2roman15():
    assert arabic2roman(8) == "VIII"
