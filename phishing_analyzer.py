# phishing_analyzer.py - DecodeLabs Project 3
# Phishing Awareness Analysis Tool

def analyze_email():
    print("="*50)
    print(" PHISHING AWARENESS ANALYZER v1.0")
    print("="*50)

    sender = input("Enter Sender Email: ").lower()
    subject = input("Enter Subject: ").lower()
    body = input("Enter Email Body: ").lower()
    link = input("Enter Any Link in Email: ").lower()

    red_flags = []
    risk_score = 0

    # 1. Fake Domain Check
    fake_indicators = ["-secure", "-verify", "support-", "google", "facebook"]
    if any(d in sender for d in fake_indicators):
        red_flags.append(("Fake-looking domain", "Possible impersonation"))
        risk_score += 3

    # 2. Urgent Language
    urgent_words = ["urgent", "suspended", "verify now", "24 hours", "blocked", "immediately"]
    if any(w in subject or w in body for w in urgent_words):
        red_flags.append(("Urgent language", "Pressure to act fast"))
        risk_score += 3

    # 3. Credential Request
    cred_words = ["otp", "password", "kyc", "verify account", "aadhar", "pan"]
    if any(w in body for w in cred_words):
        red_flags.append(("Request for OTP/Password", "Credential theft attempt"))
        risk_score += 4

    # 4. Suspicious Link
    if "bit.ly" in link or "tinyurl" in link:
        red_flags.append(("URL Shortener", "Hides real destination"))
        risk_score += 2
    if "http" in link or ".in" in link or ".com" in link:
        red_flags.append(("External link", "Verify before clicking"))
        risk_score += 1

    # Risk Level
    if risk_score >= 8: level = "HIGH RISK - DO NOT CLICK"
    elif risk_score >= 4: level = "MEDIUM RISK - BE CAREFUL"
    else: level = "LOW RISK"

    # Output
    print("\n" + "="*50)
    print(" ANALYSIS REPORT")
    print("="*50)

    if not red_flags:
        print("No major red flags found.")
    else:
        for flag, reason in red_flags:
            print(f"[X] {flag} : {reason}")

    print("-"*50)
    print(f"RISK LEVEL: {level}")
    print("="*50)
    print("Recommendation: Never share OTP/Password. Verify with official website.")

if __name__ == "__main__":
    analyze_email()
