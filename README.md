
# Compromised Password Checker (Bloom Filter)

## 📚 Overview
This project implements a **Bloom Filter** from scratch to efficiently check whether a password has likely been compromised in a known breach dataset.

Users can enter a password into a simple web form, and the app will check if it exists in a database of breached passwords using a probabilistic Bloom filter structure.

- If found: warns the user that the password might not be safe.
- If not found: reassures the user that the password likely isn't compromised.

---

## 🌐 Live Demo

You can try the app live here: [Bloom Filter Password Checker - Live Demo](https://your-app-name.onrender.com)

---

## 🚀 How to Run the Project

### 1. Install Requirements
Make sure you have Python 3 installed.

Then install Flask:

```bash
pip3 install flask
```

---

### 2. Project Structure

```plaintext
/Compromised-Password-Checker
  |- app.py                 # Flask web server
  |- bloom_filter.py        # Custom Bloom Filter implementation
  |- passwords.txt          # Sample breached password list
  |- templates/
      |- index.html         # Simple web form
  |- README.md              # This file
```

---

### 3. Run the Application
From the project folder, start the Flask server:

```bash
python3 app.py
```

You should see output like this:
```plaintext
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

---

### 4. Use the App
- Open your web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)
- Enter a password in the form
- Click **"Check"**
- See the result!

---

## ⚙️ Technical Details
- **Bloom Filter Size:** 10,000 bits
- **Number of Hash Functions:** 5
- **Hashing Algorithm:** `hashlib.sha256`
- **False Positives:** Possible, but false negatives are impossible.

---

## 🔥 Why a Bloom Filter?
- Fast membership tests even with large datasets.
- Memory-efficient compared to storing every password directly.
- Useful for security applications where checking billions of passwords needs to be lightweight.

---

## 📌 Notes
- The full breached password dataset is too large to upload to GitHub. A small sample list is used here for demonstration purposes.
- The Bloom Filter was built **from scratch** (not using third-party libraries).
- The `hashlib` Python library is used to create multiple independent hash functions based on `sha256`.

