from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn . feature_extraction . text import TfidfVectorizer
from sklearn . metrics . pairwise import cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Q1:


def compute_mean(x):
    mean = np.mean(x)
    return mean


X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
print("Q1 : Mean : ", compute_mean(X))

# Q2:


def compute_median(x):
    size = len(x)
    x = np.sort(x)
    # print(x)
    if (size % 2 == 0):
        index = int(size/2)
        return (x[index-1] + x[index])/2
    else:
        index = int(size+1/2)
        return x[index]


X = [1, 5, 4, 4, 9, 13]
print("Q2 : Median : ", compute_median(X))


# Q3:

def compute_std(x):

    size = len(x)
    mean = compute_mean(x)
    variance = 1/size*np.sum((x-mean)**2)
    return np.sqrt(variance)


X = [171, 176, 155, 167, 169, 182]
print("Q3 - ", compute_std(X))


# Q4:

def compute_correlation_cofficient(x, y):
    n = len(x)
    numerator = n*np.sum(x*y) - np.sum(x)*np.sum(y)
    denominator = np.sqrt(n*np.sum(x**2) - np.sum(x)**2) * \
        np.sqrt(n*np.sum(y**2) - np.sum(y)**2)

    return np.round(numerator/denominator, 2)


X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print("Q4 - Correlation : ", compute_correlation_cofficient(X, Y))


# Q5:

# Download dataset : ! gdown 1 iA0WmVfW88HyJvTBSQDI5vesf - pgKabq

data = pd.read_csv("module_2/week_4_statistics/advertising.csv")


def correlation(x, y):
    return compute_correlation_cofficient(x, y)


x = data["TV"]
y = data["Radio"]
corr_xy = correlation(x, y)
print(f"Q5 - Correlation between TV and Sales : {round(corr_xy,2)}")

# Q6:
features = ["TV", "Radio", "Newspaper"]

for feature_1 in features:
    for feature_2 in features:
        correlation_value = correlation(data[feature_1], data[feature_2])
        print(
            f"Q6 - Correlation between {feature_1} and {feature_2}: {round(correlation_value, 2)}")

# Q7:
x = data["Radio"]
y = data["Newspaper"]

result = np.corrcoef(x, y)
print(f"Q7 - {result}")

# Expected output : [[1. 0.35410375]
# [0.35410375 1. ]]

# Q8:

print(f"Q8 -{data.corr()}")

# Q9:

plt.figure(figsize=(10, 8))
data_corr = data.corr()
sns.heatmap(data_corr, annot=True, fmt=".2f", linewidth=.5)
plt.show()

# Q10:
vi_data_df = pd.read_csv("module_2/week_4_statistics/vi_text_retrieval.csv")
context = vi_data_df["text"]
context = [doc.lower() for doc in context]

tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)
element_value = context_embedded.toarray()[7][0]
print("Element at [7][0]:", element_value)

# Q11:


def tfidf_search(question, tfidf_vectorizer, context, top_d=5):
    # Lowercasing the question
    question = question.lower()

    # Encode the question with TF-IDF
    query_embedded = tfidf_vectorizer.transform([question])

    # Compute cosine similarity between query and context
    cosine_scores = cosine_similarity(query_embedded, context).flatten()

    # Get top k cosine score and index its
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            'id': idx,
            'cosine_score': cosine_scores[idx]
        }
        results.append(doc_score)
    return results


# Load the dataset
context = vi_data_df['text']

# Convert the text to lowercase
context = [doc.lower() for doc in context]

# Initialize the TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit the vectorizer to the context
context_embedded = tfidf_vectorizer.fit_transform(context)

# Example usage
question = vi_data_df.iloc[0]['question']
results = tfidf_search(question, tfidf_vectorizer, context_embedded, top_d=5)

# Print the top result's cosine score
print("Top result's cosine score:", results[0]['cosine_score'])


# Q12:

def corr_search(question, tfidf_vectorizer, context, top_d=5):
    # Lowercasing before encoding
    question = question.lower()

    # Transform the question into TF-IDF vector
    query_embedded = tfidf_vectorizer.transform([question])

    # Calculate cosine similarity scores
    corr_scores = cosine_similarity(query_embedded, context).flatten()

    # Get top k correlation scores and their indices
    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'corr_score': corr_scores[idx]
        }
        results.append(doc)
    return results


# Load the dataset
context = vi_data_df['text']

# Convert the text to lowercase
context = [doc.lower() for doc in context]

# Initialize the TF-IDF Vectorizer and fit the context
tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)

# Example usage
question = vi_data_df.iloc[0]['question']
results = corr_search(question, tfidf_vectorizer, context_embedded, top_d=5)

# Print the second top result's correlation score
print("Second top result's correlation score:", results[1]['corr_score'])
