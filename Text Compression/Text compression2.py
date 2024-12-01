from groq import Groq
vowels = ["a", "e", "i", "o", "u"]

def compress(file):
    text = []
    length = len(file)
    
    for i in range(length):
        text.append(file[i])
            
    shorterText = text
    
    shorterText = [char for char in text if char not in vowels]
            
    finalText = ""
    for i in range(len(shorterText)):
        finalText += shorterText[i] 
        
    return finalText
        
        
def decompress(text):
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Given all of the vowels in the following text habe been removed, replace the missing letters to complete the text All of the letters provided are in the final text so do not remove any, the spaces are also definitely gaps between words.ONLY return the final text, surround the list in quotation marks, the test is: " + text,
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

while True:
    choice = input("file or string (f or s)")
    if choice == "f":
        filename = input("What is the name of the file you want to compress? ")
        with open(filename, "r") as r:
            file = r.read()
    else: 
        file = input("What is the string you want to compress? ")
        
    API_KEY = "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"

    client = Groq(
        api_key=(API_KEY),
    )

    with open ("compressed.txt", "w") as w:
        compressed = compress(file)
        w.write(compressed)

    with open("decompressed.txt", "w") as w:
        decompressed = decompress(compressed)
        if decompressed.count('"') > 1:
            decompressed = decompressed.split('"')
        elif decompressed.count("'") > 1:
            decompressed = decompressed.split("'")
            

        index = max([jaccard_similarity(file, decompressed[i])*100 for i in range(len(decompressed))])
        
        for i in range(len(decompressed)):
            if jaccard_similarity(file, decompressed[i])*100 == index:
                decompressed = decompressed[i]
                
        w.write(decompressed)
        print("Percentage Compressed: " , int(len(compressed) / len(file) * 100), "%")
        print(f"Accuracy: {jaccard_similarity(file, decompressed) * 100}%")


 
 