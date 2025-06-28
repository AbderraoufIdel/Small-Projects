---

```markdown
# 🗂️ Topic Tracker App

A simple Python app that manages user-input topics across different platforms.  
It checks if a topic is already stored in `data.json` under each platform, lets the user remove or add it interactively, and saves the updated data back to the file.

---

## 🚀 Features

- Accepts user input for a topic
- Checks if the topic exists under any platform
- Allows removing existing topics
- Allows adding new topics to any platform
- Automatically updates the `data.json` file

---

## 📁 Project Structure

```

📦 your-project/
┣ 📄 main.py
┣ 📄 data.json
┗ 📄 README.md

````

---

## 🧠 How It Works

1. Loads `data.json` as a dictionary with platform names as keys and topic lists as values.
2. Prompts the user to input a topic.
3. Iterates over each platform to:
   - Check if the topic is already listed.
   - Prompt to remove it (if found) or add it (if not found).
4. Saves the updated data back to `data.json`.

---

## 📝 Example `data.json`

```json
{
    "twitter": ["ai", "python"],
    "instagram": ["fitness", "cooking"]
}
````

---

## 📦 Usage

```bash
python checkit.py
```

You will be prompted with questions like:

```
What is the topic?
Do you wanna remove it? (yes or no)
Do you wanna add it to platform? (yes or no)
```

---

## 🔧 Requirements

* Python 3.6+
* A `data.json` file in the same directory

---

## 📌 Notes

* Make sure `data.json` is properly formatted JSON before running.
* Topics are automatically converted to lowercase for consistency.

---

## 🧑‍💻 Author

Abderraouf Idel

---

## 📜 License

This project is open source and free to use.

```
