ratings=[1,2,2]
candies=0
prev_rating=1
c=0
for i in range(len(ratings)):
    if ratings[i]>prev_rating :
        c+=1 
        candies+=c  
        prev_rating=ratings[i]
    if prev_rating>ratings[i] :
        c=1
        candies+=2
        prev_rating=ratings[i] 
    if prev_rating==ratings[i] :
        c=1
        candies+=c  
    print(c)

print(candies)