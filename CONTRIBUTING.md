# Contributing to SemiconFab

Thank you for your interest in contributing to SemiconFab! This project is **source-available** under the [PolyForm Noncommercial License 1.0.0](LICENSE).

---

## 1. How to Submit Equipment Data

We actively encourage fab engineers, equipment specialists, and researchers to expand and verify our equipment catalog.

1. **Equipment Submission Runbook**:
   Please read our comprehensive submission guide: [SUBMISSION.md](SUBMISSION.md).
2. **Interactive Web Form**:
   You can submit new equipment records or fill in missing fields for draft records using the web form at [/add-equipment](https://semiconfab.org/add-equipment) (`add-equipment.html`).
3. **Data Provenance Tiers**:
   Every contributed data point must be accompanied by an explicit provenance tier:
   - `vendor_confirmed`: Published OEM documentation (datasheet, whitepaper).
   - `independent_verified`: Third-party physical cleanroom audit or certified dealer inspection.
   - `community_corroborated`: $\ge 2$ independent semiconductor engineers concordant within 5%.
   - `inferred`: Derived from platform family physics, node scaling, or engineering calculation.
   - `synthetic`: Computational estimate (requires explicit disclaimer).
4. **Local Validation**:
   Validate your generated JSON records against `schema.json` using the bundled Python CLI:
   ```bash
   pip install ./tools/validator
   schemavalidator validate path/to/your/record.json
   ```

---

## 2. Code Style & Tooling

To ensure consistency across the codebase, we enforce automated formatting:

- **Prettier**:
  - Indentation: 2 spaces (no tabs)
  - Quotes: Double quotes
  - Semicolons: Always
  - Trailing Commas: All
  - Run formatter:
    ```bash
    npm run format
    ```
  - Check formatting:
    ```bash
    npm run format:check
    ```
- **ESLint**:
  - Run linter:
    ```bash
    npm run lint
    ```

---

## 3. Pull Request Guidelines

1. **No Behavior Change Without an Issue**:
   All PRs that alter existing behavior, UI logic, or simulation models must be linked to an existing GitHub Issue discussing the rationale and pedagogical impact.
2. **Untouchable Assets**:
   Published numbers (7 L1 / 114 draft records, 18 tool groups / 217 machines) and canonical trace files (`catalog.json`, `events-t1-fifo.jsonl`) are protected contracts. Pull requests altering these core files without prior working-group sign-off will be rejected.
3. **Bilingual Requirement**:
   All user-facing strings must support both English and Simplified Chinese.
4. **Documentation**:
   If an architectural trade-off or non-obvious design choice is made, record the decision and justification in `ASSUMPTIONS.md`.

---

## 4. Licensing of Contributions

By submitting a pull request or equipment dataset, you agree that your contribution will be licensed under the project's [PolyForm Noncommercial License 1.0.0](LICENSE). Commercial use requires a separate license — contact info@semiconfab.org.
