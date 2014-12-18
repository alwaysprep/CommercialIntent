from sklearn.pipeline import Pipeline
from sklearn.cross_validation import KFold
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from sklearn.svm import SVC

from reader import extract



new_data_text, new_data_class = extract("cleaned_data.csv")


pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range=(1, 1))),
    ('classifier', SVC(kernel='linear')),
])

k_fold = KFold(n=new_data_text.size, n_folds=5)


scores = []

for train_indices, test_indices in k_fold:

    train_text = new_data_text[train_indices]
    train_y = new_data_class[train_indices]
    test_text = new_data_text[test_indices]
    test_y = new_data_class[test_indices]

    pipeline.fit(train_text, train_y)

    predicted = pipeline.predict(test_text)

    score = pipeline.score(test_text, test_y)

    scores.append(score)


print(score)