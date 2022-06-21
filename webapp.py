from flask import Flask, render_template
import bustimes

app = Flask(__name__)

def get_bus_times():
    times = bustimes.available_times()
    result = []
    if len(times) > 0:
        for time in times:
            result.append({
                "due": time.__repr__(),
                "min_left": int(time.minutes_left())
            })
    else:
        result.append({
            "due": "No Buses For Today",
            "min_left": "N/A"
        })
    
    return result

@app.route("/")
def main():
    result = get_bus_times()
    return render_template("index.html", closest_time = result[0], other_times=result[1:])

app.run(host="0.0.0.0", port="80")
