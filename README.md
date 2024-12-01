# AI IMAGE AND TEXT COMPRESSION
# Image compression
2 types, prompt, and slice:
Prompt uses AI to create a description of an image and then to decompress it we use an iamge generator to generate an image based on that prompt. Slicing removes half the pixles of the image, and based on the surrounding images uses AI to guess what the pixel in between would be.

![image](https://github.com/user-attachments/assets/7844fd38-75a2-48c5-aa07-223bfb01c005)
Goes to 
![image](https://github.com/user-attachments/assets/e09001d1-6d1a-4332-8890-7876b171b7fd)

# Text compression
All of the vowels in the file are removed to compress it, to decompress it is fed into an LLM tasked with rebuilding it my replacing the vowels.

Original:
i have a brown fox called tom

Compressed:
hv  brwn fx clld tm

Decompressed:
All of the horses I have bare a brown fox called Tim
