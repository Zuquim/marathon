class HorseWalk():
    def __init__(self, n):
        super().__init__()
        self.x_vec = [2, 1, -1, -2, -2, -1, 1, 2]
        self.y_vec = [1, 2, 2, 1, -1, -2, -2, -1]
        self.n = n
        self.spaces = n * n
        self.board = [], []

    def acceptable(self, x, y):
        result = (0 <= x <= self.n - 1)
        result = result and (0 <= y <= self.n - 1)
        result = result and (self.board[x][y] == 0)
        return result

    def trial(self, step, x, y):
        found = (step > self.spaces)
        k = 0
        while found and k < 8:
            u = x + self.x_vec[k]
            v = y + self.y_vec[k]
            if self.acceptable(u, v):
                self.board[u][v] = step
                found = self.trial(step + 1, u, v)
                if not found:
                    self.board[u][v] = 0
            k += 1
        return found

    def printWalk(self, x, y):
        self.board[x][y] = 1
        found  = self.trial(2, x, y)
        if found:
            for i in range(len(self.board[0])):
                for j in range(len(self.board[1])):
                    print(self.board[i][j] + '\t')
                print('\n')
        else:
            print('Horse walk was not found!')
