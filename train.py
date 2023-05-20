from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Function to train a classifier
def train_classifier(X, y):
    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(X)
    classifier = LogisticRegression()
    classifier.fit(X_train, y)
    return vectorizer, classifier

# Define your labeled training data
labeled_data = [
    ("This is a bug report.", ":bug:"),
    ("Please fix this issue.", ":bug:"),
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
    ("Build process failure.", ":building_construction:"),
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
    ("macOS-specific bug.", ":computer:"),
    ("iOS-specific bug.", ":iphone:"),
    ("Android-specific bug.", ":robot:"),
    ("JavaScript-related issue.", ":javascript:"),
    ("Python-related issue.", ":snake:"),
    ("Ruby-related issue.", ":gem:"),
    ("Java-related issue.", ":coffee:"),
    ("PHP-related issue.", ":elephant:"),
    ("HTML-related issue.", ":html5:"),
    ("CSS-related issue.", ":css3:"),
    ("SASS-related issue.", ":eyeglasses:"),
    ("LESS-related issue.", ":minus:"),
    ("JSON-related issue.", ":memo:"),
    ("XML-related issue.", ":page_with_curl:"),
    ("Markdown-related issue.", ":pencil2:"),
    ("TypeScript-related issue.", ":typescript:"),
    ("Go-related issue.", ":gopher:"),
    ("Rust-related issue.", ":rust:"),
    ("Shell scripting issue.", ":shell:"),
    ("C programming issue.", ":desktop_computer:"),
    ("C++ programming issue.", ":desktop_computer:"),
    ("C# programming issue.", ":desktop_computer:"),
    ("Swift programming issue.", ":swift:"),
    ("Kotlin programming issue.", ":kotlin:"),
    ("Flutter-related issue.", ":flutter:"),
    ("Docker-related issue.", ":whale:"),
    ("AWS-related issue.", ":aws:"),
    ("Azure-related issue.", ":azure:"),
    ("GCP-related issue.", ":gcp:"),
    ("GraphQL-related issue.", ":graphql:"),
    ("REST API issue.", ":zzz:"),
    ("OAuth-related issue.", ":key:"),
    ("Redux-related issue.", ":recycle:"),
    ("Vuex-related issue.", ":recycle:"),
    ("Angular-related issue.", ":a:"),
    ("React-related issue.", ":atom_symbol:"),
    ("Vue.js-related issue.", ":herb:"),
    ("Svelte-related issue.", ":mag:"),
    ("Django-related issue.", ":spider_web:"),
    ("Flask-related issue.", ":wine_glass:"),
    ("Ruby on Rails-related issue.", ":train:"),
    ("Laravel-related issue.", ":framed_picture:"),
    ("Spring-related issue.", ":cherry_blossom:"),
    ("Node.js-related issue.", ":leaves:"),
    ("Express.js-related issue.", ":train2:"),
    ("NestJS-related issue.", ":bird:"),
    ("MongoDB-related issue.", ":leaves:"),
    ("MySQL-related issue.", ":dolphin:"),
    ("PostgreSQL-related issue.", ":elephant:"),
    ("SQLite-related issue.", ":file_folder:"),
    ("Redis-related issue.", ":fire:"),
    ("WordPress-related issue.", ":capital_abcd:"),
    ("Shopify-related issue.", ":shopping_cart:"),
    ("WooCommerce-related issue.", ":shopping_cart:"),
    ("Joomla-related issue.", ":j:"),
    ("Drupal-related issue.", ":d:"),
    # Add more labeled data...
]

# Extract the features (X) and labels (y) from the labeled data
X = [data[0] for data in labeled_data]
y = [data[1] for data in labeled_data]

# Train the classifier
vectorizer, classifier = train_classifier(X, y)

# Save the trained classifier and vectorizer to a file
with open("model.pkl", "wb") as f:
    pickle.dump((vectorizer, classifier), f)
