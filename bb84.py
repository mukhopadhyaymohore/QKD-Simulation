import numpy as np

class BB84:
    def __init__(self, n_bits=20):
        self.n_bits = n_bits
        # Alice generates random bits and bases
        self.alice_bits = np.random.randint(2, size=n_bits)
        self.alice_bases = np.random.randint(2, size=n_bits)  # 0 = rectilinear, 1 = diagonal

    def measure(self, bob_bases):
        """Bob measures photons using his random bases"""
        results = []
        for abit, abase, bbase in zip(self.alice_bits, self.alice_bases, bob_bases):
            if abase == bbase:
                results.append(abit)
            else:
                results.append(np.random.randint(2))
        return results

    def sift_key(self, bob_bases, bob_results):
        """Extract final key where bases match and bits agree"""
        key = []
        for abit, abase, bbase, bresult in zip(self.alice_bits, self.alice_bases, bob_bases, bob_results):
            if abase == bbase and abit == bresult:
                key.append(abit)
        return key
