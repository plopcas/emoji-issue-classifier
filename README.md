
# Emoji Issue Classifier

The Emoji Issue Classifier is a GitHub Action that automatically classifies issues by adding relevant emoji labels. It performs sentiment analysis, keyword matching, and machine learning-based classification to add relevant emoji labels to the issues.

## Usage

1. Create a `.github/workflows/emoji-classifier.yml` file in your repository.
2. Add the following workflow configuration to the file:

```yaml
# .github/workflows/issue-classifier.yml
name: 'Use Emoji Issue Classifier Action'

on:
  issues:
    types: [opened, edited]

jobs:
  classify:
    runs-on: ubuntu-latest

    steps:
    - name: Use Emoji Classifier
      uses: plopcas/emoji-issue-classifier@v1.1.0
      env:
        GITHUB_TOKEN: ${{ secrets.PAT }}
```

3. Configure the necessary environment variables:
   - `GITHUB_TOKEN`: GitHub token with repository access.
4. Customize the behavior of the Emoji Issue Classifier by modifying the Python script (`main.py`) based on your requirements.
5. Run the Emoji Issue Classifier by executing `python main.py` in the repository directory.

## Test

In order to test the classifier you can:

1. Create a `test.json` file with the following content:

```
{
    "issue": {
      "number": 1
    }
}
```

2. Create a `test.sh` file with the following content:
```
#!/bin/bash
# test.sh

export GITHUB_TOKEN=YOUR_TOKEN
export GITHUB_REPOSITORY=YOUR_REPOSITORY
export GITHUB_EVENT_PATH=test/test.json
python classifier/main.py
```

3. Ensure that the bash script (test.sh) has the correct permissions to be executed.
```
chmod +x test.sh
```

4. Run run this bash script from the terminal with:
```
./test.sh
```

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
