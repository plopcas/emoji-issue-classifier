from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
from nltk.corpus import wordnet

# Function to perform synonym replacement
def synonym_replacement(text):
    augmented_text = []
    for word in text.split():
        synonyms = wordnet.synsets(word)
        if synonyms:
            augmented_text.append(synonyms[0].lemmas()[0].name())
        else:
            augmented_text.append(word)
    return ' '.join(augmented_text)

# Function to perform data augmentation
def augment_data(X, y):
    augmented_X = []
    augmented_y = []
    for i in range(len(X)):
        augmented_X.append(X[i])
        augmented_y.append(y[i])
        
        augmented_text = synonym_replacement(X[i])
        augmented_X.append(augmented_text)
        augmented_y.append(y[i])
        
        # Apply other augmentation techniques as needed
        
    return augmented_X, augmented_y

# Define your labeled training data
labeled_data = [
    ("This is a bug report.", ":bug:"),
    ("Please fix this issue.", ":wrench:"),
    ("Add a new feature.", ":sparkles:"),
    ("Improve performance.", ":chart_with_upwards_trend:"),
    ("Security vulnerability.", ":lock:"),
    ("Crash on startup.", ":boom:"),
    ("Data analysis required.", ":bar_chart:"),
    ("Design update needed.", ":art:"),
    ("Documentation request.", ":page_facing_up:"),
    ("Error in the code.", ":warning:"),
    ("Translation needed.", ":globe_with_meridians:"),
    ("UI layout issue.", ":framed_picture:"),
    ("Backend API problem.", ":gear:"),
    ("Frontend rendering bug.", ":computer:"),
    ("Question regarding usage.", ":question:"),
    ("Discussion on future features.", ":speech_balloon:"),
    ("Help needed with a task.", ":raising_hand:"),
    ("Duplicate issue.", ":twisted_rightwards_arrows:"),
    ("Good first issue for newcomers.", ":baby:"),
    ("Enhancement suggestion.", ":bulb:"),
    ("Invalid behavior.", ":x:"),
    ("Will not fix this issue.", ":negative_squared_cross_mark:"),
    ("Configuration error.", ":wrench:"),
    ("Mobile app issue.", ":iphone:"),
    ("Web compatibility issue.", ":globe_with_meridians:"),
    ("Build process failure.", ":hammer:"),
    ("Release planning.", ":rocket:"),
    ("Deployment problem.", ":ship:"),
    ("Success case scenario.", ":heavy_check_mark:"),
    ("Failure case scenario.", ":x:"),
    ("Code review request.", ":eyes:"),
    ("Merge conflicts.", ":twisted_rightwards_arrows:"),
    ("Commit message issue.", ":pushpin:"),
    ("Pull request discussion.", ":arrows_counterclockwise:"),
    ("Version control management.", ":bookmark:"),
    ("Hotfix required.", ":fire:"),
    ("Cleanup and refactoring.", ":broom:"),
    ("Revert a previous change.", ":leftwards_arrow_with_hook:"),
    ("Database connection problem.", ":floppy_disk:"),
    ("Server configuration issue.", ":cloud:"),
    ("Client-side compatibility issue.", ":computer:"),
    ("Network communication problem.", ":globe_with_meridians:"),
    ("Linux-specific bug.", ":penguin:"),
    ("Windows-specific bug.", ":desktop_computer:"),
    ("macOS-specific bug.", ":apple:"),
    ("iOS-specific bug.", ":iphone:"),
    ("Android-specific bug.", ":robot:"),
    ("JavaScript-related issue.", ":yellow_heart:"),
    ("Python-related issue.", ":snake:"),
    ("Ruby-related issue.", ":gem:"),
    ("Java-related issue.", ":coffee:"),
    ("PHP-related issue.", ":elephant:"),
    ("HTML-related issue.", ":page_facing_up:"),
    ("CSS-related issue.", ":art:"),
    ("SASS-related issue.", ":eyeglasses:"),
    ("LESS-related issue.", ":arrow_down_small:"),
    ("JSON-related issue.", ":memo:"),
    ("Markdown-related issue.", ":memo:"),
    ("Docker-related issue.", ":whale:"),
    ("AWS-related issue.", ":cloud:"),
    ("Azure-related issue.", ":cloud:"),
    ("GCP-related issue.", ":cloud:"),
    # Add more labeled data relevant to your situation...
]

# Extract the features (X) and labels (y) from the labeled data
X = [data[0] for data in labeled_data]
y = [data[1] for data in labeled_data]

# Perform data augmentation
augmented_X, augmented_y = augment_data(X, y)

# Combine original and augmented data
combined_X = X + augmented_X
combined_y = y + augmented_y

# Train the classifier
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(combined_X)
classifier = LogisticRegression()
classifier.fit(X_train, combined_y)

# Save the trained classifier and vectorizer to a file
with open("training/model.pkl", "wb") as f:
    pickle.dump((vectorizer, classifier), f)
