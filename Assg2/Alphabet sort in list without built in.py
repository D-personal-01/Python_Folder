def alphasort(l1):
    l2 = l1.copy()  
    r = []

    while l2:
        smallest = l2[0]
        for word in l2:
            if word.lower() < smallest.lower():
                smallest = word
        l2.remove(smallest)   
        r.append(smallest)      

    return r


l1 = ["banana", "apple", "Cherry", "date", "apricot"]
print(alphasort(l1))