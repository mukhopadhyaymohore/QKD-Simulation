import numpy as np

class Eve:
    def intercept(self, bits, bases):
        eve_bases = np.random.randint(2, size=len(bits))
        disturbed_bits = []
        for bit, abase, ebase in zip(bits, bases, eve_bases):
            if abase == ebase:
                disturbed_bits.append(bit)
            else:
                disturbed_bits.append(np.random.randint(2))
        return disturbed_bits
