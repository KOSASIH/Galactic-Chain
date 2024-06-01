import qiskit
from qiskit import QuantumCircuit, execute
from qiskit.providers.aer import AerSimulator

class QuantumAI:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.model = None

    def build_model(self):
        qc = QuantumCircuit(5, 2)
        qc.h(range(5))
        qc.barrier()
        qc.measure(range(5), range(2))
        return qc

    def train(self):
        self.model = self.build_model()
        simulator = AerSimulator()
        job = execute(self.model, simulator, shots=1024)
        result = job.result()
        counts = result.get_counts(self.model)
        return counts

    def evaluate(self, X_test, y_test):
        counts = self.train()
        accuracy = 0
        for x, y in zip(X_test, y_test):
            if counts[x] > counts[y]:
                accuracy += 1
        return accuracy / len(X_test)
