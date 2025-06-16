from textblob import TextBlob

def correct_text(text):
    blob = TextBlob(text)
    corrected = blob.correct()
    return str(corrected)

# it corrects spelling errors in the input text using TextBlob
input_text = input("Enter a sentence: ")
print("Corrected:", correct_text(input_text))
