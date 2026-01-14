# Optimization – Linear Programming (LP) Budget Allocation

## Project Overview
This mini-project formulates a **marketing budget allocation** problem as a **Linear Programming (LP)** optimization task.  
Given a fixed total budget and realistic per-channel constraints, the goal is to **maximize expected return** based on marginal impact coefficients.

This project demonstrates foundational optimization skills:
- Objective function design
- Constraint modeling (equalities + bounds)
- Solving LP using SciPy (`linprog`)
- Interpreting results in a business context

---

## Business Problem
Marketing teams often need to answer:

> *How should we allocate a fixed marketing budget across channels to maximize expected sales/impact under operational constraints?*

---

## LP Formulation

### Decision Variables
Let:
- \( x_{tv} \), \( x_{search} \), \( x_{social} \), \( x_{email} \)  
be the budget allocated to each channel.

### Objective Function
Maximize total expected return:

\[
\max \; 0.028x_{tv} + 0.081x_{search} + 0.052x_{social} + 0.095x_{email}
\]

Coefficients represent **marginal impact per dollar** (can be derived from an MMM regression baseline).

### Constraints
1) **Fixed total budget**
\[
x_{tv} + x_{search} + x_{social} + x_{email} = 35000
\]

2) **Channel bounds (operational constraints)**
- TV: 5000 to 20000  
- Search: 2000 to 12000  
- Social: 1000 to 10000  
- Email: 500 to 5000  

3) **Non-negativity** is enforced via bounds.

---

## Solution Method
SciPy’s `linprog` solves minimization problems, so the objective is converted to minimization by negating coefficients:

\[
\min \; -(0.028x_{tv} + 0.081x_{search} + 0.052x_{social} + 0.095x_{email})
\]

Implementation: `lp_budget_allocation.py`

---

## Results
**Optimized Allocation (LP):**
- TV: **8000**
- Search: **12000**
- Social: **10000**
- Email: **5000**

**Max Objective Value:** **2191.0**

### Interpretation
The optimizer allocates budget to **higher marginal-return channels** (Search, Social, Email) up to their maximum bounds, and assigns the remaining budget to lower-return channels (TV).  
This behavior is expected in linear optimization when coefficients represent constant marginal returns.

---

## Project Structure
optimization-linear-programming/

├── lp_budget_allocation.py

├── requirements.txt

└── README.md

## How to Run

Install dependencies:

pip install -r requirements.txt


Run the solver:
python lp_budget_allocation.py

## Key Takeaways

Formulated a real-world budget allocation problem as a linear program

Modeled constraints using equality + bounds

Solved LP using SciPy and interpreted results for decision-making

Demonstrated optimization fundamentals applicable to finance/marketing analytics

## Future Improvements

Add diminishing returns (non-linear constraints) to model saturation

Extend to multi-period allocation (weekly/monthly planning)

Compare LP results with non-linear optimization used in MMM
