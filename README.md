![elizur.](https://elizur.s3.amazonaws.com/elizur_github_banner.png "elizur.")

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/trollefson/elizur.svg?branch=master)](https://travis-ci.org/trollefson/elizur)
[![PyPI version](https://badge.fury.io/py/elizur.svg)](https://badge.fury.io/py/elizur)
[![Coverage Status](https://coveralls.io/repos/github/trollefson/elizur/badge.svg?branch=master)](https://coveralls.io/github/trollefson/elizur?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Elizur is an open source finance library for actuaries, finance professionals, and students.  The library currently helps with calculating present values, future values, expected present values, life contingencies, and other common procedures performed by professionals and students.  The library is intended to help with exam formula and other general finance calculations.  It is not a place for real world modeling solutions like IFRS17 or Solvency II.  The library will remain a library.  If you'd like to create a web ui or desktop application with Elizur please start a seperate project and include Elizur as a dependency.  The library is free of charge, open source, well tested, documented, and depends only on the Python 3 standard library at runtime.  The Elizur project is named after [Elizur Wright](https://en.wikipedia.org/wiki/Elizur_Wright).

If you like Elizur, support the project by clicking the :star: above!

## Requirements

* [Python 3.5+](https://www.python.org/downloads/)

## Install

`pip install elizur`

## Documentation

Read the library documentation [here](https://trollefson.github.io/elizur)

## Examples

Given an interest rate calculate a discount factor

```python
>>> import elizur.life.annuity as ann
>>> ann.discount_factor(0.07)
0.9345794
```

Given a term and interest rate calculate the present value of an annuity

```python
>>> import elizur.life.annuity as ann
>>> ann.annuity_pv(n=10, i=0.07)
7.023581540932602
``` 
Given a term and interest rate calculate the present value of an annuity increasing by one each period

```python
>>> import elizur.life.annuity as ann
>>> ann.increasing_annuity_pv(n=10, i=0.07)
34.73913324929581
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

Given a set of cash flows, probabilities, and interest rates calculate the expected present value

```python
>>> from elizur.life import expected_present_value
>>> expected_present_value(
>>>    cash_flows=(10, 11, 12),
>>>    probabilities=(0.99, 0.98, 0.97),
>>>    interest_rates=(0.05, 0.06, 0.07)
>>> )
28.88814436019514
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

## What's Next?

* Endowments
* Deferred Insurance
* Value-at-Risk (Var)
* Tail Value-at-Risk (TVar)
* Sharpe Ratio
* Option and derivate pricing

## Contributing

Checkout the contributing guide [here](https://github.com/trollefson/elizur/blob/master/CONTRIBUTING.md) if you'd like to contribute code or raise issues [here](https://github.com/trollefson/elizur/issues).
