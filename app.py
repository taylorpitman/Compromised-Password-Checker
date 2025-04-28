from flask import Flask, request, render_template
from bloom_filter import BloomFilter
import os
app = Flask(__name__)

# Create Bloom Filter
bf = BloomFilter(size=10000, hash_count=5)  # Adjusted to match your custom implementation

# Load passwords into Bloom Filter
with open("samplePasswords.txt", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        bf.add(line.strip())

# Define a route for the root URL, supporting both GET and POST methods
@app.route("/", methods=["GET", "POST"])

def index():

    # Initialize an empty message to display to the user
    message = ""
    if request.method == "POST":

        # Check if the request method is POST (form submission)
        password = request.form.get("password")

        # Retrieve the password entered by the user in the form
        if password:

            # Ensure the password is not empty
            if password in bf:

                # Check if the password exists in the Bloom Filter (potentially compromised)
                message = "⚠️ Your password might not be safe! You might want to change it."

            else:
                # Success message for safe passwords
                message = "✅ Your password isn't in our set of compromised passwords!"

    # Render the HTML template and pass the message to it
    return render_template("index.html", message=message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Get the port from Render or default to 10000
    app.run(host="0.0.0.0", port=port)
