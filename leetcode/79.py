class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n = len(board)
        m = len(board[0])
        global flag
        flag = False
        visit = [[0 for i in range(m)] for j in range(n)]
        def helper(index, i, j, visit) -> None:
            v = []
            for t in visit:
                v.append(tuple(t))
            v = tuple(v)
            if index == len(word):
                return

            for k in range(4):
                i1 = i + direct[k][0]
                j1 = j + direct[k][1]

                if i1 >= 0 and i1 < n and j1 >= 0 and j1 < m and board[i1][j1] == word[index] and v[i1][j1] == 0:
                    visit = [list(l) for l in v]
                    print(visit)
                    visit[i1][j1] = 1
                    print(word[index])
                    if index + 1 == len(word):
                        global flag
                        flag = True
                    helper(index + 1, i1, j1, visit)

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        flag = True
                    # print(visit)
                    visit[i][j] = 1
                    helper(1, i, j, visit)
                    visit = [[0 for ii in range(m)] for jj in range(n)]

        return flag
s = Solution()
BOOL = s.exist([["B","C","E"],["F","E","S"],["D","E","E"]],"ESEEEC")
print(BOOL)