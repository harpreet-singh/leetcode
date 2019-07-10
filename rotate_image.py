class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        #print(matrix)
        
        #matrix = list(map(list,zip(*matrix)))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
