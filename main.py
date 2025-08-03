import requests
from bs4 import BeautifulSoup
import re
import tldextract
import whois
from datetime import datetime

EMAIL_REGEX = r"[\w\.-]+@[\w\.-]+\.\w+"

# 1. WHOIS data fetcher
def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return {
            "registrar": w.registrar,
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date),
            "country": w.country,
            "whois_email": w.emails if isinstance(w.emails, str) else ', '.join(w.emails or [])
        }
    except Exception:
        return {
            "registrar": None,
            "creation_date": None,
            "expiration_date": None,
            "country": None,
            "whois_email": None
        }

# 2. Email extraction from one URL
def extract_emails(url, proxies=None):
    try:
        print(f"\n[+] Visiting: {url}")
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10, proxies=proxies)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        emails = re.findall(EMAIL_REGEX, text)

        domain = tldextract.extract(url).registered_domain
        whois_info = get_whois_info(domain)

        unique_emails = set(emails)
        if not unique_emails:
            print("[-] No emails found.")
        for email in unique_emails:
            print(f"\n📧 Email Found: {email}")
            print(f"🌐 Source URL: {url}")
            print(f"🗓 Date: {datetime.now().isoformat()}")
            print(f"🔍 WHOIS Domain: {domain}")
            print(f"    Registrar: {whois_info['registrar']}")
            print(f"    Created: {whois_info['creation_date']}")
            print(f"    Expires: {whois_info['expiration_date']}")
            print(f"    Country: {whois_info['country']}")
            print(f"    WHOIS Email: {whois_info['whois_email']}")
    except Exception as e:
        print(f"[!] Error processing {url}: {e}")

# 3. User input and proxy setup
def main():
    print("=== AI Live Email Finder Tool (with Proxy + WHOIS) ===")

    # User input for websites
    url_input = input("Enter website URLs (comma separated):\n> ")
    urls = [u.strip() for u in url_input.split(",") if u.strip()]

    # Optional proxy input
    use_proxy = input("Do you want to use a proxy? (y/n): ").lower()
    proxies = None
    if use_proxy == 'y':
        proxy_ip = input("Enter proxy IP (e.g. http://127.0.0.1:8080):\n> ").strip()
        proxies = {
            "http": proxy_ip,
            "https": proxy_ip
        }

    for url in urls:
        if not url.startswith("http"):
            url = "http://" + url
        extract_emails(url, proxies)

if __name__ == "__main__":
    main()
