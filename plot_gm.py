import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# ========== Parameters ==========
PARAMS = {
    'a': 0.01,           
    'b': 0.05,            
    'mu': -0.8,            
    'n_points': 100000,  
    'colormap': 'winter', # Colors: 'viridis', 'plasma', 'winter', 'hot'
    'filename': 'gumowski_mira.pdf'  
}
# ================================

def gumowski(x, mu):
    return x * mu + 2 * x * x * (1 - mu) / (1 + x * x)

def trajectory(a, b, mu, n):
    x, y = np.zeros(n), np.zeros(n)
    x[0], y[0] = 0, 0.5  
    
    for i in range(n-1):
        x[i+1] = a * y[i] * (1 - b * y[i] * y[i]) + y[i] + gumowski(x[i], mu)
        y[i+1] = -x[i] + gumowski(x[i+1], mu)
    
    return x, y

def create_plot():
    # strange attractor trajectory
    x, y = trajectory(PARAMS['a'], PARAMS['b'], PARAMS['mu'], PARAMS['n_points'])
    
    
    plt.figure(figsize=(10, 10), facecolor='black')
    colors = np.linspace(0, 1, PARAMS['n_points'])
    plt.scatter(x, y, s=0.1, c=colors, cmap=PARAMS['colormap'], alpha=0.7)
    
    plt.gca().set_facecolor('black')
    plt.axis('off')
    plt.tight_layout()
    
    with PdfPages(PARAMS['filename']) as pdf:
        pdf.savefig(bbox_inches='tight', facecolor='black')
    
    plt.close()
    print(f"Saved as : {PARAMS['filename']}")


if __name__ == "__main__":
    create_plot()
