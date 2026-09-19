s ="hello everyu one"

words=s.split()

result=" "

for word in words:
    if len(word)>len(result):
        result=word
    

print("longest words in this : ",result)