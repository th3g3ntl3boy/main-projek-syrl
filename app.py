from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

k_means = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def hello_world():
    return render_template("index.html")

@app.route("/", methods = ["POST"])
def kmeans():
    vx1 = request.form["x1"]
    vx2 = request.form["x2"]
    vx3 = request.form["x3"]
    wilayah = request.form["var"]
    df= pd.read_csv("Idx_Miskin.csv")
    df1 = df.iloc[:, [1,2,3]].values
    model = k_means.fit(df1)
    testing = [[vx1,vx2,vx3]]
    klasternya = str(model.predict(testing)+1)
    return render_template("index.html", myklaster = klasternya , kabupaten = wilayah)

if __name__ == "__main__":
    app.run(debug=True)