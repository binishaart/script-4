from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Example script elements
camera_angles = ["Close-up", "Wide shot", "Over-the-shoulder", "Bird's eye view", "Tracking shot"]

@app.route('/', methods=['GET', 'POST'])
def index():
    script = None
    if request.method == 'POST':
        mood = request.form.get('mood', 'Neutral')
        # Generate a simple professional script
        characters = ["Alice", "Bob", "Detective"]
        lines = [
            f"{random.choice(characters)}: '{mood} situation unfolds.'",
            f"{random.choice(characters)}: 'We need to act fast!'",
            f"{random.choice(characters)}: 'What was that sound?'"
        ]
        angles = [f"{random.choice(camera_angles)}" for _ in lines]
        script = "\n".join([f"{angle} - {line}" for angle, line in zip(angles, lines)])
    return render_template("index.html", script=script)

if __name__ == '__main__':
    app.run(debug=True)
