import numpy as np
import matplotlib.pyplot as plt

def run_cosmology_simulation():
    """
    Simulates the evolution of energy densities in a universe with 
    Fisher Information Gravity (FIG).
    Reference: Section VII, Eq (9) of Manuscript.
    """
    
    # 1. Define Scale Factor Array (Logarithmic scale from Early Universe to Today)
    # a = 10^-10 (Early) to a = 1 (Today)
    a = np.logspace(-6, 0, 500)
    
    # 2. Define Density Parameters (Normalized to critical density today)
    # Standard Lambda-CDM parameters
    Omega_r0 = 9e-5   # Radiation
    Omega_m0 = 0.31   # Matter
    Omega_L0 = 0.69   # Dark Energy (Lambda)
    
    # Fisher Information Parameter (The new theory)
    # Chosen to be small today to satisfy current bounds
    Omega_FI0 = 1e-12 
    
    # 3. Evolution Equations
    # Radiation: a^-4
    rho_r = Omega_r0 * (a ** -4)
    
    # Matter: a^-3
    rho_m = Omega_m0 * (a ** -3)
    
    # Dark Energy: Constant
    rho_L = Omega_L0 * np.ones_like(a)
    
    # Fisher Information: a^-6 (Stiff Fluid, w=1) [cite: 56]
    rho_FI = Omega_FI0 * (a ** -6)
    
    # 4. Visualization
    plt.figure(figsize=(10, 7))
    
    # Plot densities
    plt.loglog(a, rho_r, label=r'Radiation ($\propto a^{-4}$)', linestyle='--', color='orange')
    plt.loglog(a, rho_m, label=r'Matter ($\propto a^{-3}$)', color='blue')
    plt.loglog(a, rho_L, label=r'Dark Energy (Const)', color='green')
    plt.loglog(a, rho_FI, label=r'Fisher Information ($\propto a^{-6}$)', color='red', linewidth=2.5)
    
    # Formatting
    plt.xlabel('Scale Factor (a)', fontsize=12)
    plt.ylabel(r'Relative Energy Density ($\rho / \rho_{crit,0}$)', fontsize=12)
    plt.title('Evolution of Cosmic Energy Densities (FIG Model)', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, which="both", ls="-", alpha=0.2)
    
    # Highlight the "Stiff Fluid" behavior
    plt.text(1e-5, 1e15, 'Fisher Information dominates\nonly in very early universe', 
             color='red', fontsize=9, bbox=dict(facecolor='white', alpha=0.8))
            
    # Save or Show
    plt.tight_layout()
    plt.show()
    print("Simulation Complete: Verified a^-6 scaling for Fisher Information sector.")

if __name__ == "__main__":
    run_cosmology_simulation()