# -*- coding: utf-8 -*-
"""code_01_collatz_3j1.ipynb
"""

"""
Algebraic Formulation of the Collatz Operator in Jacobsthal Space:
The 3J + J(0,1) Transformation

Author: Hiroshi Harada
Date: October 14, 2026
License: MIT License
Copyright (c) 2026 Hiroshi Harada
"""

import pandas as pd

def get_next_collatz(n):
    """Calculate the next odd node in the standard Collatz sequence."""
    n = 3 * n + 1
    while n % 2 == 0:
        n //= 2
    return n

def reduce_to_minimum_spinor(a, b):
    """
    Traverse down the Jacobsthal hierarchy to find the reduced spinor.
    This acts as the J-space 2-adic reduction to extract the representative element.
    """
    while (b - a) % 2 == 0:
        a_prev = (b - a) // 2
        if a_prev < 0:
            break
        b = a
        a = a_prev
    return a, b

def normalize_spinor(A, B):
    """
    The Shift & Cut Normalization algorithm.
    Maps an unnormalized spinor (containing even nodes) to a normalized
    odd spinor without generating fractions, resolving phase shifts in J-space.
    """
    u, v = A, B
    k = 0
    while v % 2 == 0:
        if u % 2 == 0:
            # If the root is even, apply a direct shift down (halve both).
            u //= 2
            v //= 2
        else:
            # If the root is odd, halving generates a fraction.
            # Truncate the root, generate the next term (v + 2u), and halve.
            # Thus: (v + 2u) // 2 = (v // 2) + u
            new_u = v // 2
            new_v = (v // 2) + u
            u, v = new_u, new_v
        k += 1
    return u, v, k

def generate_orbit_table(start_n):
    """
    Generate the complete Collatz orbit data mapped into Jacobsthal space
    using the 3J + J(0,1) transformation and spinor reduction.
    """
    n = start_n
    data = []
    step = 1

    while True:
        # 1. Define standard spinor
        std_a = (n + 1) // 2
        std_b = n

        # 2. Extract Reduced Spinor (Input) via 2-adic reduction
        min_in_a, min_in_b = reduce_to_minimum_spinor(std_a, std_b)

        # 3. Apply the 3J + J(0,1) Affine Transformation
        calc_a = 3 * min_in_a
        calc_b = 3 * min_in_b + 1

        # 4. Map to the correct odd node hierarchy via Shift & Cut normalization
        mapped_a, mapped_b, k = normalize_spinor(calc_a, calc_b)

        # 5. Extract Reduced Spinor (Output) for the next step
        min_out_a, min_out_b = reduce_to_minimum_spinor(mapped_a, mapped_b)

        data.append({
            "Step": step,
            "Odd Node": n,
            "Reduced J (Input)": f"J({min_in_a}, {min_in_b})",
            "3J+J(0,1)": f"J({calc_a}, {calc_b})",
            "k": k,
            "Mapped J": f"J({mapped_a}, {mapped_b})",
            "Reduced J (Output)": f"J({min_out_a}, {min_out_b})"
        })

        if n == 1:
            break

        n = get_next_collatz(n)
        step += 1

    return pd.DataFrame(data)

if __name__ == "__main__":
    # Set the starting odd node
    start_node = 7

    print(f"Calculating Collatz orbit for n = {start_node}...")
    df_orbit = generate_orbit_table(start_node)

    # Output to console
    print("\nOrbit Data:")
    print(df_orbit.to_markdown(index=False))

    # Save the dataframe to a CSV file dynamically based on the starting node
    csv_filename = f"collatz_orbit_{start_node}.csv"
    df_orbit.to_csv(csv_filename, index=False)

    print(f"\n[Success] The result has been saved to '{csv_filename}'")

