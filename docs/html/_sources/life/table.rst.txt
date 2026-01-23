.. _table:

Table
=====
.. autoclass:: elizur.life.table.LifeTable
   :members: get_lxs, get_qxs, w

   .. method:: dx(x: int) -> float:

      Args:
          * **x** - start age

      Returns:
          The number of failures between ages x and x + 1

   .. method:: qx(x: int) -> float:

      Args:
          * **x** - start age

      Returns:
          The probability of failure between the ages x and x + 1

   .. method:: px(x: int) -> float:

      Args:
          * **x** - start age

      Returns:
          The probability of survival between the ages x and x + 1

   .. method:: lx(x: int) -> float:

      Args:
          * **x** - start age

      Returns:
          The population size at age x.  This is the same thing as the
          number of person years lived between age x and x + 1.

   .. method:: ex(x: int) -> float:

      Args:
          * **x** - start age


      Returns:
          The curtate life expectation at age x

   .. method:: mx(x: int) -> float:

      Args:
          * **x** - start age

      Returns:
          The central failure rate between ages x and x + 1

   .. method:: nqx(n: int, x: int) -> float:

      Args:
          * **n** - width of failure interval in years

          * **x** - start age

      Returns:
          The probability of failure between ages x and x + n

   .. method:: nqxs(n: int) -> np.array:

      Args:
          * **n** - width of failure interval in years

      Returns:
          The probability of failure between ages x and x + n for
          all ages

   .. method:: npx(n: int, x: int) -> float:

      Args:
          * **n** - width of failure interval in years
          * **x** - start age

      Returns:
          The probability of survival between ages x and x + n

   .. method:: npxs(n: int) -> np.array:

      Args:
          * **n** - width of failure interval in years

      Returns:
          The probability of survival between ages x and x + n for
          all ages

   .. method:: nlx(n: int, x: int) -> float:

       Args:
           * **n** - width of failure interval in years

           * **x** - start age

       Returns:
           The number of person years lived between ages x and x + n

   .. method:: ndx(n: int, x: int) -> float:

       Args:
           * **n** - width of failure interval in years

           * **x** - start age

       Returns:
            The number of failures between ages x and x + n

   .. method:: nmx(n: int, x: int) -> float:

       Args:
           * **n** - width of failure interval in years

           * **x** - start age

       Returns:
           The central failure rate between ages x and x + n

   .. method:: tqxn(t: int, n: int, x: int) -> float:

        Args:
            * **t** - width of the failure interval in years

            * **n** - width of the survival interval in years

            * **x** - start age

        Returns:
            The probability of surviving from age x to x + n and
            then failing between age x + n and age x + n + t

   .. method:: tqxns(t: int, n: int) -> np.array:

        Args:
            * **t** - width of the failure interval in years

            * **n** - width of the survival interval in years

        Returns:
            The probability of surviving from age x to x + n and
            then failing between age x + n and age x + n + t for
            all ages

   .. method:: Dx(x: int, i: float) -> float:

        Actuarial commutation function Dx

        Args:
            * **x** - start age

            * **i** - interest rate

        Returns:
            Population at age x discounted for x years

   .. method:: Nx(x: int, i: float) -> float:

        Actuarial commutation function Nx

        Args:
            * **x** - start age

            * **i** - interest rate

        Returns:
            Sum of Ds from age x and onward

   .. method:: Sx(x: int, i: float) -> float:

        Actuarial commutation function Sx

        Args:
            * **x** - start age

            * **i** - interest rate

        Returns:
            Sum of Ns from age x and onward

   .. method:: Cx(x: int, i: float) -> float:

        Actuarial commutation function Cx

        Args:
            * **x** - start age

            * **i** - interest rate

        Returns:
            Failures between x and x + 1 discounted for x years

   .. method:: Mx(x: int, i: float) -> float:

        Actuarial commutation function Mx

        Args:
            * **x** - start age

            * **i** - interest rate

        Returns:
            Sum of Cs from age x and onward

   .. method:: Rx(x: int, i: float) -> float:

        Actuarial commutation function Rx

        Args:
            * **x** - start age

            * **i** - interest rate

        Returns:
            Sum of Ms from age x and onward

   .. method:: Ax(x: int, i: float) -> float:

        Args:
            * **x** - start age

            * **i** - interest rate

        Returns:
            Actuarial present value of level whole insurance

   .. method:: Axn(x: int, i: float, n: int) -> float:

        Args:
            * **x** - start age

            * **i** - interest rate

            * **n** - number of periods in the temporary insurance

        Returns:
            Actuarial present value of level temporary insurance

   .. method:: IAx(x: int, i: float) -> float:

        Args:
            * **x** - start age

            * **i** - interest rate

        Returns:
            Actuarial present value of increasing whole insurance

   .. method:: IAxn(x: int, i: float, n: int) -> float:

        Args:
            * **x** - start age

            * **i** - interest rate

            * **n** - number of periods in the temporary insurance

        Returns:
            Actuarial present value of increasing temporary insurance

   .. method:: ax(x: int, i: float) -> float:

        Args:
            * **x** - start age

            * **i** - interest rate

        Returns:
            Actuarial present value of a level perpetuity

   .. method:: axn(x: int, i: float, n: int) -> float:

        Args:
            * **x** - start age

            * **i** - interest rate

            * **n** - length of payments

        Returns:
            Actuarial present value of a temporary annuity

   .. method:: ax_due(x: int, i: float) -> float:

        Args:
            * **x** - start age

            * **i** - interest rate

        Returns:
            Actuarial present value of a level perpetuity due

   .. method:: axn_due(x: int, i: float, n: int) -> float:

        Args:
            * **x** - start age

            * **i** - interest rate

            * **n** - length of payments

        Returns:
            Actuarial present value of a temporary annuity due
