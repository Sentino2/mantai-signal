---
title: "Computing GR(1) Assume-Guarantee Contracts"
date: 2026-10-27T16:53:25+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.37534v1"
ext_id: "arxiv:2610.37534v1"
tags: ["hardware"]
summary: "Assume-guarantee contracts provide a set of algebraic operations that enable the efficient compositional design and analysis of complex engineering systems. The explicit computation of these operations at component interfaces is currently supported only for some logics lacking a notion of time. This paper develops theory and algorithms to compute these operations when the contracts are expressed i"
---

Assume-guarantee contracts provide a set of algebraic operations that enable the efficient compositional design and analysis of complex engineering systems. The explicit computation of these operations at component interfaces is currently supported only for some logics lacking a notion of time. This paper develops theory and algorithms to compute these operations when the contracts are expressed in the GR(1) modulo theory. The key challenge is the computation of two quantifier elimination problems for temporal formulas. We develop context-aided variable elimination procedures on GR(1)-modulo formulas, establish their soundness, characterize subproblem-wise optimal solutions within an admissible class of formulas, and use the procedures to compute contract operations, including composition and quotient. We implement the resulting framework in Pacti, automating compositional reasoning over GR(1) contracts. Finally, we demonstrate the framework on an automated emergency-braking case study, where we compute system-level contracts and expose compatibility conditions arising from the interaction of component specifications. Experiments on synthetic families show that the cost is governed by the number of eliminated variables and liveness conjuncts, and a comparison with exact automata-based elimination shows complementary scaling.

[Read the original at arXiv →](https://arxiv.org/abs/2610.37534v1)
