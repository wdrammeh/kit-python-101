"""
Write a function that accepts a string arg
Return its reverse
"""

def reverse_str(text):
    i = len(text) - 1
    rev = ""
    while i >= 0:
        rev = rev + text[i]
        i = i - 1
    return rev

if __name__ == "__main__":
    text = "Muhammed"
    rev = reverse_str(text)
    print(text)
    print(rev)