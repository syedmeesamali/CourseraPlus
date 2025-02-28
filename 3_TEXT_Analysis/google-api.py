import argparse
from google.cloud import language_v1


def print_result(annotations):
    """Prints the sentiment analysis results."""
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print("Sentence {} has a sentiment score of {}".format(index, sentence_sentiment))
    print("Overall Sentiment: score of {} with magnitude of {}".format(score, magnitude))
    return 0


def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language_v1.LanguageServiceClient()

    # Open and read the file
    with open(movie_review_filename, "r") as review_file:
        content = review_file.read()

    # Create a document object
    document = language_v1.Document(
        content=content, type_=language_v1.Document.Type.PLAIN_TEXT
    )

    # Analyze sentiment
    annotations = client.analyze_sentiment(request={"document": document})

    # Print the results
    print_result(annotations)


if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Analyze the sentiment of a movie review file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "filename", help="The filename of the movie review you'd like to analyze."
    )

    # Parse arguments
    args = parser.parse_args()

    # Call the analyze function with the filename
    analyze(args.filename)