Welcome to Elizur's documentation!
==================================

.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
    :target: http://perso.crans.org/besson/LICENSE.html

.. image:: https://travis-ci.org/trollefson/elizur.svg?branch=master
    :target: https://travis-ci.org/trollefson/elizur

.. image:: https://coveralls.io/repos/github/trollefson/elizur/badge.svg?branch=master
    :target: https://coveralls.io/github/trollefson/elizur?branch=master

Elizur is an open source finance package for actuaries, finance professionals, and students.  The package currently helps with calculating annuity present values, annuity future values, cash flow expected present values, and life contingencies.  Elizur depends only on the Python 3 standard library and `NumPy <https://numpy.org>`_ at runtime.  The project is named after `Elizur Wright <https://en.wikipedia.org/wiki/Elizur_Wright>`_.

If you like Elizur, support the project by starring it on `GitHub <https://github.com/trollefson/elizur>`_.

Requirements
============

`Python 3.5+ <https://www.python.org/downloads/>`_

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

All calculations accept a single numeric type or iterable (including numpy arrays) as input

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
    >>>    cash_flows=(10, 11, 12),
    >>>    probabilities=(0.99, 0.98, 0.97),
    >>>    interest_rates=(0.05, 0.06, 0.07)
    >>> )
    28.88814436019514
    >>> expected_present_value(
    ...     cash_flows=(
    ...         (10, 11, 12),
    ...         (13, 14, 15)
    ...     ),
    ...     probabilities=(
    ...         (0.99, 0.98, 0.97),
    ...         (0.96, 0.95, 0.94)
    ...     ),
    ...     interest_rates=(
    ...         (0.05, 0.06, 0.07),
    ...         (0.08, 0.09, 0.10)
    ...     )
    ... )
    array([28.88814436, 33.74225435])

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
    >>> life_table.IAxn(0, 0.07, 30)
    0.04871771529491165
    >>> life_table.ax(0, 0.07)
    14.046872397027947
    >>> life_table.axn_due(0, 0.07, 30)
    13.173054007415931

Import a mortality table in a specific SOA CSV format and perform life contingency calculations.  Download a mortality table in csv format from the SOA `here <https://mort.soa.org>`_.  This example uses the first table, 1941 CSO Basic Table ANB.

.. code-block:: python

    >>> from elizur.life.util import read_soa_csv_mort_table  
    >>> from elizur.life.table import LifeTable
    >>> mort_table = read_soa_csv_table("1941_cso_basic_table_anb.csv")
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
====================

* :ref:`genindex`
* :ref:`modindex`
