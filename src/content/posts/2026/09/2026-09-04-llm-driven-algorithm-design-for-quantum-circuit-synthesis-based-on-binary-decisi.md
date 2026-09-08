---
title: "LLM-Driven Algorithm Design for Quantum Circuit Synthesis based on Binary Decision Diagrams"
date: 2026-09-04T16:25:01+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2609.05327v1"
ext_id: "arxiv:2609.05327v1"
tags: ["models"]
summary: "Quantum circuits are central to implementing quantum algorithms on quantum devices, where quantum gates must be reversible. Many quantum algorithms rely on Boolean functions, which must therefore be implemented reversibly within quantum circuits. Reversible circuit synthesis provides a way to translate such Boolean functions into reversible circuits. Binary decision diagrams (BDDs) offer a scalabl"
---

Quantum circuits are central to implementing quantum algorithms on quantum devices, where quantum gates must be reversible. Many quantum algorithms rely on Boolean functions, which must therefore be implemented reversibly within quantum circuits. Reversible circuit synthesis provides a way to translate such Boolean functions into reversible circuits. Binary decision diagrams (BDDs) offer a scalable approach to this task, but the resulting BDDs and circuits depend heavily on variable ordering. Existing ordering heuristics commonly minimize BDD size because it is closely tied to the circuit size. However, BDD size is an imperfect proxy for the quantum cost of the synthesized circuit (QCC). We propose \texttt{QuantumEvo}, an evolutionary framework that uses an LLM as a heuristic generator for QCC-aware BDD variable ordering. Instead of predicting orderings directly, \texttt{QuantumEvo} searches over ordering heuristics initialized from multiple heuristic families. Candidate heuristics directly manipulate variable orderings using standard BDD operations and are selected by downstream QCC. The discovered heuristic, HGA-QE, modifies the sifting step inside a genetic algorithm so that the procedure is better aligned with QCC. Across the benchmark set, HGA-QE achieves a 70.9\% tie-or-win rate against the per-function best baseline and is strictly best on 13.5\% of the functions. The results demonstrate broadly competitive QCC performance, with HGA-QE showing a clearer relative advantage in strict wins on the two benchmark suites drawn from sources different from the data used for heuristic discovery.

[Read the original at arXiv →](https://arxiv.org/abs/2609.05327v1)
