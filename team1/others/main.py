while True :
  alllist = []
  elements = []
  print("\nEnter a sentence: ")
  test = input()


  for i in range (0,len(test)) :
    mychar = test[i] 
    alllist.insert(0,mychar)
  alllist.sort()
  for i in range ( 0, len(alllist) ) :
    currentchar = alllist[i]
    if i == 0 :
      elements.insert(0, currentchar)
    else:
      if currentchar != elements[0] :
        elements.insert(0, currentchar)
  elements.sort()
  print("\nCharacters:\n")
  for temp in elements:
    howmany = 0 
    for temp2 in alllist :
      if temp == temp2 :
        howmany = howmany+1
    print(temp,": ", howmany)



    



