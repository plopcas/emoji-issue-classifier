import os
import json
from github import Github
from textblob import TextBlob

def get_sentiment_emoji(sentiment_polarity):
    if sentiment_polarity > 0.5:
        return ":grin:"
    elif sentiment_polarity > 0:
        return ":slightly_smiling_face:"
    elif sentiment_polarity == 0:
        return ":neutral_face:"
    elif sentiment_polarity > -0.5:
        return ":slightly_frowning_face:"
    else:
        return ":angry_face:"

def get_keyword_emoji(text):
    keywords = {
        "bug": ":bug:",
        "error": ":warning:",
        "fix": ":wrench:",
        "update": ":arrow_up:",
        "upgrade": ":arrow_double_up:",
        "improvement": ":chart_with_upwards_trend:",
        "performance": ":rocket:",
        "security": ":lock:",
        "crash": ":boom:",
        "data": ":bar_chart:",
        "break": ":hammer:",
        "deprecated": ":no_entry_sign:",
        "document": ":page_facing_up:",
        "feature": ":sparkles:",
        "style": ":art:",
        "test": ":white_check_mark:",
        "translation": ":globe_with_meridians:",
        "refactor": ":recycle:",
        "question": ":question:",
        "discussion": ":speech_balloon:",
        "help": ":raising_hand:",
        "duplicate": ":twisted_rightwards_arrows:",
        "good first issue": ":baby:",
        "enhancement": ":bulb:",
        "invalid": ":x:",
        "wontfix": ":negative_squared_cross_mark:",
        "ui": ":framed_picture:",
        "backend": ":gear:",
        "frontend": ":computer:",
        "design": ":art:",
        "typo": ":pencil:",
        "config": ":wrench:",
        "api": ":link:",
        "mobile": ":iphone:",
        "web": ":globe_with_meridians:",
        "build": ":building_construction:",
        "release": ":rocket:",
        "deploy": ":ship:",
        "success": ":heavy_check_mark:",
        "failure": ":x:",
        "code review": ":eyes:",
        "merge": ":twisted_rightwards_arrows:",
        "commit": ":pushpin:",
        "pull request": ":arrows_counterclockwise:",
        "version": ":bookmark:",
        "hotfix": ":fire:",
        "cleanup": ":broom:",
        "revert": ":leftwards_arrow_with_hook:",
        "database": ":floppy_disk:",
        "server": ":cloud:",
        "client": ":computer:",
        "network": ":globe_with_meridians:",
        "linux": ":penguin:",
        "windows": ":desktop_computer:",
        "mac": ":computer:",
        "ios": ":iphone:",
        "android": ":robot:",
        "javascript": ":javascript:",
        "python": ":snake:",
        "ruby": ":gem:",
        "java": ":coffee:",
        "php": ":elephant:",
        "html": ":html5:",
        "css": ":css3:",
        "sass": ":eyeglasses:",
        "less": ":minus:",
        "json": ":memo:",
        "xml": ":page_with_curl:",
        "markdown": ":pencil2:",
        "typescript": ":typescript:",
        "go": ":gopher:",
        "rust": ":rust:",
        "shell": ":shell:",
        "c": ":desktop_computer:",
        "cplusplus": ":desktop_computer:",
        "csharp": ":desktop_computer:",
        "swift": ":swift:",
        "kotlin": ":kotlin:",
        "flutter": ":flutter:",
        "docker": ":whale:",
        "aws": ":aws:",
        "azure": ":azure:",
        "gcp": ":gcp:",
        "graphql": ":graphql:",
        "rest": ":zzz:",
        "oauth": ":key:",
        "redux": ":recycle:",
        "vuex": ":recycle:",
        "angular": ":a:",
        "react": ":atom_symbol:",
        "vue": ":herb:",
        "svelte": ":mag:",
        "django": ":spider_web:",
        "flask": ":wine_glass:",
        "rails": ":train:",
        "laravel": ":framed_picture:",
        "spring": ":cherry_blossom:",
        "node": ":leaves:",
        "express": ":train2:",
        "nestjs": ":bird:",
        "mongodb": ":leaves:",
        "mysql": ":dolphin:",
        "postgres": ":elephant:",
        "sqlite": ":file_folder:",
        "redis": ":fire:",
        "wordpress": ":capital_abcd:",
        "shopify": ":shopping_cart:",
        "woocommerce": ":shopping_cart:",
        "joomla": ":j:",
        "drupal": ":d:",
         # add more keywords and corresponding emojis as needed
    }
    
    for keyword, emoji in keywords.items():
        if keyword in text.lower():
            return emoji

    return None  # return None if no keyword matches

def main():
    # Setup
    g = Github(os.getenv('GITHUB_TOKEN'))
    repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))

    # Get the issue from the event payload
    with open(os.getenv('GITHUB_EVENT_PATH')) as f:
        event = json.load(f)
    issue_number = event["issue"]["number"]
    issue = repo.get_issue(number=issue_number)

    # Perform sentiment analysis
    blob = TextBlob(issue.title + " " + issue.body)
    sentiment = blob.sentiment

    # Add sentiment label
    sentiment_emoji = get_sentiment_emoji(sentiment.polarity)
    sentiment_label = None
    try:
        sentiment_label = repo.get_label(sentiment_emoji)
    except:
        sentiment_label = repo.create_label(sentiment_emoji, "FFFFFF")  # you can change the color as needed
    issue.add_to_labels(sentiment_label)
    print(f"Added sentiment label: {sentiment_emoji}")  # print the added sentiment emoji

    # Add keyword labels
    keyword_emoji = get_keyword_emoji(issue.title + " " + issue.body)
    if keyword_emoji:
        keyword_label = None
        try:
            keyword_label = repo.get_label(keyword_emoji)
        except:
            keyword_label = repo.create_label(keyword_emoji, "FFFFFF")  # you can change the color as needed
        issue.add_to_labels(keyword_label)
        print(f"Added keyword label: {keyword_emoji}")  # print the added keyword emoji

if __name__ == "__main__":
    main()
