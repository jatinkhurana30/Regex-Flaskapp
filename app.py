from flask import Flask, render_template, request, redirect, jsonify
from SolvedCodes import Answer2,Answer3

app = Flask(__name__)


@app.route("/gslab/regex", methods = ['GET'])
def index():
    log_list = Answer2.find_answer2()
    return render_template("main.html",log_list = log_list)


@app.route("/gslab/solvequestion4", methods = ['POST'])
def index2():
    input = request.form["input"]
    output_answer4 = Answer3.find_answer3(input)
    log_list = Answer2.find_answer2()
    return render_template("main.html",log_list = log_list,output_answer4 = output_answer4)

if __name__ == "__main__":
    app.run(debug=False,port=80,host='0.0.0.0')