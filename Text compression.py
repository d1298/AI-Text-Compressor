from groq import Groq

client = Groq(
    api_key=("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"),
)


#amount (1/x) of the text to be removed
# max 2

def compress(file, remove):
    text = []
    length = len(file)
    for i in range(length):
        text.append(file[i])
            
    shorterText = text
    shorterText = [char for i, char in enumerate(text) if i % remove != 0]
            
    
    finalText = ""
    
    for i in range(len(shorterText)):
        finalText += shorterText[i] 
    
    return finalText
        
        
def decompress(text,remove,filename):
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Given 1/" + str(remove) + "character of the following text has been removed,replace the missing letters to complete the text given the file name is " + filename + ". All of the letters provided are in the final text so do not remove any, the spaces are also definitely gaps between words. The final number of characters in the text is also 65 .It is vital that you only return the final text and no explanation or extra formatting, also do not return the title of the file, the test is: " + text,
            }
        ],
        model="llama3-8b-8192"
    )
    
    return (completion.choices[0].message.content)

def jaccard_similarity(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)


filename = input("What is the name of the file you want to compress? ")
remove = int(input("What amount of the file would you like to compress?"))

with open(filename, "r") as r:
    file = r.read()


with open ("compressed.txt", "w") as w:
    compressed = compress(file, remove)
    w.write(compressed)

with open("decompressed.txt", "w") as w:
    decompressed =decompress(compressed,remove, filename)
    w.write(decompressed)
    print(f"Accuracy: {jaccard_similarity(file, decompressed) * 100}%")
