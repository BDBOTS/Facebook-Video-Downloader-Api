import requests
from urllib.parse import quote
import textwrap

# Constants
API_URL = "https://fb.bdbots.xyz/dl?url="
BANNER = """
  ____  _____  ____   ____ _______ _____ 
 |  _ \|  __ \|  _ \ / __ \__   __/ ____|
 | |_) | |  | | |_) | |  | | | | | (___  
 |  _ <| |  | |  _ <| |  | | | |  \___ \ 
 | |_) | |__| | |_) | |__| | | |  ____) |
 |____/|_____/|____/ \____/  |_| |_____/ 
                                         
                                                                                                   
"""

def print_centered(text, width=70):
    """Print centered text with borders"""
    print("║" + text.center(width) + "║")

def print_header():
    """Print the header banner"""
    print("\033[1;36m" + BANNER + "\033[0m")
    print_centered("Facebook Video Downloader API Client")
    print_centered("")
    print_centered("\033[1;33mAn Open Source Project By BDBOTS\033[0m")
    print_centered("GitHub: https://github.com/bdBOTS")
    print_centered("Telegram: @BDBOTS")
    print("╚" + "═" * 70 + "╝")
    print()

def get_video_info(url):
    """Fetch video info from API"""
    try:
        response = requests.get(API_URL + quote(url), timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"\n\033[1;31mError: {str(e)}\033[0m")
        return None

def print_result(data):
    """Print the API response in a formatted way"""
    if not data or data.get("status") != "success":
        error_msg = data.get("message", "Unknown error occurred") if data else "No data received"
        print(f"\n\033[1;31mError: {error_msg}\033[0m")
        if data and "solution" in data:
            print(f"\n\033[1;33mSolution: {data['solution']}\033[0m")
        return

    print(f"\n\033[1;32m✅ Video: {data['title']}\033[0m")
    print("\033[1;34m" + "━" * 70 + "\033[0m")

    for quality in data["downloads"]:
        print(f"\n\033[1;33m🎞️ {quality['quality']} Quality ({quality['size']})\033[0m")
        print(f"\033[1;36m🔗 {quality['url']}\033[0m")

    print("\n\033[1;34m" + "━" * 70 + "\033[0m")
    print("\033[1;35mTip: Right-click links to download or use download managers\033[0m")

def main():
    """Main function"""
    print_header()

    while True:
        print("\n\033[1;34mEnter Facebook Video URL (or 'q' to quit):\033[0m")
        url = input("\033[1;36m➤ \033[0m").strip()

        if url.lower() == 'q':
            break

        if not url:
            print("\033[1;31mPlease enter a valid URL\033[0m")
            continue

        print("\n\033[1;33mFetching video info...\033[0m")
        result = get_video_info(url)
        print_result(result)

        print("\n\033[1;35m" + "═" * 70 + "\033[0m")

    print("\n\033[1;33mThank you for using BDBOTS Facebook Video Downloader!\033[0m")
    print("\033[1;36mVisit https://github.com/bdBOTS for more projects\033[0m")

if __name__ == "__main__":
    main()
