from flask import Flask, render_template, request

app = Flask(__name__)

# Converting every input currency to INR, then converting from INR to the required output currency
OTHER_TO_INR = {'USD': 75.57, 'EURO': 85.03, 'GBP': 93.33, 'AUD': 51.91, 'INR': 0.00}
INR_TO_OTHER = {'USD': 0.013, 'EURO': 0.012, 'GBP': 0.011, 'AUD': 0.019, 'INR': 0.00}


def lookup(frm):
    pass

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        currency = INR_TO_OTHER.keys()
        # Sending values for the drop down menu on index.html
        return render_template("index.html", currency = sorted(currency))
    else:
        frm = request.form.get("from")
        to = request.form.get("to")
        amt = request.form.get("amount")

        # Error Handling
        if not frm: 
            return render_template("apology.html", inp = "Select Currency")
        if not to: 
            return render_template("apology.html", inp = "Select Currency")
        if not amt or amt == 0 or isDigit(amt) == False: 
            return render_template("apology.html", inp = "Enter amount")

        # Passing the input values to function "calculate" to find the answer
        ans = calculate(frm, to, float(amt))
        return render_template('index.html', ans = ans, unit = to)


def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def calculate(frm, to, amt):
    # If both the currencies are the same, just output the amount
    if frm == to:
        return amt

    # Converting 
    if to == 'INR':
        return "{:.2f}".format((OTHER_TO_INR[frm] * amt))
    if frm == 'INR':
        return "{:.2f}".format((INR_TO_OTHER[to] * amt))
    in_inr = OTHER_TO_INR[frm] * amt 
    to_ans = INR_TO_OTHER[to] * in_inr

    # Returning the output only upto 2 decimal places
    fin = "{:.2f}".format(to_ans)
    return fin
