from pythonds.basic.stack import Stack


def balancedHTMLTags(document):
    tagStack = Stack()  # Stack for "<" and ">"
    wordStack = Stack()  # Stack for retaining words within tags
    for i in range(0, len(document)):

        if document[i] == '<':
            close = False
            start = i + 1
            tagStack.push(document[i])

            if document[i + 1] == '/':
                close = True  # for closing Tags

        elif document[i] == '>' and not tagStack.isEmpty():
            end = i - 1
            tagStack.pop()

            if close == False:
                wordStack.push(document[start:end])

            elif close == True and not wordStack.isEmpty():

                if wordStack.peek() == document[start + 1:end]:
                    wordStack.pop()
                else:
                    return False

            else:
                return False

    if tagStack.isEmpty() and wordStack.isEmpty():
        return True
    else:
        return False


print(balancedHTMLTags("<div>hi</div>"))
print(balancedHTMLTags("<html> <head> <title>Example</title> </head> <body> <h1>Hello, world</h1> </body> </html>"))
print(balancedHTMLTags("</div>test-for-false<div>"))
print(balancedHTMLTags("<h1> uhhhh </div> <div>wait wut</h1>"))
print(balancedHTMLTags("<h1>ok <div> </div> </h1>"))


