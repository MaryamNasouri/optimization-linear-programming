import numpy as np
from scipy.optimize import linprog

def solve_lp_budget_allocation(
    coeffs,
    total_budget,
    bounds
):
    """
    Linear Programming:
    Maximize: coeffs @ x
    Subject to: sum(x) = total_budget
                bounds for each x
    """

    # linprog minimizes, so we minimize negative of objective
    c = -np.array(coeffs)

    # Equality constraint: sum(x) = total_budget
    A_eq = np.ones((1, len(coeffs)))
    b_eq = np.array([total_budget])

    result = linprog(
        c=c,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=bounds,
        method="highs"
    )

    return result

if __name__ == "__main__":
    # Coefficients (marginal impact per dollar) - can be derived from MMM
    coeffs = [0.028, 0.081, 0.052, 0.095]  # TV, Search, Social, Email

    total_budget = 35000

    bounds = [
        (5000, 20000),  # TV
        (2000, 12000),  # Search
        (1000, 10000),  # Social
        (500, 5000)     # Email
    ]

    res = solve_lp_budget_allocation(coeffs, total_budget, bounds)

    if res.success:
        x = res.x
        channels = ["TV", "Search", "Social", "Email"]

        print("Optimized Allocation (LP):")
        for ch, val in zip(channels, x):
            print(f"{ch}: {val:.2f}")

        max_value = -res.fun
        print(f"\nMax Objective Value: {max_value:.4f}")
    else:
        print("Optimization failed:", res.message)
