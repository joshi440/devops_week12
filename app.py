
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def registration():
    return render_template("registration.html")


@app.route("/register", methods=["POST"])
def submit_registration():
    student_name = request.form.get("student_name", "").strip()
    roll_number = request.form.get("roll_number", "").strip()

    if not student_name or not roll_number:
        return render_template(
            "registration.html",
            error="Student name and roll number are required."
        ), 400

    return render_template(
        "registrationsuccess.html",
        student_name=student_name,
        roll_number=roll_number
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
