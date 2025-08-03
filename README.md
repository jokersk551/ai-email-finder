# 🔍 AI Email Finder Tool

This Python tool extracts **publicly visible email addresses** from **live websites**, and also pulls WHOIS information for each domain. Optionally, it supports using an HTTP proxy.

## 🚀 Features

- ✅ Live website scraping
- ✅ Email address extraction using regex
- ✅ WHOIS record lookup (creation, expiry, registrar, contact)
- ✅ Proxy support (HTTP/HTTPS)
- ✅ Command-line user input
- ✅ No config file needed

---
Install requirements.txt

pip install -r requirements.txt

## 📦 Installation

### 1. Clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/ai-email-finder.git
cd ai-email-finder
pip install -r requirements.txt

🚀 How to Use
Run the script from the terminal:
python main.py

🧾 You will be prompted to:
Enter one or more website URLs (comma-separated)
Example:
https://example.com, https://python.org

Use a proxy? (optional)
y
Enter proxy URL
Example:
http://127.0.0.1:8080
```
[+] Extracting emails from https://python.org
[✓] Found: press@python.org
[+] WHOIS Info:
    - Domain: python.org
    - Registrar: Google LLC
    - Country: US
    - Expiry: 2026-03-31

🔐 Ethical Use
This tool only extracts public email addresses.
Use responsibly. Always respect a website's robots.txt, terms, and privacy policies.

👨‍💻 Author
Sahil Koli
Penetration Tester & Ethical Hacker
LinkedIn • GitHub
