# PHASE_ROADMAP

## Phase 0: Scope Freeze and Project Skeleton

### Objective

Finalize the project scope and prepare the base structure.

### Tasks

1. Confirm accepted time formats.
2. Confirm normalization rules.
3. Confirm rejected-input behavior.
4. Confirm GUI layout.
5. Confirm technology stack.
6. Create folder skeleton.
7. Create roadmap and system overview documents.

### Deliverables

- Project folder structure.
- `PHASE_ROADMAP.md`.
- `System_Overview.md`.

### Definition of Done

- Scope is finalized.
- Project skeleton exists.
- Roadmap is approved.

### Estimated Time

30 minutes to 1 hour.

---

## Phase 1: Formal Language Specification

### Objective

Define the exact language accepted by the system.

### Tasks

1. Define the alphabet.
2. Define valid 24-hour time rules.
3. Define valid 12-hour time rules.
4. Define minute rules.
5. Define AM/PM rules.
6. Write the language using formal notation.
7. Prepare accepted examples.
8. Prepare rejected examples.

### Deliverables

- `docs/FORMAL_SPECIFICATION.md`

### Definition of Done

- Language is unambiguous.
- Accepted examples are correct.
- Rejected examples are correct.
- Specification matches the approved scope.

### Estimated Time

30 minutes to 1 hour.

---

## Phase 2: Regular Expression Design

### Objective

Create the regular expression equivalent of the formal language.

### Tasks

1. Write the 24-hour subexpression.
2. Write the 12-hour subexpression.
3. Combine both using union.
4. Add anchors if needed.
5. Expand optional operators if required.
6. Test against accepted and rejected examples.

### Deliverables

- `docs/REGULAR_EXPRESSION.md`

### Definition of Done

- Regular expression accepts all valid inputs.
- Regular expression rejects all invalid inputs.
- Expression can be explained theoretically.

### Estimated Time

30 minutes to 1 hour.

---

## Phase 3: NFA Construction

### Objective

Construct the NFA that recognizes the time language.

### Tasks

1. Identify subpatterns: hour, colon, minute, space, meridiem.
2. Build NFA fragments.
3. Combine fragments using union and concatenation.
4. Define start state.
5. Define accepting states.
6. Prepare NFA transition table or description.
7. Prepare NFA diagram if time permits.

### Deliverables

- `docs/NFA_SPECIFICATION.md`
- Optional: `diagrams/nfa.dot`
- Optional: `data/nfa.json`

### Definition of Done

- NFA correctly represents the language.
- Start state is defined.
- Accepting states are defined.
- NFA can be explained during the demo.

### Estimated Time

1 to 2 hours.

---

## Phase 4: NFA-to-DFA Conversion

### Objective

Convert the NFA into an equivalent DFA.

### Tasks

1. Perform subset construction.
2. Name DFA states clearly.
3. Identify DFA start state.
4. Identify DFA accepting states.
5. Create full DFA transition table.
6. Add dead or trap state if needed.
7. Prepare DFA diagram if time permits.

### Deliverables

- `docs/DFA_SPECIFICATION.md`
- Optional: `diagrams/dfa.dot`
- Optional: `data/dfa.json`

### Definition of Done

- DFA accepts the same language as the NFA.
- Transition table is complete.
- Dead state behavior is documented.

### Estimated Time

1.5 to 2.5 hours.

---

## Phase 5: DFA Minimization

### Objective

Minimize the DFA and prove equivalence.

### Tasks

1. Separate accepting and non-accepting states.
2. Apply partition refinement.
3. Merge equivalent states.
4. Produce minimized DFA transition table.
5. Compare minimized DFA with original DFA.
6. Prepare minimized DFA diagram if time permits.

### Deliverables

- `docs/MINIMIZED_DFA_SPECIFICATION.md`
- Optional: `diagrams/minimized_dfa.dot`
- Optional: `data/minimized_dfa.json`

### Definition of Done

- Minimized DFA accepts the same language.
- No redundant states remain.
- Minimization process can be explained.

### Estimated Time

1 to 2 hours.

---

## Phase 6: Core Validation Engine

### Objective

Implement the validator using the minimized DFA.

### Tasks

1. Define alphabet in code.
2. Define states.
3. Define start state.
4. Define accepting states.
5. Define transition table.
6. Implement trace generation.
7. Implement accept/reject decision.
8. Implement basic rejection reasons.
9. Implement normalization logic.

### Deliverables

- `core/normalizer.py`
- `core/automaton.py`
- `core/trace.py`
- `core/diagnostics.py`

### Definition of Done

- Valid 24-hour inputs are accepted.
- Valid 12-hour inputs are accepted.
- Invalid inputs are rejected.
- Trace is generated.
- Basic rejection reasons are generated.

### Estimated Time

2 to 3 hours.

---

## Phase 7: GUI Development

### Objective

Build a clean and presentable user interface.

### Tasks

1. Create main app layout.
2. Add input field.
3. Add validate button.
4. Add result banner.
5. Add summary tab.
6. Add formal language tab.
7. Add automata tab.
8. Add trace tab.
9. Add test cases tab.
10. Add sample input buttons.

### Deliverables

- `app.py`
- `ui/layout.py`
- `ui/summary_tab.py`
- `ui/formal_language_tab.py`
- `ui/automata_tab.py`
- `ui/trace_tab.py`
- `ui/test_cases_tab.py`

### Definition of Done

- User can enter input.
- User can validate input.
- Result is displayed clearly.
- All required artifacts are displayed.
- GUI is ready for demonstration.

### Estimated Time

2 to 3 hours.

---

## Phase 8: Testing and Demonstration Preparation

### Objective

Ensure the system works reliably for presentation.

### Tasks

1. Create accepted test cases.
2. Create rejected test cases.
3. Test normalization cases.
4. Test edge cases.
5. Prepare sample inputs.
6. Prepare demo script.
7. Fix critical UI issues.
8. Verify all tabs display correctly.

### Deliverables

- `docs/TEST_PLAN.md`
- `docs/DEMO_SCRIPT.md`
- `core/samples.py`
- `tests/`

### Definition of Done

- Must-have test cases pass.
- Demo runs smoothly.
- Rejection explanations are understandable.
- No critical crash occurs during normal use.

### Estimated Time

1 to 2 hours.

---

## Phase 9: Documentation and Final Polish

### Objective

Prepare the final submission and presentation.

### Tasks

1. Complete formal specification documentation.
2. Include regular expression.
3. Include NFA.
4. Include DFA.
5. Include minimized DFA.
6. Include sample results.
7. Write conclusion.
8. Explain equivalence between representations.
9. Polish GUI labels and wording.

### Deliverables

- Completed documentation set.
- Final README.
- Final demo-ready application.

### Definition of Done

- Project looks complete.
- Theory is clearly connected to implementation.
- System can be demonstrated within a few minutes.

### Estimated Time

1 to 2 hours.