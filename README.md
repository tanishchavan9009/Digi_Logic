# ⚡ DigiLogic — Flip-Flop & Digital Electronics Hub

<div align="center">

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)](https://en.wikipedia.org/wiki/C_(programming_language))
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)

<p align="center">
  <b>An interactive, visual, and gamified web platform for mastering Digital Logic Design, Combinational Circuits (SSI/MSI), and Sequential Flip-Flop Architectures — with native Streamlit Cloud deployment support.</b>
</p>

[Explore Features](#-key-features) • [Streamlit Deploy Guide](#-streamlit-deployment) • [Quick Start](#-quick-start--usage) • [Logic Reference](#-digital-logic-reference-guide) • [Contributing](#-contributing)

</div>

---

## 📖 Table of Contents

- [🌟 Project Overview](#-project-overview)
- [✨ Key Features](#-key-features)
- [📐 Digital Logic Reference Guide](#-digital-logic-reference-guide)
  - [1. Small Scale Integration (SSI) – Logic Gates](#1-small-scale-integration-ssi--logic-gates)
  - [2. Medium Scale Integration (MSI) – Combinational Circuits](#2-medium-scale-integration-msi--combinational-circuits)
  - [3. Sequential Circuits & Flip-Flops](#3-sequential-circuits--flip-flops)
  - [4. Flip-Flop Quick Conversion & Excitation Table](#4-flip-flop-quick-conversion--excitation-table)
- [🎮 Interactive Modules](#-interactive-modules)
  - [⚡ Real-Time Logic Gate Simulator](#-real-time-logic-gate-simulator)
  - [📝 Dynamic MCQ Assessment Engine](#-dynamic-mcq-assessment-engine)
  - [🌙 Responsive Light / Dark Theme Engine](#-responsive-light--dark-theme-engine)
- [📂 Repository Structure](#-repository-structure)
- [🚀 Quick Start & Usage](#-quick-start--usage)
- [💻 C Programming Modules](#-c-programming-modules)
- [🛠️ Tech Stack](#️-tech-stack)
- [🤝 Contributing](#-contributing)
- [📄 License & Authors](#-license--authors)

---

## 🌟 Project Overview

**DigiLogic (Flip-Flop Zone)** bridges the gap between theoretical textbook electronics and intuitive visual learning. Traditional digital electronics pedagogy often suffers from static diagrams and abstract state equations. This repository delivers an all-in-one web-based interactive laboratory where students, educators, and electronics hobbyists can:

- **Simulate** gate-level logic dynamically with immediate truth table generation.
- **Inspect** combinational building blocks (Multiplexers, Demultiplexers, Decoders, Encoders) with vector-based SVG circuit representations.
- **Master** sequential state machines and flip-flop transitions ($SR$, $JK$, $D$, $T$).
- **Test** their comprehension through multi-tier quizzes ranging from fundamental to advanced circuit analysis.

```
       ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
       │   Logic Gates   │ ───> │  Combinational  │ ───> │   Sequential    │
       │   (AND/OR/XOR)  │      │  (MUX/DEMUX/DEC)│      │  (Flip-Flops)   │
       └─────────────────┘      └─────────────────┘      └─────────────────┘
                │                        │                        │
                ▼                        ▼                        ▼
       [ SSI Foundation ]       [ MSI Data Routing ]     [ Memory & State ]
```

---

## ✨ Key Features

| Feature | Description | Highlight |
| :--- | :--- | :--- |
| 🎛️ **Live Gate Simulator** | Toggle inputs $A$ & $B$ and watch outputs change instantaneously with auto-updating truth tables. | Zero-latency DOM updates |
| 🔄 **Flip-Flop State Visualizer** | Interactive tabbed explorer for $SR$, $D$, and $JK$ Flip-Flops with next-state equations. | Memory circuit clarity |
| 🎨 **SVG Circuit Diagrams** | Crisp, scalable vector schematics for $4:1\text{ MUX}$, $1:4\text{ DEMUX}$, and $2:4\text{ Decoders}$. | Retina-sharp UI |
| 🎯 **Gamified Quiz Engine** | 3 difficulty tiers (Easy, Medium, Hard) covering IC numbers, universal gates, and circuit theory. | Instant scoring & review |
| 🌓 **Adaptive Theme Mode** | High-contrast dark mode and clean light mode toggle for late-night study sessions. | Persistent CSS variables |
| 📱 **Fully Responsive** | Optimized grid layouts tailored for mobile, tablet, and desktop screens. | Fluid flex/grid design |

---

## 📐 Digital Logic Reference Guide

### 1. Small Scale Integration (SSI) – Logic Gates

Small Scale Integration (SSI) ICs typically integrate fewer than $10$ to $12$ equivalent logic gates per package.

| Gate | Boolean Expression | Standard IC | Truth Table Summary |
| :--- | :---: | :---: | :--- |
| **AND** | $Y = A \cdot B$ | **IC 7408** | Output is `1` only when **all** inputs are `1`. |
| **OR** | $Y = A + B$ | **IC 7432** | Output is `1` when **any** input is `1`. |
| **NOT** | $Y = \overline{A}$ | **IC 7404** | Inverts the input signal. |
| **NAND** | $Y = \overline{A \cdot B}$ | **IC 7400** | Universal gate; inverse of AND gate. |
| **NOR** | $Y = \overline{A + B}$ | **IC 7402** | Universal gate; inverse of OR gate. |
| **XOR** | $Y = A \oplus B = A\overline{B} + \overline{A}B$ | **IC 7486** | Output is `1` when inputs are **different**. |
| **XNOR** | $Y = \overline{A \oplus B} = AB + \overline{A}\overline{B}$ | **IC 74266** | Output is `1` when inputs are **identical**. |

---

### 2. Medium Scale Integration (MSI) – Combinational Circuits

MSI devices pack $10$ to $100$ logic gates, executing specialized arithmetic and data routing operations without internal state storage:

```
  4:1 Multiplexer (Data Selector)          1:4 Demultiplexer (Data Distributor)
          +---------------+                         +---------------+
    I0 ---|               |                   I --->|               |---> Y0
    I1 ---|               |                         |               |---> Y1
    I2 ---|      MUX      |---> Y                   |     DEMUX     |---> Y2
    I3 ---|               |                         |               |---> Y3
          +-------+-------+                         +-------+-------+
                  |                                         |
               S1 S0 (Select Lines)                      S1 S0 (Select Lines)
```

- **Multiplexer (MUX - IC 74151 / 74153):** Selects one of $2^n$ analog/digital data inputs and forwards it to a single output line using $n$ select lines:
  $$Y = \overline{S_1}\,\overline{S_0}I_0 + \overline{S_1}S_0 I_1 + S_1\overline{S_0}I_2 + S_1 S_0 I_3$$
- **Demultiplexer (DEMUX):** Routes a single input stream to one of $2^n$ output lines based on select lines.
- **Decoder (IC 74138 - 3:8 Decoder):** Converts $n$-bit coded inputs into a maximum of $2^n$ unique active outputs.
- **Encoder (IC 74148 / 74147):** Condenses $2^n$ input data lines into an $n$-bit binary code.

---

### 3. Sequential Circuits & Flip-Flops

Sequential circuits incorporate memory feedback loops. Output is a function of current inputs **and** previous state ($Q_n$).

#### 🔄 SR Flip-Flop (Set-Reset)
- **Characteristic Equation:** $Q_{n+1} = S + R'Q_n \quad (\text{Constraint: } S \cdot R = 0)$

| $S$ | $R$ | $Q_{n+1}$ | State Description |
| :---: | :---: | :---: | :--- |
| `0` | `0` | $Q_n$ | **No Change (Memory)** |
| `0` | `1` | `0` | **Reset** |
| `1` | `0` | `1` | **Set** |
| `1` | `1` | `X` | **Invalid / Forbidden Condition** |

---

#### 🔄 JK Flip-Flop (Universal Sequential Cell)
- **Characteristic Equation:** $Q_{n+1} = J\overline{Q_n} + \overline{K}Q_n$
- Resolves the $S=R=1$ race condition by toggling the output state.

| $J$ | $K$ | $Q_{n+1}$ | State Description |
| :---: | :---: | :---: | :--- |
| `0` | `0` | $Q_n$ | **No Change** |
| `0` | `1` | `0` | **Reset** |
| `1` | `0` | `1` | **Set** |
| `1` | `1` | $\overline{Q_n}$ | **Toggle** |

---

#### 🔄 D Flip-Flop (Data / Delay)
- **Characteristic Equation:** $Q_{n+1} = D$
- Eliminates invalid states; widely used in shift registers and CPU cache pipelines.

| $D$ | $Q_{n+1}$ | State Description |
| :---: | :---: | :--- |
| `0` | `0` | **Reset to 0 on clock edge** |
| `1` | `1` | **Set to 1 on clock edge** |

---

#### 🔄 T Flip-Flop (Toggle)
- **Characteristic Equation:** $Q_{n+1} = T \oplus Q_n$
- Fundamental building block for asynchronous and synchronous binary counters.

| $T$ | $Q_{n+1}$ | State Description |
| :---: | :---: | :--- |
| `0` | $Q_n$ | **Hold State** |
| `1` | $\overline{Q_n}$ | **Invert / Toggle State** |

---

### 4. Flip-Flop Quick Conversion & Excitation Table

When designing counters or state machines, use this excitation lookup matrix:

| $Q_n \rightarrow Q_{n+1}$ | $S$ | $R$ | $J$ | $K$ | $D$ | $T$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$0 \rightarrow 0$** | `0` | `X` | `0` | `X` | `0` | `0` |
| **$0 \rightarrow 1$** | `1` | `0` | `1` | `X` | `1` | `1` |
| **$1 \rightarrow 0$** | `0` | `1` | `X` | `1` | `0` | `1` |
| **$1 \rightarrow 1$** | `X` | `0` | `X` | `0` | `1` | `0` |

*(Where `X` denotes a Don't Care condition)*

---

## 🎮 Interactive Modules

### ⚡ Real-Time Logic Gate Simulator
Built with a dynamic vanilla JS evaluator that executes bitwise operators in real-time:

```javascript
function logicGate(a, b, type) {
    switch(type) {
        case "AND":  return a & b;
        case "OR":   return a | b;
        case "NAND": return !(a & b) ? 1 : 0;
        case "NOR":  return !(a | b) ? 1 : 0;
        case "XOR":  return a ^ b;
    }
}
```

### 📝 Dynamic MCQ Assessment Engine
- 3 difficulty categories with real-time DOM injection and score tallying.
- Immediate feedback highlighting mastery in Combinational and Sequential concepts.

### 🌙 Responsive Light / Dark Theme Engine
- Smooth CSS backdrop filters and customizable theme palettes with zero layout shift.

---

## 📂 Repository Structure

```text
📦 FLIP-FLOP
 ┣ 📜 app.py                # Streamlit Web Application (Full Suite + Native Simulators)
 ┣ 📜 requirements.txt      # Python Dependencies for Streamlit Deployment
 ┣ 📜 cppsdeco.html         # Interactive Learning & Simulation Engine (HTML5/CSS3/JS)
 ┣ 📜 index.html            # Portal Entry Page
 ┣ 📜 structure_book.c      # C Data Structures & Sorting Demonstration
 ┣ 📜 structure_book.exe    # Compiled executable for book struct manager
 ┣ 📜 flip-flop code.zip    # Archived project assets and starter templates
 ┗ 📜 README.md             # Project documentation and digital logic manual
```

---

## 🚀 Quick Start & Usage

### 🎈 Option 1: Run with Streamlit (Recommended)
Experience the full interactive dashboard including live gate simulations, sequential clock lab, and embedded web suite:

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch Streamlit app:**
   ```bash
   streamlit run app.py
   ```
   *Your browser will automatically open `http://localhost:8501`.*

---

### 🌐 Option 2: Run Standalone HTML Web App
No build tools, bundlers, or Python required!

1. **Launch in your default browser:**
   - **Windows (PowerShell):**
     ```powershell
     Start-Process .\cppsdeco.html
     ```
   - **macOS:**
     ```bash
     open cppsdeco.html
     ```
   - **Linux:**
     ```bash
     xdg-open cppsdeco.html
     ```
   - Or open with VS Code's **Live Server** extension.

---

## ☁️ Streamlit Cloud Deployment Guide

Deploying your DigiLogic project to the web is completely **free** via **Streamlit Community Cloud**:

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "feat: Add Streamlit app and requirements"
   git push origin main
   ```
2. **Visit Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io) and log in with your GitHub account.
3. **Deploy New App:**
   - Click **"New app"** (or **"Create app"**).
   - **Repository:** `tanishchavan9009/Tanish-codes`
   - **Branch:** `main` (or your active branch)
   - **Main file path:** `app.py` (or `FLIP-FLOP/app.py` if in a subfolder)
4. **Click "Deploy!":**
   - Streamlit will automatically install `requirements.txt` and launch your live URL in seconds! 🚀

---

## 💻 C Programming Modules

Alongside web simulations, this repository includes foundational C programs illustrating structured data manipulation and sorting algorithms:

### 📚 `structure_book.c`
Demonstrates custom structs, dynamic user inputs, and exchange sorting algorithms:

```c
struct book {
    char title[30];
    char author[30];
    char genre[20];
    int year;
};
```

**Compile and Run:**
```bash
gcc structure_book.c -o structure_book
./structure_book
```

---

## 🛠️ Tech Stack

<div align="left">

- **Frontend Core:** Vanilla HTML5, Semantic Elements, Modern CSS3 Flexbox/Grid
- **Vector Graphics:** Inline SVG for circuit and gate topology
- **Scripting:** Vanilla JavaScript (ES6+), DOM APIs, IntersectionObserver
- **Systems Programming:** C (C99 Standard / GCC)
- **Design:** Poppins typography, Glassmorphism, CSS Custom Properties

</div>

---

## 🤝 Contributing

Contributions are warmly welcomed! If you would like to expand the project:

1. **Fork** the Repository.
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/Add-Counter-Simulator
   ```
3. **Commit** your enhancements:
   ```bash
   git commit -m "feat: Add 4-bit synchronous counter simulation"
   ```
4. **Push** to your branch:
   ```bash
   git push origin feature/Add-Counter-Simulator
   ```
5. **Open** a Pull Request.

---

## 📄 License & Authors

Distributed under the **MIT License**. See `LICENSE` for more information.

<div align="center">

Crafted with 💡 by **Tanish** & Contributors  
*Empowering digital electronics learners worldwide.*

[![Back to Top](https://img.shields.io/badge/▲-Back_to_Top-00eaff?style=flat-square)](#-digilogic--flip-flop--digital-electronics-hub)

</div>
