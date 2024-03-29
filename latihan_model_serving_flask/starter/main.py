import json
import numpy as np
import tensorflow as tf
from flask import Flask, request


#================Membuat Web App Sederhana Menggunakan Flask========================
# Your code here
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
#===================================================================================


#============Membuat API Endpoint dalam Web App sebagai Model Serving===============
# Your code here
#===================================================================================



#=============================Menjalankan Web App===================================
# Your code here
#===================================================================================