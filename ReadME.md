
README — Assignment 1: Bucket Access Optimization (CS206)

Student Name: Elind Kusha
Course: CS206 – Algorithms & Complexity

---

Problem Description
BigWeather is a weather forecasting company using a distributed computing system composed of dynos—machines that require access to buckets, specialized cache components containing sensor data.

Each dyno must have access to a bucket, either:
- By hosting its own (incurring a fixed bucket_cost), or
- By connecting to another dyno via a bond (incurring a fixed bond_cost).

The objective is to determine the minimum total cost to ensure that every dyno has access to at least one bucket, either directly or through connected dynos.

---

Problem Modeling
The problem is modeled as a graph:
- Each dyno is a node.
- A virtual node (node 0) represents the bucket-hosting option.
- Hosting a bucket is an edge from node 0 to the dyno with cost = bucket_cost.
- A bond is an edge between two dynos with cost = bond_cost.

We apply a modified Kruskal's Minimum Spanning Tree (MST) algorithm with a Union-Find data structure to avoid cycles and efficiently manage connectivity.

---

How It Works
1. A virtual node 0 connects to all dynos with edges weighted by bucket_cost.
2. All valid bonds are added as undirected edges weighted by bond_cost.
3. All edges are sorted by cost.
4. A Union-Find data structure is used to greedily build a minimum-cost configuration ensuring all dynos can access at least one bucket.
5. The MST stops when all dynos are connected (directly or indirectly) to the virtual bucket node.

---

Input Format
The program prompts for an input file with the following format:

n k bucket_cost bond_cost
u1 v1
u2 v2
...
uk vk

- n: Number of dynos (1 to n)
- k: Number of possible bonds
- bucket_cost: Cost to host a bucket
- bond_cost: Cost to create a bond
- Each of the next k lines contains two integers ui vi representing a valid bond between dynos.

Example:
6 5 4 3
1 2
1 3
4 5
6 4
2 3

---

Output Format
The program outputs a single integer representing the minimum cost configuration.

Example Output:
20

---

How to Run
1. Ensure you have Python 3 installed.
2. Save the code as assign1.py.
3. Open a terminal and run the script:
   python assign1.py
4. When prompted, enter the absolute path to your input file.

---

Algorithm Used
- Kruskal’s Algorithm (Greedy MST)
- Union-Find with path compression and union by rank

Time Complexity:
- Edge sorting: O(E log E)
- Union-Find operations: O(α(N)) ~ constant
- Overall: O(E log E) where E = n + k

---

Files
- assign1.py: Main Python source code
- Input text file (user-provided)
- README.txt: This file

---

Bonus (Not Implemented)
- Count all minimum cost configurations.
- Visualize one optimal configuration.

---

Academic Honesty
This solution is entirely original and adheres to the academic integrity policies outlined in the assignment. All algorithms and data structures are implemented from scratch.
