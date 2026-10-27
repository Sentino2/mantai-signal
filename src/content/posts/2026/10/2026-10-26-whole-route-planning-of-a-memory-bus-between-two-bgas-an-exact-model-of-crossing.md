---
title: "Whole-Route Planning of a Memory Bus Between Two BGAs: An Exact Model of Crossings and Layer Changes, Negotiated to DRC-Clean Copper"
date: 2026-10-26T15:24:28+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.35601v1"
ext_id: "arxiv:2610.35601v1"
tags: ["hardware", "models"]
summary: "Routing the bus between a processor and its DRAM remains largely manual in printed circuit board (PCB) design, and published algorithms optimize proxies such as crossing or layer counts. We present a router that plans every lane of a two-layer BGA-to-BGA bus before any copper is laid, and carries the plan to design-rule-clean copper. Its core is an exact constraint-programming model that chooses, "
---

Routing the bus between a processor and its DRAM remains largely manual in printed circuit board (PCB) design, and published algorithms optimize proxies such as crossing or layer counts. We present a router that plans every lane of a two-layer BGA-to-BGA bus before any copper is laid, and carries the plan to design-rule-clean copper. Its core is an exact constraint-programming model that chooses, for all lanes at once, where each necessary crossing occurs, in what order -- by a rule over every triple of lanes -- and where each lane changes layer, with via room; for the ends it is given, it proves its plan optimal within the model. The model reads naturally as physics: worldlines, frustrated Ising spins and contact forces. A linear program places the lanes in millimeters; the constraints it must violate return to the model as cuts, and audit findings as negotiated congestion prices, until the plan passes an audit against the production router's rules or lays clean. The escapes are chosen by an estimate of the same objective, and differential pairs carry their polarity, with an automatic via crossover where the ends disagree. On an Allwinner H3 and a Zynq-7020, each to a DDR3 device, the router completes every rung of two ladders, of up to 51 nets on the H3 (its whole bus) and 43 on the Zynq, connected and DRC-clean, never with more vias than the human designer (80 against 88 and 62 against 100 at the top rungs) and always with less copper, where the toolkit's production router leaves nets open on four of the ten rungs and Freerouting completes none. On the Zynq board itself it completes 45 of the bus's nets with 70 vias to the designer's 105. On generated buses of three, four and six routing layers every run completes, and every one with a known optimum attains it.

[Read the original at arXiv →](https://arxiv.org/abs/2610.35601v1)
