def hamming_distance(x, y):
    return bin(x ^ y).count('1')

def euclidean_distance(x, y):
    return abs(x - y)
