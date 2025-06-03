![elizur.](https://elizur.s3.amazonaws.com/elizur_github_banner.png "elizur.")

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/trollefson/elizur.svg?branch=master)](https://travis-ci.org/trollefson/elizur)
[![PyPI version](https://badge.fury.io/py/elizur.svg)](https://badge.fury.io/py/elizur)
[![Coverage Status](https://coveralls.io/repos/github/trollefson/elizur/badge.svg?branch=master)](https://coveralls.io/github/trollefson/elizur?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Elizur is an open source finance package for actuaries, finance professionals, and students.  The package currently helps with calculating annuity present values, annuity future values, cash flow expected present values, and life contingencies.  Elizur depends only on the Python 3 standard library and [NumPy](https://numpy.org>) at runtime.  The project is named after [Elizur Wright](https://en.wikipedia.org/wiki/Elizur_Wright).

If you like Elizur, support the project by clicking the :star: above!

## Requirements

* [Python 3.5+](https://www.python.org/downloads/)

## Install

`pip install elizur`

## Documentation

Read the library documentation [here](https://trollefson.github.io/elizur)

## Examples

All calculations accept a single numeric type or iterable (including numpy arrays) as input

Given an interest rate calculate a discount factor

```python
>>> import elizur.life.annuity as ann
>>> ann.discount_factor(0.07)
0.9345794
>>> ann.discount_factor([0.07, 0.06])
array([0.93457944, 0.94339623])
```

Given a term and interest rate calculate the present value of an annuity

```python
>>> import elizur.life.annuity as ann
>>> ann.annuity_pv(n=10, i=0.07)
7.023581540932602
>>> ann.annuity_pv(n=[10, 20], i=[0.07, 0.08])
array([7.02358154, 9.81814741])
```
Given a term and interest rate calculate the present value of an annuity increasing by one each period

```python
>>> import elizur.life.annuity as ann
>>> ann.increasing_annuity_pv(n=10, i=0.07)
34.73913324929581
>>> ann.increasing_annuity_pv(n=[10, 20], i=[0.07, 0.08])
array([34.73913325, 78.90793815])
```

Given cash flows, probabilities, and interest rates calculate the expected present value

```python
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
```

Given a mortality table calculate life contingencies and probabilities

```python
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
```

Import a mortality table in a specific SOA CSV format and perform life contingency calculations.  Download a mortality table in csv format from the SOA [here](https://mort.soa.org).  This example uses the first table, 1941 CSO Basic Table ANB.

```python
>>> from elizur.life.util import read_soa_csv_mort_table
>>> from elizur.life.table import LifeTable
>>> mort_table = read_soa_csv_table("1941_cso_basic_table_anb.csv")
>>> life_table = LifeTable(mort_table["values"])
>>> life_table.qx(77)
0.10364
>>> life_table.Ax(0, 0.07)
0.03800673925889163
```

There are many other possibilities.  Check out the reference section of the [docs](https://trollefson.github.io/elizur) for a full list of functionality.

## Contributing

Checkout the contributing guide [here](https://github.com/trollefson/elizur/blob/master/CONTRIBUTING.md) if you'd like to contribute code or raise issues [here](https://github.com/trollefson/elizur/issues).
