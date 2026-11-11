# LoopSentinel: Sound Infinite-Loop Detection & Termination Verification within Turing Computability Limits

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Course](https://img.shields.io/badge/Course-21CSC301T%20FLA-orange.svg)](https://www.srmist.edu.in/)
[![Assessment](https://img.shields.io/badge/CLA--2-Task%204%20Teamwork-green.svg)](#)
[![Tests](https://img.shields.io/badge/Tests-14%2F14%20Passing-brightgreen.svg)](#)
[![Soundness](https://img.shields.io/badge/Soundness%20Sweep-2500%2F2500%20Verified-success.svg)](#)
[![Theory](https://img.shields.io/badge/Computability-Undecidable%20(Rice's%20Theorem)-red.svg)](#)

> **Continuous Learning Assessment – 2 (CLA-2) | Assessment Task 4**  
> **Course:** 21CSC301T – Formal Language and Automata  
> **Department:** Artificial Intelligence and Machine Learning (AIML), School of Computing  
> **Institution:** SRM Institute of Science and Technology, Tiruchirappalli – 621105  
> **Faculty Guide:** Dr. C. Gunasundari (Assistant Professor, Dept. of AIML)  
> **Date:** November 2026  

---

## 👥 Team Details & Role Distribution

| Team Member | Register Number | Role (per Course Guidelines) | Primary Responsibilities |
| :--- | :--- | :--- | :--- |
| **C. Manoj Reddy** | `RA2411026050038` | **Modelling and Analysis** | Formal TM reduction, SentinelLang grammar & 3-address compiler, undecidability proofs, diagonal construction engine, static ranking analysis rules, finite-state automata model. |
| **K. Divakar** | `RA2411026050022` | **Validation & Empirical Testing** | Benchmark ground-truth curation (16 programs), automated test runner, 2,500-program soundness sweep, watchdog comparison, Turing machine transition traces. |
| **P. Charan Kumar** | `RA2411026050057` | **Documentation & Tooling** | GitHub repository architecture, README.md, CONTRIBUTIONS.md, pipeline and computability hierarchy diagrams, final consolidated LaTeX/ReportLab academic report, presentation evidence. |

---

## 📌 Executive Summary

Every software developer has experienced an unresponsive application hanging indefinitely, wondering: *Is the program genuinely stuck in an infinite loop, or is it merely progressing slowly?*

This project investigates **Infinite-Loop Detection in Software** through the formal foundations of **Turing Machines** and the **Theory of Computability**:
1. **Formal Formulation:** We formulate loop detection as language membership in $\text{LOOP} = \overline{\text{HALT}_{\text{TM}}}$.
2. **Impossibility Proof:** Using Turing's classical diagonal construction, we prove that no general exact algorithmic decider can exist for all programs.
3. **Complexity Asymmetry:** We demonstrate that while $\text{HALT}_{\text{TM}}$ is Turing-recognizable ($\mathcal{RE}$), $\text{LOOP}$ is non-recognizable ($\text{co-}\mathcal{RE}$ only), and general semantic properties ($\text{TOTAL}_{\text{TM}}$, Program Equivalence) are outside both classes by **Rice's Theorem**.
4. **Engineering Solution — LoopSentinel:** Since an exact general decider is mathematically impossible, we design **LoopSentinel**, a sound three-stage verification engine for an imperative language compiled to an abstract register machine:
   - **Stage 1 (Static Analysis):** Floyd linear ranking functions ($R(s) > 0, \Delta R \le -c$) and Gupta recurrent non-termination invariants.
   - **Stage 2 (Dynamic Cycle Detection):** Exact instantaneous state memoization ($\langle PC, \vec{v} \rangle$) on deterministic execution paths.
   - **Stage 3 (Finite Hardware Automata):** Fixed $k$-bit modular model checking ($|PC| \times 2^{k \cdot |\text{vars}|}$ state bound via Pigeonhole Principle).
   - **Honest Logic:** Emits certified proofs for `HALTS` and `LOOPS`, while honestly answering `UNKNOWN` when undecidable bounds are hit.

---

## 🚀 Key Results & Benchmark Comparison

We evaluated LoopSentinel against a curated 16-program benchmark representing terminating loops, common software bugs (wrong counter updates, Euclidean zero-division bugs), and non-terminating loops, comparing against an industrial-style timeout watchdog (50,000-step threshold):

| Metric | LoopSentinel (Integrated) | Static Stage Alone | Naive Watchdog (50k steps) |
| :--- | :---: | :---: | :---: |
| **Correctly Decided** | **15 / 16** | 10 / 16 | 15 / 16* |
| **Honest UNKNOWN** | **1** (`doubling`) | 6 | 0 |
| **False-Positive Errors** | **0** (100% Sound) | **0** (100% Sound) | **1** (`busy_wait` misclassified) |
| **Proof Provided** | Certified Math Proof | Certified Math Proof | None (Heuristic guess) |

> **Crucial Takeaway:** A 50,000-step timeout watchdog misdiagnoses `busy_wait` (a correct loop requiring 1,000,000 steps) as an infinite loop! LoopSentinel's static stage immediately proves it terminates using its linear ranking function $R(s) = 1,000,000 - \text{counter}$. Furthermore, LoopSentinel honestly reports `UNKNOWN` on `doubling` ($x = x \times 2$), where values grow exponentially on unbounded integers without repeating a state.

---

## 🛠️ Repository Architecture

```text
FLA-Task4-Infinite-Loop-Detection/
├── loopsentinel/              # Core Verification Package
│   ├── __init__.py           # Package exports & metadata
│   ├── machine.py            # AST parser, 3-address IR compiler, register machine interpreter
│   ├── analyzer.py           # Multi-stage verification engine (static + cycle + k-bit)
│   ├── diagonal.py           # Executable diagonal adversary generator & candidate deciders
│   ├── tm.py                 # 1-tape formal Turing Machine simulator with ID cycle detection
│   ├── programs.py           # Curated 16-program benchmark with hand-verified ground truth
│   └── cli.py                # Command-line interface for demo, benchmark & explain modes
├── tests/                    # Automated Test Suite
│   ├── test_machine.py       # IR compilation and abstract machine tests
│   ├── test_analyzer.py      # Static analysis, ranking functions, and bug proofs
│   ├── test_diagonal.py      # Diagonal proof adversarial contradiction tests
│   ├── test_tm.py            # Turing machine halting, cycle, and runaway tests
│   └── test_soundness_sweep.py # 2,500-program automated soundness fuzzing sweep
├── docs/                     # Documentation & Deliverables
│   ├── diagrams/             # High-resolution architectural and computability diagrams
│   └── presentation/         # Team presentation slide outline and speaker notes
├── run_tests.py              # Zero-dependency standard library test runner
├── README.md                 # Project documentation
├── CONTRIBUTIONS.md          # Individual contribution statements and signoff
└── LICENSE                   # MIT License
```

---

## ⚡ Quickstart & Reproducibility

### 1. Clone & Run All Demonstrations
```bash
git clone https://github.com/ManojReddy-AD/FLA-Task4-Infinite-Loop-Detection.git
cd FLA-Task4-Infinite-Loop-Detection

# Run theory demo, Turing machine simulations, and benchmark suite
python3 -m loopsentinel.cli all
```

### 2. Inspect a Specific Bug (Step-by-Step Explanation)
```bash
# Analyze Euclid's subtraction GCD bug on a=0, b=5:
python3 -m loopsentinel.cli explain gcd_zero_bug

# Analyze counter update bug showing unbounded integers vs 8-bit hardware:
python3 -m loopsentinel.cli explain wrong_direction
```

### 3. Run Automated Soundness Suite (2,500 Programs)
```bash
python3 run_tests.py
```

---

## 🏛️ Alignment with Sustainable Development Goals (SDG)

* **SDG 9: Industry, Innovation, and Infrastructure**
* **Integration Level:** Level 2 (Design Alignment)
* **Impact:** Infinite loops, hanging threads, and runaway computations exhaust critical industrial compute resources, degrade public cloud availability, and trigger catastrophic failure in cyber-physical systems. LoopSentinel provides sound formal verification methods for safety-critical embedded systems and cloud microservices, preventing software hangs while respecting fundamental computability limits.
