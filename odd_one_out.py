def odd_one_out(arr):
    counter = []
    for i in range(len(arr)):
        counter.append(len(arr[i]))
    arr_len = len(arr)   
    count_nums = 0
    for x in range(len(counter)):
        if arr_len - counter.count(counter[x]) == 1:
            return True
        elif x != len(counter) - 1:
            if counter.count(counter[x]) == 1 and counter.count(counter[x+1]) != 1:
                return True
        else:
            return False
            
odd_one_out(["swanky", "rhino", "moment"])
odd_one_out(["silly", "mom", "let", "the"])
odd_one_out(["the", "them", "theme"])
odd_one_out(["very", "to", "an", "some"])