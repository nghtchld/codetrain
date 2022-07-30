# %%
import random
import os
# %%
# txt = "Thank you for this video! I was coding along and noticed that if you capitalize the 'The' in the  theremin sentence as your corpus ('the theremin is theirs, ok? yes, it is. this is a theremin.'), it actually  only repeats 'The' when you generate the text (like what Daniel is doing at 19:33). Does anyone have any insight into this? The only explanation I could even remotely think of is that the ascii of the capital 'T' is getting in the way of the random function but I'm probably completely off. Thanks again!"
data = 'data'
filename = 'nggyu.txt' #'text.txt'
filepath = os.path.join(data,filename)

with open(filepath, 'r', encoding='utf-8') as f:
    txt = f.read()#.replace('\n', ' ')

order = 4
ngrams = {}
output_length = 500
seed = 'love'

for i in range(len(txt)-order):
    gram = txt[i:i+order].lower()
    next_letter = txt[i+order]
    if gram not in ngrams:
        ngrams[gram] = [next_letter]
    else:
        ngrams[gram].append(next_letter)

# %%
newtxt = seed
for n in range(output_length):
    new_ngram = newtxt[n:n+order].lower()
    extend = random.choice(ngrams[new_ngram])
    newtxt += extend
    
# %%
print(newtxt)
# # %%
# for k,v in ngrams.items():
#     print(k,v)
# %%
