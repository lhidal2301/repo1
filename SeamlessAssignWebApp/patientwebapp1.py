import json
from flask import Flask

app = Flask(__name__)
@app.route("/")
def patientpage():
    with open("patient.json") as patientfile:
        data = json.load(patientfile)
        return data

if __name__=="__main__":
    app.run(debug=True, use_reloader=True)
