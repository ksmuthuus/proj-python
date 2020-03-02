def sentence_maker(phrase):
  interrogatives=("Who","Why","How","When","Which","What")
  phrase = phrase.capitalize()
  if phrase.startswith(interrogatives):
    phrase="{}?".format(phrase)
  else:
    phrase="{}.".format(phrase)
  return phrase

results=[]
while True:
  text=input("Say something: ")
  if(text == "/end"):
    break
  else:
    results.append(sentence_maker(text))
formattedResult = " ".join(results)
print(formattedResult)




