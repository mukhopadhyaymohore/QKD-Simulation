import sys, os, numpy as np
from PySide6.QtCore import QObject, Signal, Slot, QUrl
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from bb84 import BB84
from protocols import B92, E91
from eve import Eve
from cipher import xor_encrypt, xor_decrypt

class BB84Connector(QObject):
    updateResults = Signal(list, list, list, list, list)

    @Slot(str, bool)
    def runProtocol(self, protocolName="BB84", eveEnabled=False):
        if protocolName == "BB84":
            protocol = BB84()
            bob_bases = np.random.randint(2, size=protocol.n_bits)
            if eveEnabled:
                eve = Eve()
                disturbed_bits = eve.intercept(protocol.alice_bits, protocol.alice_bases)
                bob_results = protocol.measure(bob_bases)
            else:
                bob_results = protocol.measure(bob_bases)
            final_key = protocol.sift_key(bob_bases, bob_results)
            alice_bits = [int(x) for x in protocol.alice_bits]
            alice_bases = [int(x) for x in protocol.alice_bases]
            bob_bases = [int(x) for x in bob_bases]
            bob_results = [int(x) for x in bob_results]
            final_key = [int(x) for x in final_key]

        elif protocolName == "B92":
            protocol = B92()
            bob_bases = np.random.randint(2, size=protocol.n_bits)
            bob_results = protocol.measure(bob_bases)
            final_key = bob_results
            alice_bits = [int(x) for x in protocol.alice_bits]
            alice_bases = [0]*protocol.n_bits
            bob_bases = [int(x) for x in bob_bases]
            bob_results = [int(x) for x in bob_results]
            final_key = [int(x) for x in final_key]

        elif protocolName == "E91":
            protocol = E91()
            alice_bits, bob_results = protocol.measure()
            final_key = [a for a, b in zip(alice_bits, bob_results) if a == b]
            alice_bases = [0]*protocol.n_pairs
            bob_bases = [0]*protocol.n_pairs
            final_key = [int(x) for x in final_key]

        # Emit results to QML
        self.updateResults.emit(alice_bits, alice_bases, bob_bases, bob_results, final_key)

        # ✅ Absolute path fix: always write next to main.py
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "final_key.txt")
        with open(file_path, "w") as f:
            f.write("".join(map(str, final_key)))

    @Slot(str, list, result=str)
    def encryptMessage(self, message, key):
        return xor_encrypt(message, key)

    @Slot(str, list, result=str)
    def decryptMessage(self, ciphertext, key):
        return xor_decrypt(ciphertext, key)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    connector = BB84Connector()
    engine.rootContext().setContextProperty("backend", connector)

    # Load UI from project root
    engine.load(QUrl("../ui/main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
