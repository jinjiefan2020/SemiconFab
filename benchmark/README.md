<!-- MIMAC-2026 300mm wafer fab benchmark specification files and route definitions. -->

# Benchmark Data and Specifications

This directory contains the machine-readable route configurations (`routes.json`) and discrete-event simulation engine for the MIMAC-2026 simulation benchmark. The canonical technical specification is located at [/MIMAC-2026-SPEC-v1.0.md](/MIMAC-2026-SPEC-v1.0.md).

## Routes data v1.1 (2026-10-16)

Fixed the degenerate tails of products A/B/C: the last ~10 steps were pure
LITHO/TRACK alternation (step-count padding). Replaced with a proper ending
module: passivation CVD → pad-open litho/etch → strip → final cleans →
final inspection. Step counts unchanged (120/104/92). No published benchmark
results are affected (only sanity results had been published).
