# Artificial Intelligence Text Compression

I designed a new type of text compression algorithm that can reduce the filesize of a text file by up to 50%.
This new algorithm can take a 65 byte file and compress it into a 32 byte file which can halve the time it takes to send across the internet. The program can also decompress the file once transferred with up to 100% accuracy.

![image](https://github.com/user-attachments/assets/31a00227-e90d-4b8d-81e7-0a2678f0b1f5)

It works by removing half of the characters in the text to compress it. To decompress it it sends the filename and compressed text to a LLM and asks it to rebuild the text.

Results:

When removing **50%** of the text, the algorithm can decompress it to roughly **70%** of the original text

When removing **25%** of the text, the algorithm copes much better, managing to recreate **>90%** of the original file
