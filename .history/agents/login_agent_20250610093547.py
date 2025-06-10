def guess_platform(text):
    platforms = ['Amazon', 'Flipkart', 'Netflix', 'Hotstar']
    for platform in platforms:
        if platform.lower() in text.lower():
            return platform
    return "Unknown"
def simulate_login(platform, email, password):
    print(f"[SIMULATION] Logging into {platform} with {email} / {password}")
