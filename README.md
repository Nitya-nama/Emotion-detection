# Emotion Detector Game

An interactive **AI-powered Emotion Detection Web App** built using **Flask**, **Hugging Face Transformers**, and **HTML/CSS/JS**.  
Type a sentence — and the app detects your emotion instantly with emojis and dynamic background colors! 🌈

---

## Features

* Detects emotions like *Joy, Sadness, Anger, Fear, Love, Surprise* * 🎨 Dynamic emoji and background color based on emotion  
* (Optional) Save user emotions using **MongoDB Atlas** * 📊 History page with **Chart.js** visualization  

---

## Tech Stack

* **Frontend:** HTML, CSS, JavaScript  
* **Backend:** Flask (Python)  
* **Machine Learning Model:** Hugging Face – `j-hartmann/emotion-english-distilroberta-base`  
* **Database (Optional):** MongoDB Atlas  

---

## Installation & Setup

1.  Clone the repository  
    ```bash
    git clone [https://github.com/your-username/emotion-detector-game.git](https://github.com/your-username/emotion-detector-game.git)
    cd emotion-detector-game
    ```
2.  Install dependencies
    ```bash
    pip install flask transformers pymongo torch
    ```
3.  (Optional) Set up MongoDB Atlas
    * Create a free **MongoDB Atlas** account
    * Get your connection URI
    * Add it in `app.py` like this (replace the placeholder):
        ```python
        from pymongo import MongoClient
        client = MongoClient("your-mongodb-atlas-uri")
        db = client["emotion_db"]
        ```
4.  Run the app
    ```bash
    python app.py
    ```
5.  Open your browser and visit:

    👉 `http://127.0.0.1:5000`

### Folder Structure
```bash
emotion-detector-game/ │ ├── app.py ├── templates/ │ ├── index.html │ └── history.html ├── static/ │ ├── style.css │ └── script.js └── README.md
```
## Example Usage

| Input | Output | Effect |
| :--- | :--- | :--- |
| `I am really angry at my friend.` | `😠 Anger` | Background color changes to red. |

---

## Future Improvements

* Add voice input for detecting spoken emotion
* Add multilingual support (Hindi, Spanish, etc.)
* Display emotion trends over time using charts

---

## Credits

* Model: Hugging Face – `j-hartmann/emotion-english-distilroberta-base`
* Flask: Pallets Projects
* Chart.js: chartjs.org

---

## License

This project is licensed under the **MIT License**.

<br>

Made with ❤️ by Nitya Nama.
