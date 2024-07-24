import matplotlib.pyplot as plt

# Data for 271,101 rows
rows_271101 = {
    "Linear Search": 60.1465,
    "Aho-Corasick": 207.8094,
    "Regex Search": 211.9788,
    "Binary Search": 315.0124,
    "Knuth-Morris-Pratt": 2774.4545,
    "Rabin-Karp": 3600.3992
}

# Data for 224 rows
rows_224 = {
    "Linear Search": 0,
    "Aho-Corasick": 0.935555,
    "Regex Search": 0,
    "Binary Search": 0,
    "Knuth-Morris-Pratt": 7.528305054,
    "Rabin-Karp": 7.723808
}

# Plotting
algorithms = list(rows_271101.keys())
times_271101 = list(rows_271101.values())
times_224 = list(rows_224.values())

x = range(len(algorithms))

plt.figure(figsize=(14, 7))

plt.plot(x, times_271101, marker='o', label="271,101 rows")
plt.plot(x, times_224, marker='o', label="224 rows")

plt.xticks(x, algorithms, rotation=45)
plt.xlabel("Algorithms")
plt.ylabel("Execution Time (ms)")
plt.title("Performance Comparison of Search Algorithms")
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()
