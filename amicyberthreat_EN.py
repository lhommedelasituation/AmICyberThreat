import re

with open('github_urls.txt', 'r') as f:
    github_urls = [url.strip() for url in f]

with open('mozilla_urls.txt', 'r') as f:
    mozilla_urls = [url.strip() for url in f]

with open('urls_addons_chrome.txt', 'r') as f:
    chrome_addon_urls = [url.strip() for url in f]

with open('urls_twitter.txt', 'r') as f:
    twitter_urls = [url.strip() for url in f]

file_path = input("Please enter the path to your text file containing your search history: ")

with open(file_path, 'r') as f:
    user_history = f.read()

urls_in_history = re.findall(r'((?:https?:\/\/)?[\w\-\.]+\.\w{2,}(?:\/[\w\.\/]*)*\/?)', user_history)

score = 0

with open('original.txt', 'r') as f:
    urls = [url.strip() for url in f]

for url in urls_in_history:
    if url in urls:
        score += 1
    elif "github.com" in url:
        if any(repo_url in url for repo_url in github_urls):
            score += 5
        else:
            score += 1
    elif "addons.mozilla.org" in url:
        if any(addon_url in url for addon_url in mozilla_urls):
            score += 2.5
        else:
            score += 1
    elif "chrome.google.com" in url:
        if any(addon_url in url for addon_url in chrome_addon_urls):
            score += 2.5
        else:
            score += 1
    elif "twitter.com" in url:
        if any(twitter_url in url for twitter_url in twitter_urls):
            score += 1.5
        else:
            score += 1

if score == 0:
    term = "a cat. No threat detected."
elif score <= 10:
    term = "novice"
elif score <= 25:
    term = "small-time player"
elif score <= 50:
    term = "aspiring hacker"
elif score <= 100:
    term = "up-and-coming hacker"
elif score <= 250:
    term = "experienced hacker"
elif score <= 500:
    term = "professional cybercriminal"
else:
    term = "hacking master"

print("Your threat score is:", score)
print("You are a", term) 
