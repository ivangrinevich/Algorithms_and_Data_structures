class DisjointSetUnion:

    def __init__(self, n):
        self.size = [1 for _ in range(n)]
        self.parent = [i + 1 for i in range(n)]

    def find_set(self, x):
        if x == self.parent[x - 1]:
            return x
        self.parent[x - 1] = self.find_set(self.parent[x - 1])
        return self.parent[x - 1]

    def union(self, x, y):
        x = self.find_set(x)
        y = self.find_set(y)
        if x != y:
            if self.size[x - 1] < self.size[y - 1]:
                x, y = y, x
            self.parent[y - 1] = x
            self.size[x - 1] += self.size[y - 1]
            return True
        return False


with open('../Individual_task/inputs/roads_input.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/roads_output.txt', 'w', encoding='utf-8') as f_output:
    n, q = [int(i) for i in f_input.readline().split()]
    coherency = n
    p = DisjointSetUnion(n)
    for i in range(q):
        u, v = [int(i) for i in f_input.readline().split()]
        if p.union(u, v):
            coherency -= 1
        print(coherency, file=f_output)
