# TO CHECK IF TWO GIVEN STRINGS ARE ANAGRAM OR NOT:-
x=input('enter the first string').lower()
y=input('enter the second sring').lower()
if len(x)==len(y):
    if sorted(x)==sorted(y):
        print("true")
else:
    print("false")
