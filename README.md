# **Algebraic Formulation of the Collatz Operator in Jacobsthal Space: The $3J+J(0,1)$ Transformation**

**Hiroshi Harada - October 14, 2026**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23367384.svg)](https://doi.org/10.5281/zenodo.23367384)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Document: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

## **Overview**

This repository provides the research paper and reproducible Python implementation for algebraically formulating the scalar operation $3n+1$ in the Collatz conjecture as an affine transformation of a spinor (column vector) in Jacobsthal (J) space.

By representing an odd node $b$ and its internal state $a$ as a J-spinor $J(a,b)$, we define the Collatz operation as the following affine transformation:

$$3J(a,b)+J(0,1)$$

This formulation clarifies the algebraic behavior of the additive noise "+1" in the Collatz process. Furthermore, we demonstrate that the trivial loop of the Collatz orbit can be described as a fixed-point structure in J-space:

$$1 \rightarrow 4 \rightarrow 1$$

This study aims to provide a fundamental algebraic framework for analyzing the Collatz space as a dynamical system.

---

## **Contents**

### **`REPORT_EN.pdf` / `REPORT_JP.pdf`**

Research reports (English and Japanese versions) summarizing the theoretical framework of this study.

**Topics covered:**

- Definition of J-Spinor
- The $3J+J(0,1)$ Affine Transformation
- Phase Shift
- J-space 2-adic Reduction
- J Equivalence Class
- Fixed-Point Structure

---

### **`code_01_collatz_3j1.py`**

A Python script implementing the transformation below and the **J-space 2-adic Reduction** defined in the paper:

$$3J+J(0,1)$$

Starting from a specified odd node, it computes the Collatz orbit within J-space.

---

## **Key Concepts**

### **1. J-Spinor and Affine Transformation**

An odd node $b$ and its internal state $a$ are defined as a two-component column vector:

$$
J(a,b)
= \begin{pmatrix} a\\ b \end{pmatrix}
$$

The Collatz operation is expressed by the following affine transformation:

$$3J(a,b)+J(0,1)$$

---

### **2. J-space 2-adic Reduction**

In the standard Collatz calculation, the $3n+1$ operation is followed by division by $2^k$.

In J-space, we introduce the **Reduced Spinor** to perform the equivalent role.

The reduced spinor is defined by recursively descending the J-hierarchy to the state immediately before leaving the integer J-space and generating a rational (fractional) spinor upon the next reduction.

This reduced spinor serves as the representative element of its corresponding J equivalence class.

---

### **3. J Equivalence Class**

A set of J-sequences sharing the same reduced spinor is defined as a **J Equivalence Class**.

**Example:**

The odd values appearing at even indices of the $J(0,1)$ sequence share the same reduced spinor $J(0,1)$ and thus belong to the same J equivalence class:

$$J(0,1) = 0,1,1,3,5,11,21,43,85,\dots$$

$$J(0,1)_{even} = 1,5,21,85,\dots$$

---

### **4. Fixed-Point Structure**

For the terminal point $J(0,1)$, the following relation holds:

$$3J(0,1)+J(0,1) = 4J(0,1)$$

Therefore, $J(0,1)$ acts as an eigenvector of this transformation with an eigenvalue of $4 = 2^2$.

This can be interpreted as a fixed-point structure that algebraically describes the trivial loop of the Collatz orbit:

$$1 \rightarrow 4 \rightarrow 1$$

---

## **Note on the Normalization Algorithm**

The **Shift & Cut Normalization** employed in this implementation is not an externally introduced heuristic method.

It is a normalization rule derived directly from the recursive structure inherent in the recurrence relation of the J-sequence:

$$J_n = J_{n-1} + 2J_{n-2}$$

Accordingly, J-space 2-adic Reduction is not an ad-hoc rule, but an implementation of the intrinsic dynamics of Jacobsthal space.

---

## **Usage**

### **Requirements**

- Python 3.x
- pandas

Installation:

```bash
pip install pandas
```

---

### **Execution**

```bash
python code_01_collatz_3j1.py
```

---

### **Setting the Initial Node**

Modify the following variable at the end of the script to any desired odd integer:

```python
start_node = 7
```

Example:

```python
start_node = 27
```

---

### **Output**

Running the script performs the following actions:

- Outputs the orbit table in Markdown format to the console
- Automatically generates a CSV file

**Generated CSV filename:**

```text
collatz_orbit_<start_node>.csv
```

**Examples:**

```text
collatz_orbit_7.csv
collatz_orbit_27.csv
collatz_orbit_871.csv
```

The CSV file records the following columns:

- Odd Node
- Reduced J (Input)
- 3J+J(0,1)
- k
- Mapped J
- Reduced J (Output)

---

## **License**

- **Research Document:** CC BY 4.0
- **Python Source Code:** MIT License

Copyright (c) 2026 Hiroshi Harada
