#defining a function with 3 parameters
def Numbers(A, arr_size, sum):
    # Fix the first element as A[i]
    for i in range(0, arr_size - 2):

        # Fix the second element as A[j]
        for j in range(i + 1, arr_size - 1):

            # Now look for the third number
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                    print("Triplet is", A[i],
                          ",", A[j], ",", A[k])
                    return True

    return False

#declaring a predefined list
A =[1, 1, 2, -2, 0, 9]
#the condition
sum = 0
arr_size = len(A)
Numbers(A, arr_size, sum)
