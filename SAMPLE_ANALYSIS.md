# Sample Phishing Email Analysis


## Test Case 1: Fake Bank Email
**Input Email:**
From: security@bankofindia-secure.com
Subject: URGENT: Account Suspended in 24 Hours
Body: Dear Customer, Verify your account now. Enter OTP to avoid suspension.
Link: http://bit.ly/verify-bank

**Tool Output:**
```[ANALYZING EMAIL...]
 Fake-looking domain : Possible impersonation
 Urgent language : Pressure to act fast
 Request for OTP/Password : Credential theft attempt
 URL Shortener : Hides real destination
 External link : Verify before clicking

RISK LEVEL: HIGH RISK - DO NOT CLICK[X]```
**Final Result: HIGH RISK**

---
## Test Case 2: Fake Paytm KYC
**Input Email:**
From: support@paytm-kyc-verify.in
Subject: KYC Pending - Action Required
Body: Your wallet will be blocked. Submit Aadhar and OTP to continue.
Link: http://paytm-kyc-verify.in

**Tool Output:**
```[ANALYZING EMAIL...]
 Fake-looking domain : Possible impersonation
 Request for OTP/Password : Credential theft attempt
 External link : Verify before clicking

RISK LEVEL: HIGH RISK - DO NOT CLICK[X]```
**Final Result: HIGH RISK**

---
## Test Case 3: Fake Google Alert
**Input Email:**
From: noreply@google-security-team.com
Subject: Unusual Login Detected
Body: New device login from Meerut. Verify password immediately to secure account.
Link: http://googIe.com/security

**Tool Output:**
```[ANALYZING EMAIL...]
 Fake-looking domain : Possible impersonation
 Urgent language : Pressure to act fast
 Request for OTP/Password : Credential theft attempt
 External link : Verify before clicking

RISK LEVEL: HIGH RISK - DO NOT CLICK[X]```
**Final Result: HIGH RISK**

---
## Conclusion
This tool successfully detects common phishing indicators like fake domains, urgent language, and credential theft attempts.
