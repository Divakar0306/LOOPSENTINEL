# INDIVIDUAL CONTRIBUTION STATEMENTS

**Continuous Learning Assessment – 2 (CLA-2) | Assessment Task 4**  
**Course:** 21CSC301T – Formal Language and Automata  
**Faculty Handling:** Dr. C. Gunasundari (Assistant Professor, Dept. of AIML)  
**School of Computing, SRM Institute of Science and Technology, Tiruchirappalli**  
**Academic Year:** 2026–2027 | **Semester:** V | **Section:** A  

---

### 1. C. Manoj Reddy (`RA2411026050038`) — Modelling and Analysis
* **Primary Role:** Theoretical modeling, computational reduction, and static analysis engine design.
* **Specific Contributions:**
  1. Formulated the formal mapping between real-world programs and Turing Machines, defining the decision languages $\text{HALT}_{\text{TM}}$, $\text{LOOP} = \overline{\text{HALT}_{\text{TM}}}$, and $\text{TOTAL}_{\text{TM}}$.
  2. Drafted the formal undecidability proof via Turing diagonalization and established the recognizability asymmetry ($\text{HALT} \in \mathcal{RE}$, $\text{LOOP} \notin \mathcal{RE}$).
  3. Designed SentinelLang's grammar and implemented the Python AST parser and 3-address register machine compiler (`loopsentinel/machine.py`).
  4. Formulated and implemented the static verification rules in `loopsentinel/analyzer.py`, including Floyd linear ranking functions ($R(s) = \text{bound} - \text{var}$, $\Delta R \le -c$) and Gupta recurrent non-termination invariants.
  5. Built the $k$-bit modular register model to demonstrate the theoretical boundary where finite memory transforms undecidable computations into decidable finite automata.

### 2. K. Divakar (`RA2411026050022`) — Validation and Empirical Testing
* **Primary Role:** Benchmark curation, empirical test suite implementation, and soundness verification.
* **Specific Contributions:**
  1. Assembled and verified ground truth for the 16-program benchmark suite (`loopsentinel/programs.py`), covering standard loops, classic bugs, Euclid's subtraction GCD with zero edge cases, Collatz sequences, and exponential growth.
  2. Implemented the formal 1-tape deterministic Turing Machine simulator (`loopsentinel/tm.py`) with Instantaneous Description (ID) history tracking, validating the binary incrementer, two-state oscillator, and runaway writer.
  3. Engineered the adversarial diagonalization testing module (`loopsentinel/diagonal.py`), verifying contradiction against four candidate deciders ($H_{\text{optimist}}$, $H_{\text{pessimist}}$, $H_{\text{syntax}}$, $H_{\text{timeout}}$).
  4. Designed the automated 2,500-program soundness sweep in `tests/test_soundness_sweep.py`, proving that no static `HALTS` verdict failed to terminate and no static `LOOPS` verdict halted (0% false positives).
  5. Implemented the comparison harness against industrial-style timeout watchdogs, proving that fixed timeouts generate false-positive errors on slow terminating tasks (`busy_wait`).

### 3. P. Charan Kumar (`RA2411026050057`) — Documentation, Architecture and Tooling
* **Primary Role:** Repository architecture, system documentation, visual diagrams, and formal report synthesis.
* **Specific Contributions:**
  1. Architected the complete GitHub repository structure, standardizing modular packaging, CLI endpoints, and zero-dependency test execution.
  2. Authored the comprehensive project `README.md`, detailing problem formulation, theoretical proofs, CLI usage, benchmark tables, and SDG 9 alignment.
  3. Generated publication-quality vector diagrams (`docs/diagrams/`): Fig. 1 (Problem Mapping), Fig. 2 (Computability Hierarchy Venn Diagram), and Fig. 4 (LoopSentinel Architecture Flowchart).
  4. Prepared high-fidelity terminal execution evidence and screenshots for the CLI demonstration, step-by-step bug explanations, and benchmark runs.
  5. Typeset and compiled the consolidated 21-page academic report in strict accordance with SRMIST university standards and the reference structural template.
  6. Prepared the team presentation slides outline and speaker notes (`docs/presentation/presentation_outline.md`).

---

### Team Verification & Attestation

We hereby attest that the work documented in this repository and report is our original collective effort, carried out under the academic supervision of Dr. C. Gunasundari. All team members actively participated in the model design, code verification, benchmark evaluation, and final report review.

* **C. Manoj Reddy (RA2411026050038)** — *Signed*
* **K. Divakar (RA2411026050022)** — *Signed*
* **P. Charan Kumar (RA2411026050057)** — *Signed*

*Place: Tiruchirappalli*  
*Date: November 2026*
