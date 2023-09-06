from flask import Flask,jsonify


app=Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message":"running status 200"}),200
@app.route("/about")
def home():
    return jsonify({"message":"about hello hellol"}),200

if __name__=='__main__':
    app.run()