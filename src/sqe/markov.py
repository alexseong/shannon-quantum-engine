import numpy as np
from typing import Union, List

class QuantumMarkovModel:
    """
    Classical-to-Quantum Markov Transition Engine.
    Translate classical stochastic processes into quantum density matrix evolutions.
    """

    def __init__(self, states_count: int):
        self.n = states_count
        # Set Ground State to |0><0| at initial state
        self.density_matrix = np.zeros((self.n, self.n), dtype=complex)
        self.density_matrix[0, 0] = 1.0 + 0.j

    def from_classical_distribution(self, distribution: np.ndarray):
        """
        [Connection to my research from 30 years ago]
        Convert a classical probability distribution(Markov state) into a diagonal density matrix
        rho = sum(p_i|i><i|)
        """
        if not np.isclose(np.sum(distribution), 1.0):
            raise ValueError("Distribution must sum to 1.0")
            
        self.density_matrix = np.diag(distribution.astype(complex))
        return self.density_matrix

    def get_von_neumann_entropy(self) -> float:
        """
        Compute Quantum Entropy (Quantum version of Shannon Entropy)
        S(rho) = -Tr(rho * log(rho))
        """ 
        # Compute Eigenvalues
        eignvalues = np.linalg.eigvals(self.density_matrix)
        # Preventing the calculation of the logarithm of a zero eigenvalue (mathematical rigor)
        ev = eignvalues[eignvalues > 1e-15]

        return -np.real(np.sum(ev * np.log(ev)))

    def apply_transition(self, transition_matrix: np.ndarray):
        """
        Apply the classical transition matrix P using quantum operations.
        Note: This step involves "simulating" the classical transition in a quantum context.
        The extension to actual quantum channels(Kraus Operators) will be performed in the next step. 
        """
        # v_{t+1} = v_t * P (implementing the classical transition maxtrix) 
        current_dist = np.diag(self.density_matrix)
        next_dist = np.dot(current_dist, transition_matrix)
        # self.density_matrix = np.diag(next_dist)
        return self.density_matrix

if __name__ == "__main__":
    qmm = QuantumMarkovModel(states_count=3)
    # Search pattern probabilities: [Main Page, Search Result, Detail Page]
    pattern = np.array([0.5, 0.3, 0.2])

    rho = qmm.from_classical_distribution(pattern)
    entropy = qmm.get_von_neumann_entropy()

    print(f"QUantum Density Matrix:\n{rho}")
    print(f"Von Neumann Entropy: {entropy:.4f}")
