# from flask import Flask, render_template, request
# import pickle
# import pandas as pd

# app = Flask(__name__)

# model = pickle.load(open("model.pkl","rb"))

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict():

#     title = request.form["title"]
#     review = request.form["review"]
#     age = int(request.form["age"])
#     rating = int(request.form["rating"])
#     feedback = int(request.form["feedback"])

#     text = title + " " + review

#     data = pd.DataFrame({
#         "text":[text],
#         "Age":[age],
#         "Rating":[rating],
#         "Positive Feedback Count":[feedback]
#     })

#     prediction = model.predict(data)[0]

#     if prediction == 1:
#         result = "Recommended ✅"
#     else:
#         result = "Not Recommended ❌"

#     return render_template("index.html", prediction_text=result)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=10000)

from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    title    = request.form["title"]
    review   = request.form["review"]
    age      = int(request.form["age"])
    rating   = int(request.form["rating"])
    feedback = int(request.form.get("feedback", 0) or 0)

    text = title + " " + review

    data = pd.DataFrame({
        "text":                   [text],
        "Age":                    [age],
        "Rating":                 [rating],
        "Positive Feedback Count":[feedback]
    })

    prediction = model.predict(data)[0]

    if prediction == 1:
        result      = "recommended"
        result_text = "Recommended"
    else:
        result      = "not_recommended"
        result_text = "Not Recommended"

    return render_template("index.html",
                        prediction=result,
                        prediction_text=result_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)