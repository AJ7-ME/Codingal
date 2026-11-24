import math
from collections import defaultdict, Counter
from articles import ARTICLES
def tokenize(text):
    return "".join(ch if ch.isalnum() else " " for ch in text.lower()).split()
index = defaultdict(dict)
lengths = {}
for doc_id, (title, text) in enumerate(ARTICLES):
    words = tokenize(title + " " + text)
    lengths[doc_id] = len(words)
    for word in words:
        index[word][doc_id] = index[word].get(doc_id, 0) + 1
N = len(ARTICLES)

def idf(word):
    count = len(index.get(word, {}))
    if count == 0:
        return 0
    return math.log(N / count)
def search(query, method="TF-IDF", k=3):
    scores = Counter()
    for word in tokenize(query):
        for doc_id, count in index.get(word, {}).items():
            tf = count / lengths[doc_id]
            if method == "COUNT":
                scores[doc_id] += count
            elif method == "TF":
                scores[doc_id] += tf
            else:  # TF-IDF
                scores[doc_id] += tf * idf(word)
    results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return results[:k]
print("Welcome to the Mini Search Engine!")
while True:
    query = input("\nEnter your search query (or 'exit' to quit): ")
    if query.lower() == "exit":
        print("Exiting the search engine. Goodbye!")
        break
    result = search(query)
    if not result:
        print("No results found.")
    else:
        for rank, (doc_id, score) in enumerate(result, start=1):
            title = ARTICLES[doc_id][0]
            print(f"{rank}. {title} (Score: {score:.3f})")