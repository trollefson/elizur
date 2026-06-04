Welcome to Elizur's documentation!
==================================

.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
    :target: https://www.gnu.org/licenses/gpl-3.0

.. image:: https://github.com/trollefson/elizur/actions/workflows/lint-and-test.yml/badge.svg
    :target: https://github.com/trollefson/elizur/actions/workflows/lint-and-test.yml

.. image:: https://codecov.io/gh/trollefson/elizur/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/trollefson/elizur

Elizur is a finance library for actuaries, finance professionals, and students.
The package helps with calculating annuity present values, annuity future values,
cash flow expected present values, life contingencies, and multi-decrement tables.
Elizur depends on `NumPy <https://numpy.org>`_ and `Polars <https://pola.rs>`_ at runtime.
The project is named after `Elizur Wright <https://en.wikipedia.org/wiki/Elizur_Wright>`_.

If you like Elizur, support the project by starring it on `GitHub <https://github.com/trollefson/elizur>`_.

Requirements
============

`Python 3.12+ <https://www.python.org/downloads/>`_

Installation
============

.. code-block:: bash

    pip install elizur

Reference
=========

Follow the links below to view code base documentation

.. toctree::
   :maxdepth: 3

   life/index

Examples
========

All calculations accept a single numeric type or iterable (including numpy arrays) as input.

Given an interest rate calculate a discount factor

.. code-block:: python

    >>> import elizur.life.annuity as ann
    >>> ann.discount_factor(0.07)
    0.9345794
    >>> ann.discount_factor([0.07, 0.06])
    array([0.93457944, 0.94339623])

Given a term and interest rate calculate the present value of an annuity

.. code-block:: python

    >>> import elizur.life.annuity as ann
    >>> ann.annuity_pv(n=10, i=0.07)
    7.023581540932602
    >>> ann.annuity_pv(n=[10, 20], i=[0.07, 0.08])
    array([7.02358154, 9.81814741])

Given a term and interest rate calculate the present value of an annuity increasing by one each period

.. code-block:: python

    >>> import elizur.life.annuity as ann
    >>> ann.increasing_annuity_pv(n=10, i=0.07)
    34.73913324929581
    >>> ann.increasing_annuity_pv(n=[10, 20], i=[0.07, 0.08])
    array([34.73913325, 78.90793815])

Given a set of cash flows, probabilities, and interest rates calculate the expected present value

.. code-block:: python

    >>> from elizur.life import expected_present_value
    >>> expected_present_value(
    ...     cash_flows=(10, 11, 12),
    ...     probabilities=(0.99, 0.98, 0.97),
    ...     interest_rates=(0.05, 0.06, 0.07)
    ... )
    28.88814436019514

Given a mortality table calculate life contingencies and probabilities

.. code-block:: python

    >>> from elizur.life.table import LifeTable, EXAMPLE_TABLE
    >>> life_table = LifeTable(EXAMPLE_TABLE)
    >>> life_table.qx(0)
    0.006271
    >>> life_table.qx(77)
    0.036094
    >>> life_table.tqxn(3, 2, 77)
    0.08770141840040623
    >>> life_table.Ax(0, 0.07)
    0.01562517028789102
    >>> life_table.ax(0, 0.07)
    14.046872397027947

Export a life table as a Polars DataFrame for use in projection models

.. code-block:: python

    >>> from elizur.life.table import LifeTable, EXAMPLE_TABLE
    >>> life_table = LifeTable(EXAMPLE_TABLE)
    >>> frame = life_table.to_frame()
    >>> frame.head(3)
    shape: (3, 6)
    ┌─────┬──────────┬──────────┬────────────┬──────────┬──────────┐
    │ age ┆ qx       ┆ px       ┆ lx         ┆ dx       ┆ mx       │
    ╞═════╪══════════╪══════════╪════════════╪══════════╪══════════╡
    │ 0   ┆ 0.006271 ┆ 0.993729 ┆ 100000.0   ┆ 627.1    ┆ 0.006271 │
    │ 1   ┆ 0.000418 ┆ 0.999582 ┆ 99372.9    ┆ 41.538…  ┆ 0.000418 │
    │ 2   ┆ 0.000281 ┆ 0.999719 ┆ 99331.36…  ┆ 27.912…  ┆ 0.000281 │
    └─────┴──────────┴──────────┴────────────┴──────────┴──────────┘

Combine mortality and lapse decrements using a multi-decrement table

.. code-block:: python

    >>> from elizur.life.table import LifeTable, MultiDecrementTable, EXAMPLE_TABLE
    >>> import numpy as np
    >>> mortality = LifeTable(EXAMPLE_TABLE)
    >>> lapse_rates = np.full(mortality.table_size, 0.05)
    >>> lapse_rates[-1] = 0.0
    >>> mdt = MultiDecrementTable(mortality, lapse_rates)
    >>> mdt.qx_d(0)    # probability of death in multi-decrement context
    0.005944...
    >>> mdt.qx_w(0)    # probability of lapse in multi-decrement context
    0.047843...
    >>> mdt.qx_tau(0)  # total decrement probability
    0.053387...
    >>> frame = mdt.to_frame()
    >>> frame.columns
    ['age', 'qx_prime_d', 'qx_prime_w', 'qx_d', 'qx_w', 'qx_tau', 'px_tau', 'lx_tau', 'dx_d', 'dx_w']

Import a mortality table in SOA CSV format and perform life contingency calculations.
Download a mortality table in csv format from the SOA `here <https://mort.soa.org>`_.

.. code-block:: python

    >>> from elizur.life.util import read_soa_csv_mort_table
    >>> from elizur.life.table import LifeTable
    >>> mort_table = read_soa_csv_mort_table("1941_cso_basic_table_anb.csv")
    >>> life_table = LifeTable(mort_table["values"])
    >>> life_table.qx(77)
    0.10364
    >>> life_table.Ax(0, 0.07)
    0.03800673925889163

There are many other possibilities.  Check out the `Reference`_ links for a full list of functionality.

Contributing
============

Checkout the contributing guide `here <https://github.com/trollefson/elizur/blob/master/CONTRIBUTING.md>`_ if you'd like to contribute code or raise issues `here <https://github.com/trollefson/elizur/issues>`_.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
