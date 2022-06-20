from flask import Flask, render_template
import bustimes

app = Flask(__name__)

@app.route("/")
def main():
    times = bustimes.available_times()
    result = []
    for time in times:
        result.append({
            "due": time.__repr__(),
            "min_left": int(time.minutes_left())
        })
    return render_template("index.html", closest_time = result[0], other_times=result[1:])

app.run()
