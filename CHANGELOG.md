# Changelog

All notable changes to this project will be documented in this file.

## [0.3.1] — 2026-06-04

### Fixed
- Removed committed docs output that caused GitHub Pages 404; docs now built
  and deployed exclusively via GitHub Actions on tag push

---

## [0.3.0] — 2026-06-04

### Added
- `LifeTable.to_frame()` — exports the life table as a Polars DataFrame with
  columns `age`, `qx`, `px`, `lx`, `dx`, `mx` for joining against policy-level
  DataFrames in actuarial projection engines
- `MultiDecrementTable` — two-decrement table combining mortality and lapse
  using the UDD approximation; exposes `qx_d`, `qx_w`, `qx_tau`, `px_tau`,
  `lx_tau`, `dx_d`, `dx_w`, `npx_tau`, and `to_frame()`
- Codecov integration for coverage reporting

### Changed
- Migrated build backend from `hatchling` to `uv_build`
- Migrated dependency management from `hatch` to `uv`
- Migrated project to `src/` layout; tests moved from `test/` to `tests/`
- Expanded ruff lint rules to include `I` (isort), `UP` (pyupgrade),
  `B` (bugbear), and `ANN` (annotations)
- Replaced `Union[X, Y]` and `Tuple` annotations with modern `X | Y` and
  built-in generics throughout
- Replaced Black badge with Ruff badge in README
- Replaced Travis CI badge with GitHub Actions badge

### Removed
- `makefun` runtime dependency — replaced with `functools.wraps` and
  `__wrapped__` traversal for stacked decorator support
- `mock` dev dependency — `unittest.mock` from the standard library is sufficient
- `pylint` disable comments

---

## [0.2.2] — 2025-06-03

### Changed
- Refactored GitHub Actions publish workflow
- Fixed missing checkout version in GitHub workflows

---

## [0.2.1] — 2025-06-03

### Added
- GitHub Actions CI/CD pipeline for lint, test, and PyPI publish
- Project `Makefile` for common development tasks
- `pre-commit` configuration with ruff

### Changed
- Migrated from `setup.py` to `pyproject.toml`
- Switched dependency management to `uv`
- Reorganised docs directory for GitHub Pages

### Removed
- Travis CI configuration
- `pylint`

---

## [0.2.0] — 2020-05-04

### Added
- NumPy-backed `LifeTable` for significantly faster actuarial calculations
- Vectorised `expected_present_value` supporting variable cashflows,
  probabilities, and interest rates including 2D array batch evaluation
- Bounds handling for ages and intervals beyond the table size

### Changed
- `LifeTable` internals rewritten to use NumPy arrays (`qxs`, `pxs`, `lxs`,
  `dxs`, `mxs` are now `numpy.ndarray`)
- Applied Black code formatting throughout
- Moved input validators to a dedicated `elizur.life.util.validators` module
- Reorganised package structure to reduce `__init__.py` complexity

---

## [0.1.2] — 2019-06-27

### Fixed
- Corrected `tqxn` docstring

---

## [0.1.1] — 2019-06-27

### Fixed
- Added missing `long_description_content_type` to package metadata for
  correct PyPI rendering

---

## [0.1.0] — 2019-06-27

### Added
- `LifeTable` with full single-decrement actuarial functions: `qx`, `px`,
  `lx`, `dx`, `ex`, `mx`, `nqx`, `npx`, `nlx`, `ndx`, `nmx`, `tqxn`
- Commutation functions: `Dx`, `Nx`, `Sx`, `Cx`, `Mx`, `Rx`
- Actuarial present value functions: `Ax`, `Axn`, `IAx`, `IAxn`,
  `ax`, `axn`, `ax_due`, `axn_due`
- Annuity functions: `annuity_pv`, `annuity_due_pv`, `annuity_fv`,
  `annuity_due_fv`, `perpetuity_pv`, `perpetuity_due_pv`,
  `increasing_annuity_pv`, `decreasing_annuity_pv`, `geo_increasing_annuity_pv`
- SOA CSV mortality table reader (`read_soa_csv_mort_table`)
- `discount_factor`, `discount_rate`, `interest_rate` utility functions
