print("Enter 10 elements in list: ")
 
List=[]
for Index in range(1,11):
    Val = int(input())
    List.append(Val)
    Highest=List[0]
    for Index in List:
        if(Index>Highest):
            Highest=Index
#print( Highest)
print("Largest element is: ", Highest)
