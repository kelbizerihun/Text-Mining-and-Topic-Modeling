import os
import re
import PyPDF2
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

#Abina- Function to extract text from PDF files
def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return text

#Mike- Function for data cleaning
def clean_text(text):
  
    cleaned_text = re.sub(r'\W+', ' ', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.lower() 

#Mike- Function for data partitioning (e.g., train-test split)
def partition_data(data, train_ratio=0.8):
    train_size = int(len(data) * train_ratio)
    train_data = data[:train_size]
    test_data = data[train_size:]
    return train_data, test_data

#Kelbi- Function for feature extraction and data reduction
def extract_features(data):

    tfidf_vectorizer = TfidfVectorizer(max_features=1000)
    tfidf_matrix = tfidf_vectorizer.fit_transform(data)

    svd = TruncatedSVD(n_components=100)
    reduced_features = svd.fit_transform(tfidf_matrix)

    return reduced_features

#Abina- Data collection
pdf_files_directory = 'pdf_files/'
pdf_files = [os.path.join(pdf_files_directory, file) for file in os.listdir(pdf_files_directory)]

#Abina- Extract text from PDF files
corpus = []
for pdf_file in pdf_files:
    text = extract_text_from_pdf(pdf_file)
    corpus.append(text)

#Mike- Data cleaning
cleaned_corpus = [clean_text(text) for text in corpus]

#Mike- Data partitioning
train_data, test_data = partition_data(cleaned_corpus)

#Naizgi -Analytical processing and algorithms
#Kelbi- Feature extraction and data reduction
train_features = extract_features(train_data)
test_features = extract_features(test_data)


print("Sample Train Features:")
print(train_features[:5])
print("Sample Test Features:")
print(test_features[:5])
