import urllib

def read_text():
    quotes = open('/Users/federico/Desktop/python-course/movie_quotes.txt')
    content = quotes.read()
    quotes.close()
    check_profanity(content)

def check_profanity(text_to_check):
    connection = urllib.urlopen(
        'http://www.wdylike.appspot.com/?q=' + text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()