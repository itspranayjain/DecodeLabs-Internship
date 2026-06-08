from colorama import Fore, Style, init
import re
import time

# Initialize Colorama
init(autoreset=True)

# ==========================
# Banner
# ==========================

def banner():
    print(Fore.GREEN + r"""
██████╗ ██╗  ██╗██╗███████╗██╗  ██╗
██╔══██╗██║  ██║██║██╔════╝██║  ██║
██████╔╝███████║██║███████╗███████║
██╔═══╝ ██╔══██║██║╚════██║██╔══██║
██║     ██║  ██║██║███████║██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝

      PHISHGUARD v1.0
   Threat Detection Utility
""")

# ==========================
# Phishing Keywords
# ==========================

phishing_keywords = [
    "urgent",
    "verify",
    "click here",
    "account suspended",
    "bank",
    "password",
    "login",
    "security alert",
    "limited time",
    "winner",
    "claim now",
    "update account",
    "confirm identity"
]

# ==========================
# Analyzer Function
# ==========================

def analyze_message(message):

    score = 0
    red_flags = []

    message_lower = message.lower()

    # Check phishing keywords
    for keyword in phishing_keywords:

        if keyword in message_lower:
            score += 10
            red_flags.append(
                f"Suspicious keyword detected: '{keyword}'"
            )

    # Check URLs
    urls = re.findall(r'https?://\S+', message)

    if urls:
        score += 20
        red_flags.append(
            "Suspicious URL detected"
        )

    # Urgency Indicators
    urgency_words = [
        "immediately",
        "urgent",
        "now",
        "act fast"
    ]

    for word in urgency_words:

        if word in message_lower:
            score += 10
            red_flags.append(
                f"Urgency tactic detected: '{word}'"
            )

    # Risk Classification
    if score <= 20:
        status = "SAFE"
        color = Fore.GREEN

    elif score <= 50:
        status = "SUSPICIOUS"
        color = Fore.YELLOW

    else:
        status = "PHISHING LIKELY"
        color = Fore.RED

    return score, status, color, red_flags

# ==========================
# Main Program
# ==========================

banner()

print(Fore.CYAN + "Paste the email/message below:\n")

message = input("> ")

print(Fore.BLUE + "\n[*] Scanning Message...")
time.sleep(2)

score, status, color, flags = analyze_message(message)

print(Fore.WHITE + "\n===================================")
print(Fore.MAGENTA + " PHISHGUARD ANALYSIS REPORT")
print(Fore.WHITE + "===================================\n")

print(Fore.CYAN + f"Risk Score: {score}/100")

print(color + f"\nStatus: {status}")

print(Fore.YELLOW + "\nRed Flags Found:")

if flags:
    for flag in flags:
        print(Fore.WHITE + f"✓ {flag}")
else:
    print(Fore.GREEN + "No red flags detected")

print(Fore.CYAN + "\nRecommendation:")

if status == "SAFE":
    print(Fore.GREEN +
          "Message appears safe. Stay cautious.")

elif status == "SUSPICIOUS":
    print(Fore.YELLOW +
          "Verify sender before clicking links.")

else:
    print(Fore.RED +
          "Do NOT click any links. Verify sender independently.")

print(Fore.WHITE + "\n===================================\n")
