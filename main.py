from openai import OpenAI

words = open("/usr/share/dict/words")
contents_of_file = words.read()
word_set = set(contents_of_file.split())
words.close()


initial = ["sallad", "ribus", "rnamen", "pocke", "riche", "sbub", "tacro", "beread", "keabab", "pike"]
first_five = set()
second_five = set()


for a in initial[0]:
    for b in initial[1]:
        for c in initial[2]:
            for d in initial[3]:
                for e in initial[4]:
                    first_response = a+b+c+d+e
                    first_five.add(first_response)

first_half = word_set.intersection(first_five)




for f in initial[5]:
        for g in initial[6]:
            for h in initial[7]:
                 for i in initial[8]:
                      for j in initial[9]:
                           second_response = f+g+h+i+j
                           second_five.add(second_response)

second_half = word_set.intersection(second_five)

print(first_half)
print(second_half)

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = ""
)

completion = client.chat.completions.create(
  model="nvidia/llama-3.1-nemotron-70b-instruct",
  messages=[{"role":"user","content":f"Form a two word phrase from these two lists: {first_half} and {second_half}"}],
  temperature=0.5,
  top_p=1,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")