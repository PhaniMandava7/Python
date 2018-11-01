# textwrap module has 2 functions wrap() and fill() to wrap the texts.

# textwrap.wrap(text[,width])  -------> wraps the single paragraph in text so every line is at most widh characters long.
#    wrap function returns a list of output lines, without final newlines.


# textwrap.fill(text[,width])  -------> wraps the single paragraph in text and returns a single string containing the wrapped paragraph.
#    fill returns the wrapped lines joined with a new line.

#----------  fill(text) ~= "\n".join(wrap(text))

string = 'textwrap.wrap(text[,width])  -------> wraps the single paragraph in text so every line is at most widh characters long.'
import textwrap
wrapped_text = textwrap.wrap(string)  # -----> It doesn't split the words at width=70
for line in wrapped_text:
    print(len(line),'->',line)

print()
print()


filled_text = textwrap.fill(string)  # -----> It doesn't split the words at width=70
print(filled_text)

print('---------------------------------------------------------------')


import textwrap
width=10
wrapped_text = textwrap.wrap(string,width)  # -----> It doesn't split the words at width=70
for line in wrapped_text:
    print(len(line),'->',line)

print()
print()


filled_text = textwrap.fill(string,width)  # -----> It doesn't split the words at width=70
print(filled_text)
