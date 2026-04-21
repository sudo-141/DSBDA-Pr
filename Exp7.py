import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

text = "Hello Mr.Dayum, How are you doing today? Weather is good today. You should enjoy."
tokenized_text=sent_tokenize(text)
print(tokenized_text)
print("\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

tokenized_word=word_tokenize(text)
print(tokenized_word)
print("\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

ex_sent="""A Sample for free, showing off stop words flitration."""
stop_words=set(stopwords.words('english'))
word_tokens =word_tokenize(ex_sent)
print("\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
print("\n Word Tokenization : ", word_tokens)
print("\n Filtered : ", filtered_sentence)
print("\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

ps = PorterStemmer()
words = ["program","programs","programmer","programing","programmers"]
for w in words:
    print(w, " : ",ps.stem(w))
print("\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

lemmatizer = WordNetLemmatizer()
print("rocks : ", lemmatizer.lemmatize("rocks"))
print(" corpora : ", lemmatizer.lemmatize("rocks"))
print("\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

sent = "Everything is all bout money"
tokens = nltk.word_tokenize(sent)
pos_tagging = nltk.pos_tag(tokens)
print(pos_tagging)
print("\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

