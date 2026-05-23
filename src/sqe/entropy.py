import numpy as np
from scipy.linalg import logm

class QuantumInformationTheory:
    """
    Tools for calculating Quantum Information metrics.
    Focuses on extending Shannon's classical concepts to Quantum states.
    """

    @staticmethod
    def von_neuman_entropy(rho)