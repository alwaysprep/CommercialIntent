from sklearn.svm import SVC

from reader import extract



new_data_text, new_data_class = extract("cleaned_data.csv")


cls = SVC()

train = new_data_class[:len(new_data_class)/2]

cls.fit(train)