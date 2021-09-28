
dictionary = {
				'hello':'gesture greeting',
				'good':'achha'
				}

Search = input("pleae enter your word in Dictionary: ")
print("\n----------------------------")
print("\nYour entered::  %s \n\n Searching ............... \n " % Search)
print("\n----------------------------")

Result={}
for keys,value in dictionary.items():
	if str(keys)== str(Search):
		Result[keys]= value
		break

if len(Result)==0:
	print("not match")
else:
	print("Meaning for this %s World is %s: " % (Result.keys(), Result.values()))