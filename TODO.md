# TODO

## Annuity and EPV

[X] Annuity and epv numpy (backwards compat, works with NaNs, 1s, and 0s)
[X] Array sphinx docs for epv
[X] Decide on how input and output typing should work (tuples, numpy array, etc)
[X] Array README docs for epv
[X] Array README docs for annuities
[X] Array sphinx docs for annuities
[X] Allow matrix of epv calculations
[X] Numpy input docs and typing

## General

[X] Change use of imports via __init__
[ ] Document performance improvement in using numpy arrays or numba over plain python iteration

## LifeTable

[X] Decide on how input and output typing should work (tuples, numpy array, etc)
[X] Add plural of lx, qx, px, nx, dx, etc to life table interface
[X] Use numpy to produce matrix of npx, nqx, etc
[X] Out of bounds inputs should not error - e.g. qx[505] == 1
[ ] Remove deprecated methods in v1.0.0

## Other

[ ] Bring in numpy financial compatability
[ ] Endowments
[ ] Deferred Insurance
[ ] Value-at-Risk (Var)
[ ] Tail Value-at-Risk (TVar)
[ ] Sharpe Ratio
[ ] Option and derivate pricing
