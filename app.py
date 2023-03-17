from flask import Flask, request, render_template
import re

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def match_regex():
    # Get the test string and regular expression from the form submission
    text_string = request.form['text_string']
    regular_expression = request.form['regular_expression']
    

    # Find all matches in the test string using the regular expression
    matches = re.findall(regular_expression, text_string)

    # Render the results page with the matches
    return render_template('result.html', matches=matches)



if __name__ == '__main__':
    app.run(debug=True)