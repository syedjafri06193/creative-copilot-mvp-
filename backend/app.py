from flask import Flask, request, jsonify
import tempfile
from analysis import analyze_video

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    ref = request.files["reference"]

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        ref.save(tmp.name)
        ref_stats = analyze_video(tmp.name)

    feedback = (
        f"Reference pacing: {ref_stats['frames']} frames\n"
        f"Average color (BGR): {ref_stats['color']}\n\n"
        "Your edit comparison coming next."
    )

    return jsonify({"feedback": feedback})

if __name__ == "__main__":
    app.run(debug=True)
