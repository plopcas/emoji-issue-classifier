
# Emoji Issue Classifier

The Emoji Issue Classifier is a GitHub Action that automatically classifies issues by adding relevant emoji labels. It performs sentiment analysis, keyword matching, and machine learning-based classification to add relevant emoji labels to the issues.

## Usage

1. Create a `.github/workflows/emoji-classifier.yml` file in your repository.
2. Add the following workflow configuration to the file:

```yaml
name: Emoji Issue Classifier
on:
  issues:
    types:
      - opened
      - edited

jobs:
  classify-issue:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x

      - name: Install dependencies
        run: pip3 install -r requirements.txt

      - name: Run Emoji Issue Classifier
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: python main.py
```

3. Configure the necessary environment variables:
   - `GITHUB_TOKEN`: GitHub token with repository access.
   - (Optional) Other environment variables used in your script.
4. Customize the behavior of the Emoji Issue Classifier by modifying the Python script (`main.py`) based on your requirements.
5. Run the Emoji Issue Classifier by executing `python main.py` in the repository directory.

## Customization

You can customize the behavior of the Emoji Issue Classifier by modifying the following components:

- **Sentiment Analysis**: adjust the sentiment thresholds and corresponding emojis in the `get_sentiment_emoji` function.
- **Keyword Matching**: add or modify keywords and corresponding emojis in the `get_keyword_emoji` function.
- **Trained Model**: train and save a new model using the provided `train` script and replace the `model.pkl` file.
- **Label Color**: change the label color in the `add_label_to_issue` function by modifying the hex color code.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
