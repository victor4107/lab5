from flask import Flask
app = Flask(__name__)
from matrix import aaa

@app.route('/')
def hello():
    ar1 = aaa(5)
    return "Hello World! {}".format(ar1)

if __name__ == '__main__':
    f = open("text.txt", "w")
    f.write("content")
    f.close()
    app.run()
#comment
