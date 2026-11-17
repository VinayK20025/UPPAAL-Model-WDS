# Assumption-Aware CPS/WDS Metamodel (Working Specification)

## Scope

This working specification separates components, relationships, assumptions, behaviours, temporal constraints, provenance and verification obligations. It is a conceptual repository artefact; it is not a claim that an automated model transformation implementation is already available.

The current repository contains UPPAAL XML models under `models/`. The metamodel described here is a proposed modelling abstraction and must not be confused with a machine-readable schema or an automatically applied transformation, neither of which is currently supplied at the top level.

## Core model

Let `MM = (C, R, A, B, Θ, P, V)` where `C` is the component set, `R` the relationship set, `A` the assumptions, `B` the behaviour descriptions, `Θ` the temporal constraints, `P` the provenance records and `V` the verification obligations.

A component assumption is scoped to a component. A relationship assumption is scoped to a directed interaction/interface between two components. Examples include a sensor that operates correctly but a channel that delays, drops or alters its measurements; a PLC that produces a command but a delivery relation that loses the command.

## Assumption record

Each assumption should identify a stable ID, scope, predicate, provenance, rationale, status and violation-observation mechanism. Distinguish a documented assumption from its formalisation and from verification of whether the assumption holds.

## Provenance

Record whether a parameter is source-specified, experimentally selected or assumed. Parameter provenance is not a substitute for logical assumption semantics.

## Well-formedness checks

- Every relationship endpoint refers to a declared component.
- Every relationship-scoped assumption identifies its source, target and interface.
- Every temporal bound has a declared unit and clock interpretation.
- Every verification obligation references declared model elements.
- External/unresolved assumptions are not silently treated as proven.

These are proposed constraints; they are not currently enforced by an executable top-level metamodel validator.
