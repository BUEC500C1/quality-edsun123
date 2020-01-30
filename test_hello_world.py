from flask import Flask
import pytest
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"
        
if __name__ == "__main__":
    app.run()
    
def test_hello_world():
    assert hello_world() == "Hello World!"
