# Quantum Key Distribution Simulation (BB84, B92, E91)

This project is a simulation of quantum key distribution protocols (BB84, B92, and E91) with a graphical interface built using **PySide6 (Qt/QML)**.  
It demonstrates how Alice and Bob can establish a shared secret key securely, even in the presence of an eavesdropper (Eve).

---

## ✨ Features
- Simulates **BB84**, **B92**, and **E91** protocols
- Visual comparison of Alice’s and Bob’s bits and bases
- Error rate calculation with progress bar
- Final key extraction and storage (`backend/final_key.txt`)
- Simple XOR-based encryption/decryption demo using the generated key
- Educational step guide explaining the protocol stages

---

## 📂 Project Structure

```text
BB84/
├── backend/
│   ├── bb84.py
│   ├── cipher.py
│   ├── eve.py
│   ├── main.py
│   ├── protocols.py
│   └── final_key.txt
├── ui/
│   ├── main.qml
│   └── components/
│       ├── BarChart.qml
│       └── StepGuide.qml
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements
- Python 3.9+
- PySide6
- NumPy

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Simulation

From the project root (`BB84/`):

```bash
python backend/main.py
```

This will launch the Qt/QML interface.

---

## 📖 How It Works
1. **Alice chooses random bits and bases.**
2. **Bob measures with his bases.**
3. **Mismatched bases are discarded.**
4. **Final key is extracted.**
5. The final key can be used to encrypt/decrypt messages with a simple XOR cipher.

---

## 📜 License
MIT License
