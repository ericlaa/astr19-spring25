import numpy as np

def main():
    x_vals = np.linspace(0, 2 * np.pi, 1000)
    sin_vals = np.sin(x_vals)

    print("x\t\tsin(x)")
    print("-" * 25)

    for i in range(len(x_vals)):
        print(f"{x_vals[i]:.6f}\t{sin_vals[i]:.6f}")

if __name__ == '__main__':
    main()
