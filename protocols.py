import numpy as np

class B92:
    def __init__(self, n_bits=20):
        self.n_bits = n_bits
        self.alice_bits = np.random.randint(2, size=n_bits)

    def measure(self, bob_bases):
        results = []
        for abit, bbase in zip(self.alice_bits, bob_bases):
            if abit == bbase:
                results.append(abit)
            else:
                results.append(np.random.randint(2))
        return results

class E91:
    def __init__(self, n_pairs=20):
        self.n_pairs = n_pairs
        self.pairs = [(np.random.randint(2), np.random.randint(2)) for _ in range(n_pairs)]

    def measure(self):
        alice_results = [a for a, b in self.pairs]
        bob_results = [b for a, b in self.pairs]
        return alice_results, bob_results
    