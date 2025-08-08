from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model components
model = joblib.load("model/svm_model.pkl")
scaler = joblib.load("model/scaler.pkl")
le = joblib.load("model/label_encoder.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        try:
            features = [float(request.form[f]) for f in [
                "tBodyAcc-mean()-X", "tBodyAcc-mean()-Y", "tBodyAcc-mean()-Z",
                "tBodyAcc-std()-X", "tBodyAcc-std()-Y", "tBodyAcc-std()-Z",
                "tBodyAcc-mad()-X", "tBodyAcc-mad()-Y", "tBodyAcc-max()-X",
                "tBodyAcc-min()-X", "tBodyAcc-energy()-X", "tBodyAcc-iqr()-X"
            ]]
            input_scaled = scaler.transform([features])
            pred = model.predict(input_scaled)
            prediction = le.inverse_transform(pred)[0]
        except:
            prediction = "Invalid input. Please enter all 12 values correctly."
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
