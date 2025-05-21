class UnionFind:
    def __init__(self, size):
        # Initialize the parent and rank arrays
        self.parent = list(range(size))  # Each element is its own parent initially
        self.rank = [0] * size  # Rank is used to keep the tree flat

    def find(self, x):
        # Find the root of the element x with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Compress the path
        return self.parent[x]

    def union(self, x, y):
        # Union the sets containing x and y
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False  # They are already in the same set

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


def read_input(file_path):
    # Read the input from a file
    with open(file_path, 'r') as f:
        lines = f.read().strip().splitlines()
    n, k, bucket_cost, bond_cost = map(int, lines[0].split())
    bonds = [tuple(map(int, line.split())) for line in lines[1:]]
    return n, bucket_cost, bond_cost, bonds


def compute_minimum_cost(n, bucket_cost, bond_cost, bonds):
    edges = []

    # Connect the virtual node (0) to each dyno (1 to n) with bucket_cost
    for dyno in range(1, n + 1):
        edges.append((bucket_cost, 0, dyno))

    # Add the actual bonds between dynos with bond_cost
    for u, v in bonds:
        edges.append((bond_cost, u, v))

    # Sort all edges by cost
    edges.sort()

    # Initialize Union-Find structure for n dynos plus the virtual node
    uf = UnionFind(n + 1)
    total_cost = 0
    connected_count = 0

    for cost, u, v in edges:
        # Attempt to union the two nodes
        if uf.union(u, v):
            total_cost += cost  # Add the cost of the edge to the total
            connected_count += 1
            if connected_count == n:  # Stop if all dynos are connected
                break

    return total_cost


def main():
    # Main function to read input and compute the minimum cost
    file_path = input("Enter the absolute path to the input file: ").strip()
    try:
        n, bucket_cost, bond_cost, bonds = read_input(file_path)
        min_cost = compute_minimum_cost(n, bucket_cost, bond_cost, bonds)
        print(min_cost)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()