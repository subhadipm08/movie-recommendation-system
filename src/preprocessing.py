import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(tag):
    if tag.startswith("J"):
        return wordnet.ADJ
    elif tag.startswith("V"):
        return wordnet.VERB
    elif tag.startswith("N"):
        return wordnet.NOUN
    elif tag.startswith("R"):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def lemmatize_text(text):
    tokens = word_tokenize(text.lower())
    tagged = nltk.pos_tag(tokens)

    lemmas = [
        lemmatizer.lemmatize(word, get_wordnet_pos(pos))
        for word, pos in tagged
        if word.isalpha()
    ]
    return " ".join(lemmas)


def preprocess_tags(df: pd.DataFrame, col: str = "tags") -> pd.DataFrame:
    """
    Clean tags column safely.
    """
    if col not in df.columns:
        raise KeyError(f"Column '{col}' not found in DataFrame")

    df2 = df.copy()
    df2[col] = df[col].fillna("").apply(lemmatize_text)

    return df2
