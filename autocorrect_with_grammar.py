from textblob import TextBlob
import language_tool_python

def correct_text(text):
    # it will correct spelling errors in the input text by using TextBlob....
    blob = TextBlob(text)
    spelling_corrected = str(blob.correct())
    
    # it will correct grammar errors in the input text by using LanguageTool....
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(spelling_corrected)
    grammar_corrected = language_tool_python.utils.correct(spelling_corrected, matches)
    
    return grammar_corrected

# example usage....
input_text = input("Enter a sentence: ")
print("Corrected:", correct_text(input_text))
