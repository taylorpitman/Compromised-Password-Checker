from flask import Flask, request, render_template
from bloom_filter import BloomFilter

app = Flask(__name__)

# Create Bloom Filter
bf = BloomFilter(size=10000, hash_count=5)  # Adjusted to match your custom implementation

# Load passwords into Bloom Filter
with open("samplePasswords.txt", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        bf.add(line.strip())

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        password = request.form.get("password")
        if password:
            if password in bf:
                message = "⚠️ Your password might not be safe! You might want to change it."
            else:
                message = "✅ Your password isn't in our set of compromised passwords!"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
