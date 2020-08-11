class Sequence:
    def example1(self,S):
        # Return the sum of elements in sequence S
        n = len(S)
        total = 0
        for j in range(n):
            total += S[j]
        return total
    
    def example2(self, S):
        # Return the sum of the elements with even index in sequence S
        n = len(S)
        total = 0
        for j in range(0,n,2):
            total += S[j]
        return total

    def example3(self, S):
        # Return the sum of the prefix sums of sequence S
        n = len(S)
        total = 0
        for j in range(n): # loop from 0 to n-1
            for k in range(1 + j): # loop from 0 to j
                total += S[k]
        return total

    def example4(self, S):
        # Return the sum of the prefix sums of sequence S
        n = len(S)
        prefix = 0
        total = 0
        for j in range(n):
            prefix += S[j]
            total += prefix
        return total

    def example5(self, A, B): # Assume that A and B have equal length
        # Return the number of elements in B equal to the sum of prefix sums in A.
        n = len(A)
        count = 0
        for i in range(n):
            total = 0
            for j in range(n):
                for k in range(1+j):
                    total += A[k]
                if B[i] == total:
                    count += 1
        return count


print(Sequence().example1([1,2,3,4,5,6,7,8,9]))
print(Sequence().example2([1,2,3,4,5,6,7,8,9]))
print(Sequence().example3([1,2,3,4,5,6,7,8,9]))
print(Sequence().example4([1,2,3,4,5,6,7,8,9]))
print(Sequence().example5([1,2,3,4,5,6,7,8,9],[2,4,10,50,69,98,100,125,165]))
