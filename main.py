import os
import json
import pickle
from github import Github
from textblob import TextBlob
    
def load_classifier():
        # Load the trained classifier
        with open("model.pkl", "rb") as f:
            vectorizer, classifier = pickle.load(f)
        return vectorizer, classifier

# Function to classify an issue using the trained classifier
def get_predicted_emojis(issue, vectorizer, classifier):
    issue_text = issue.title + " " + issue.body
    X_test = vectorizer.transform([issue_text])
    predicted_labels = classifier.predict(X_test)
    return predicted_labels.tolist()

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

def get_keyword_emojis(text):
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
        "typo": ":pencil2:",
        "config": ":gear:",
        "api": ":link:",
        "mobile": ":iphone:",
        "web": ":globe_with_meridians:",
        "build": ":hammer:",
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
        "windows": ":computer:",
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
        "flutter": ":rocket:",
        "docker": ":whale:",
        "aws": ":cloud:",
        "azure": ":cloud:",
        "gcp": ":cloud:",
        "graphql": ":trident:",
        "rest": ":zzz:",
        "oauth": ":key:",
        "redux": ":recycle:",
        "vuex": ":recycle:",
        "angular": ":a:",
        "react": ":atom:",
        "vue": ":leaves:",
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
    
    emojis = []
    for keyword, emoji in keywords.items():
        if keyword in text.lower():
            emojis.append(emoji)

    return emojis

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
        sentiment_label = repo.create_label(sentiment_emoji, "FFFFFF")
    issue.add_to_labels(sentiment_label)
    print(f"Added sentiment label: {sentiment_emoji}")

    # Add keyword labels
    keyword_emojis = get_keyword_emojis(issue.title + " " + issue.body)
    for keyword_emoji in keyword_emojis:
        keyword_label = None
        try:
            keyword_label = repo.get_label(keyword_emoji)
        except:
            keyword_label = repo.create_label(keyword_emoji, "FFFFFF")
        issue.add_to_labels(keyword_label)
        print(f"Added keyword label: {keyword_emoji}") 
 
    
    # Load the trained classifier
    vectorizer, classifier = load_classifier()

    # Classify the issue
    predicted_emojis = get_predicted_emojis(issue, vectorizer, classifier)
    for predicted_emoji in predicted_emojis:
        predicted_label = None
        try:
            predicted_label = repo.get_label(predicted_emoji)
        except:
            predicted_label = repo.create_label(predicted_emoji, "FFFFFF")  # you can change the color as needed
        issue.add_to_labels(predicted_label)
        print(f"Added predicted label: {predicted_emoji}")  # print the added predicted emoji

if __name__ == "__main__":
    main()
