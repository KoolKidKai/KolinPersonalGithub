phrase = ["race car", "bazinga", "TacoCat!"] # phrases and words being tested
specialchars = "!@#$%^&*()~`<>,./?':;}{][\| "
inverse = ""
# all special characters - !@#$%^&*()`~-_+=[{]}\|;:"',<.>/?'"]
for phrases in phrase:
  print("Original Phrase:", phrases)
  
  for chars in specialchars:
    phrases = phrases.replace(chars, "") # replaces special characters and spaces
    phrases = phrases.lower() # makes everything lowercase
    inverse = phrases[::-1] # reverses word
  print("New Phrase:", phrases)  
  
  if (phrases == inverse):
    print("Wow! That's a palindrome!")
  else:
    print("Unfortunately, that is not a palindrome.")