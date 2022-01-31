from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

name="Neana Del Rio"
role="Cybersecurity Analyst"
phone="702-813-3048"
email="neanadelrio@gmail.com"
location="Atlanta, GA"


@app.route("/")
def index():
    return render_template("index.html", 
    name=name,
    role=role,
    phone=phone,
    email=email,
    location=location
    )

if __name__ == "__main__":
    app.run(debug=True)