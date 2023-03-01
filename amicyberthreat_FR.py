import re

with open('github_urls.txt', 'r') as f:
    github_urls = [url.strip() for url in f]

with open('mozilla_urls.txt', 'r') as f:
    mozilla_urls = [url.strip() for url in f]

with open('urls_addons_chrome.txt', 'r') as f:
    chrome_addon_urls = [url.strip() for url in f]

with open('urls_twitter.txt', 'r') as f:
    twitter_urls = [url.strip() for url in f]

file_path = input("Veuillez saisir le chemin d'accès à votre fichier texte contenant votre historique de recherche : ")
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
    term = "un chat. Aucune menace détectée."
elif score <= 10:
    term = "novice"
elif score <= 25:
    term = "petit joueur"
elif score <= 50:
    term = "pirate en herbe"
elif score <= 100:
    term = "hacker en devenir"
elif score <= 250:
    term = "hacker confirmé"
elif score <= 500:
    term = "cybercriminel professionnel"
else:
    term = "maître du hacking"

print("Votre score de menace est de :", score)
print("Vous êtes un(e)", term)
