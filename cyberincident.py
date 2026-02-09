cybersecurity_incidents = [
    "The Morris Worm disrupted computers in 1988, one of the first computer worms distributed via the internet.",
    "In 2007, Estonia suffered a massive DDoS attack that crippled the nation's digital infrastructure.",
    "In 2013, Target experienced a major data breach where millions of credit card details were stolen.",
    "The WannaCry ransomware attack in 2017 affected thousands of computers globally, encrypting data and demanding ransom.",
    "A phishing attack in 2016 compromised the email accounts of several high-profile figures, leading to the release of sensitive information.",
    "The Mirai botnet in 2016 launched DDoS attacks using IoT devices, bringing down large parts of the internet."
]

# Dictionary to categorize incidents
categories = {"virus": [], "phishing": [], "DDoS": [], "ransomware": [], "data breach": []}

# Categorize incidents
for incident in cybersecurity_incidents:
    for category in categories:
        if category in incident.lower():
            categories[category].append(incident)

# Print summary
for category, incidents in categories.items():
    print(f"\nCategory: {category.capitalize()}")
    print("\n".join(incidents) if incidents else "No incidents in this category.")
