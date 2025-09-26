# 🔒 Password Leak Checker

A simple and secure web application that checks if your password has been exposed in known data breaches using the **Have I Been Pwned (HIBP) API**.  
This tool helps users ensure their passwords are not compromised before using them.

---

## 🚀 Features
- ✅ Check if a password has appeared in data breaches.  
- ✅ Secure lookup using **k-anonymity** (your full password is never sent to the API).  
- ✅ Clear and modern **React frontend**.  
- ✅ **Flask backend** with API integration.  
- ✅ Real-time results with safe/danger alerts.  

---

## 🛠️ Tech Stack
- **Frontend:** React.js (with modern UI/UX design)  
- **Backend:** Flask (Python)  
- **API:** Have I Been Pwned Passwords API  
- **Styling:** CSS (custom responsive design)  

---

## ⚡Installation & Setup
### Backend(Flask)
<pre>cd Backend
pip install -r requirements.txt
python app.py</pre>

### Frontend(React)
- Installing dependencies and start development server
<pre>cd frontend
npm install
npm start</pre>

- To run app in single server(Production) `npm run build` copy the build folder to backend and run `python app.py`
---

## Security note

- Your actual password never sent to server or external API
- Only first 5 characters of the SHA-1 hash are sent to HIBP(K-Anonymity model)
- This ensures maximum privacy and security

---
## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

---
## 🙌 Credits

[Have I Been Pwned API](https://haveibeenpwned.com/API/v3) for the Passwords API
React, Flask, and Open Source community ❤️

---
