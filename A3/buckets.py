capacity = [4,3]

initialState = [0,0]

objectiveState = [2,0]

def enc1(buckets) :
    return [capacity[0], buckets[1]]

def enc2(buckets) :
    return [buckets[0], capacity[1]]

def esv1(buckets) :
    return [0, buckets[1]]

def esv2(buckets) :
    return [buckets[0], 0]

def d12(buckets) :
    if buckets[0] > (capacity[1]-buckets[1]) :
        return [buckets[0] - (capacity[1]-buckets[1]), capacity[1]]
    else :
        return [0, buckets[1]+buckets[0]]

def d21(buckets) :
    if buckets[1] > (capacity[0]-buckets[0]) :
        return [capacity[0], buckets[1] - (capacity[0]-buckets[0])]
    else :
        return [buckets[1]+buckets[0], 0]

def getNewBuckets(bucket) :
    newBuckets = [enc1(bucket)]
    newBuckets.append(enc2(bucket))
    newBuckets.append(esv1(bucket))
    newBuckets.append(esv2(bucket))
    newBuckets.append(d12(bucket))
    newBuckets.append(d21(bucket))
    return newBuckets

def loop(buckets) :
    if not buckets :
        print('No solution found!')
        return -1

    loopBucketsList = []
    for bucket in buckets :
        newBuckets = getNewBuckets(bucket[len(bucket)-1])
        for newBucket in newBuckets :
            historyBucketsList = bucket[:]
            if newBucket == objectiveState :
                print('Solution found:')
                bucket.append(newBucket)
                print(bucket)
                return 1
            if newBucket not in historyBucketsList :
                historyBucketsList.append(newBucket)
                loopBucketsList.append(historyBucketsList)
    loop(loopBucketsList)

def solve() :
    currentState = [[initialState]]
    loop(currentState)

solve()

