from flask import Flask, render_template, request

app = Flask(__name__)

OTHER_TO_INR = {'USD': 75.57, 'EURO': 85.03, 'GBP': 93.33, 'AUD': 51.91, 'INR': 0.00}
INR_TO_OTHER = {'USD': 0.013, 'EURO': 0.012, 'GBP': 0.011, 'AUD': 0.019, 'INR': 0.00}

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        currency = INR_TO_OTHER.keys()
        return render_template("index.html", currency = sorted(currency))
    else:
        frm = request.form.get("from")
        if not frm: 
            return render_template("apology.html", inp = "Select Currency")
        to = request.form.get("to")
        if not to: 
            return render_template("apology.html", inp = "Select Currency")
        amt = request.form.get("amount")
        if not amt or amt == 0: 
            return render_template("apology.html", inp = "Enter amount")
        ans = calculate(frm, to, float(amt))
        # return render_template('output.html', ans = ans, unit = to )
        return render_template('index.html', ans = ans, unit = to)

def calculate(frm, to, amt):
    if frm == to:
        return amt
    if to == 'INR':
        return "{:.2f}".format((OTHER_TO_INR[frm] * amt))
    if frm == 'INR':
        return "{:.2f}".format((INR_TO_OTHER[to] * amt))
    in_inr = OTHER_TO_INR[frm] * amt 
    to_ans = INR_TO_OTHER[to] * in_inr
    fin = "{:.2f}".format(to_ans)
    return fin
