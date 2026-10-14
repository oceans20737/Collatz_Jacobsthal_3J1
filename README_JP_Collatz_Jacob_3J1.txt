# **Collatz操作のJacobsthal空間における代数的定式化：$3J+J(0,1)$変換**

## **Algebraic Formulation of the Collatz Operator in Jacobsthal Space: The $3J+J(0,1)$ Transformation**

**Hiroshi Harada - October 14, 2026**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Document: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

## **概要 (Overview)**

本リポジトリは、Collatz予想における $3n+1$ というスカラー演算を、Jacobsthal（J）空間におけるスピノル（列ベクトル）のアフィン変換として代数的に定式化した研究論文と、その理論を再現するためのPython実装を公開するものです。

奇数ノード $b$ と内部状態 $a$ を $J(a,b)$ というJスピノルとして表現し、Collatz操作を以下に示すアフィン変換として定義します。

$$3J(a,b)+J(0,1)$$

この定式化により、Collatz操作における加法ノイズ「+1」の代数的な振る舞いが明確化されます。

また、以下に示すCollatz軌道の自明ループを、J空間における不動点構造として記述できることを示します。

$$1 \rightarrow 4 \rightarrow 1$$

本研究は、Collatz空間を力学系として解析するための基礎的な代数フレームワークを提供することを目的としています。

---

## **収録ファイル (Contents)**

### **`REPORT_EN.pdf` / `REPORT_JP.pdf`**

本研究の理論的枠組みをまとめた研究レポート（英語版/日本語版）です。

**内容：**

- J-Spinor の定義
- $3J+J(0,1)$ アフィン変換
- 位相のズレ（Phase Shift）
- J空間2-adic縮約
- J同値類（J Equivalence Class）
- 不動点構造

---

### **`code_01_collatz_3j1.py`**

論文で定義された下記の変換および **J-space 2-adic Reduction** を実装したPythonスクリプトです。

$$3J+J(0,1)$$

指定した奇数ノードから出発し、J空間上で軌道を計算します。

---

## **理論のハイライト (Key Concepts)**

### **1. J-Spinorとアフィン変換**

奇数ノード $b$ と内部状態 $a$ を次のように定義します。

$$
J(a,b)
= \begin{pmatrix} a\\ b \end{pmatrix}
$$

下式によってCollatz操作を表現します。

$$3J(a,b)+J(0,1)$$

---

### **2. J空間2-adic縮約（J-space 2-adic Reduction）**

通常のCollatz計算では、$3n+1$ 計算の後に $2^k$ による除算を行います。

J空間では同様の役割を果たす操作として、**縮約スピノル（Reduced Spinor）** を導入します。

縮約スピノルは、J階層を再帰的に下降し、次の縮約で整数J空間を離れ、有理数スピノルが発生する直前の状態として定義されます。

この縮約スピノルは、そのJ同値類の代表元として機能します。

---

### **3. J同値類（J Equivalence Class）**

同一の縮約スピノルを共有するJ数列の集合を、**J同値類（J Equivalence Class）** と定義します。

**例：**

$J(0,1)$ 数列の偶数項は同一の縮約スピノル $J(0,1)$ を共有するため、同一のJ同値類に属します。

$$J(0,1) = 0,1,1,3,5,11,21,43,85,\dots$$

$$J(0,1)_{even} = 1,5,21,85,\dots$$

---

### **4. 不動点構造（Fixed-Point Structure）**

終着点 $J(0,1)$ について、以下が成立します。

$$ 3J(0,1)+J(0,1) = 4J(0,1) $$

したがって、$J(0,1)$ は本変換の固有ベクトルとなり、固有値は $4 = 2^2$ となります。

これは、以下に示すCollatz軌道の自明ループを代数的に記述する不動点構造として解釈できます。

$$1 \rightarrow 4 \rightarrow 1$$

---

## **正規化アルゴリズムについて**

本実装で用いている **Shift & Cut Normalization** は、外部から導入されたヒューリスティックな手法ではありません。

これは J数列の漸化式に内在する再帰構造から導かれる正規化規則です。

$$J_n = J_{n-1} + 2J_{n-2}$$

したがって、J-space 2-adic Reduction は追加ルールではなく、J空間に内在する力学を実装したものとして解釈されます。

---

## **コードの実行方法 (Usage)**

### **必要要件 (Requirements)**

- Python 3.x
- pandas

インストール：

```bash
pip install pandas
```

---

### **実行 (Execution)**

```bash
python code_01_collatz_3j1.py
```

---

### **初期値の設定**

スクリプト末尾にある下記の箇所を任意の奇数へ変更してください。

```python
start_node = 7
```

例：

```python
start_node = 27
```

---

### **出力 (Output)**

下記が実行されます。

- コンソールへマークダウン形式の軌道表を出力
- CSVファイルを自動生成

**生成されるCSVファイル名：**

```text
collatz_orbit_<start_node>.csv
```

**例：**

```text
collatz_orbit_7.csv
collatz_orbit_27.csv
collatz_orbit_871.csv
```

CSVには以下の情報が記録されます。

- Odd Node
- Reduced J (Input)
- 3J+J(0,1)
- k
- Mapped J
- Reduced J (Output)

---

## **ライセンス (License)**

- **Research Document:** CC BY 4.0
- **Python Source Code:** MIT License

Copyright (c) 2026 Hiroshi Harada
