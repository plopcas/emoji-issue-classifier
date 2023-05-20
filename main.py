import pickle
from textblob import TextBlob
from utils.github_utils import add_label_to_issue, get_github_client, get_github_repo, get_issue_from_event
    
def load_classifier():
        # Load the trained classifier
        with open("training/model.pkl", "rb") as f:
            vectorizer, classifier = pickle.load(f)
        return vectorizer, classifier

# Function to classify an issue using the trained classifier
def get_predicted_emojis(issue_text, vectorizer, classifier):
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
    g = get_github_client()
    repo = get_github_repo(g);

    # Get the issue from the event payload
    issue = get_issue_from_event(repo)
    issue_text = issue.title + " " + str(issue.body)

    # Perform sentiment analysis
    blob = TextBlob(issue_text)
    sentiment = blob.sentiment

    # Add sentiment label
    sentiment_emoji = get_sentiment_emoji(sentiment.polarity)
    add_label_to_issue(issue, sentiment_emoji)

    # Add keyword labels
    keyword_emojis = get_keyword_emojis(issue_text)
    for keyword_emoji in keyword_emojis:
        add_label_to_issue(issue, keyword_emoji)
    
    # Load the trained classifier
    vectorizer, classifier = load_classifier()

    # Classify the issue
    predicted_emojis = get_predicted_emojis(issue_text, vectorizer, classifier)
    for predicted_emoji in predicted_emojis:
        add_label_to_issue(issue, predicted_emoji)

if __name__ == "__main__":
    main()
