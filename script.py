import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import csv
import time
import argparse





def mode():
    print("----> [1] Social media")
    print("----> [2] Forums")
    choice = input("[+] Choose mode: ")
    return choice










def search_social_media(username):
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Twitter/X": f"https://x.com/{username}",
        "TikTok": f"https://tiktok.com/@{username}",
        "Reddit": f"https://reddit.com/user/{username}",
        "Facebook": f"https://facebook.com/{username}",
        "Pinterest": f"https://pinterest.com/{username}",
        "Twitch": f"https://twitch.tv/{username}",
        "YouTube": f"https://youtube.com/@{username}",
        "Snapchat": f"https://snapchat.com/add/{username}",
        "LinkedIn": f"https://linkedin.com/in/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Telegram": f"https://t.me/{username}",
        "Mastodon (mastodon.social)": f"https://mastodon.social/@{username}",
        "Discord (via lookup, not direct profile)": None,
        "Spotify": f"https://open.spotify.com/user/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "DeviantArt": f"https://{username}.deviantart.com",
    }

    found_sites = []

    for site_name, url in platforms.items():
        if url is None:
            continue
        response = requests.get(url)
        print(site_name, response.status_code, "    Site: ", url)
        if response.status_code == 200:
            found_sites.append({"name": site_name, "url": url})

    return found_sites


def dig_github(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code != 200:
        print("[!] Couldn't reach GitHub API")
        return

    data = response.json()
    print("[+] Name:", data.get("name"))
    print("[+] Bio:", data.get("bio"))
    print("[+] Followers:", data.get("followers"))
    print("[+] Following:", data.get("following"))
    print("[+] Public repos:", data.get("public_repos"))
    print("[+] Location:", data.get("location"))


def dig_social_media(found_sites, username):
    print("[+] Found", len(found_sites), "site(s).")
    for i, site in enumerate(found_sites):
        print(i, "-", site["name"])

    pick = input("[+] Which one do you want to dig into? (number, or 'q' to skip): ")
    if pick.lower() == "q":
        return

    index = int(pick)
    chosen_site = found_sites[index]
    print("[+] Digging into", chosen_site["name"], "-", chosen_site["url"])

    if chosen_site["name"] == "GitHub":
        dig_github(username)
    else:
        print("[!] No deep-dive built yet for this site")














def search_forums(username):
    platforms = {
        "Reddit": f"https://reddit.com/user/{username}",
        "Hacker News": f"https://news.ycombinator.com/user?id={username}",
        "Stack Overflow (search only, no direct URL)": None,
        "XDA Developers": f"https://xdaforums.com/m/{username}",
        "Discourse (Meta forum)": f"https://meta.discourse.org/u/{username}",
        "NeoGAF": f"https://www.neogaf.com/members/?username={username}",
        "ResetEra": f"https://www.resetera.com/members/?username={username}",
        "MyBB demo/generic forums": None,
        "Steam Community (forums use same profile)": f"https://steamcommunity.com/id/{username}",
        "4chan (no accounts, skip)": None,
        "NodeBB (generic, varies per install)": None,
    }

    found_sites = []

    for site_name, url in platforms.items():
        if url is None:
            continue
        response = requests.get(url)
        print(site_name, response.status_code, "    Site: ", url)
        if response.status_code == 200:
            found_sites.append({"name": site_name, "url": url})

    return found_sites









print("[+] Lotus_Scope")
ussrname = input("[+] Enter username: ")
print("[+] Searching", ussrname, "----> Which mode?")
choice = mode()
print("Searching.....")


if choice == "1":
    found = search_social_media(ussrname)
    if found:
        dig_social_media(found, ussrname)
elif choice == "2":
    found = search_forums(ussrname)
    print("[+] Found", len(found), "forum(s).")
else:
    print("[!] Invalid choice")