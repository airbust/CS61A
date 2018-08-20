test = {
  'name': 'Lambda the Free',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'A lambda expression does not bind the function object that it returns to any name.',
          'choices': [
            'A lambda expression does not bind the function object that it returns to any name.',
            'A lambda expression can have any number of parameters.',
            'A lambda expression cannot return another function.',
            'A def statement can only have one line in its body.'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          Which of the following statements describes a difference between a def statement
          and a lambda expression?
          """
        },
        {
          'answer': '2',
          'choices': [
            '1',
            '2',
            '3',
            'Not enough information'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          How many parameters does the following lambda expression have?
          lambda a, b: c + d
          """
        },
        {
          'answer': 'When the function returned by the lambda expression is called.',
          'choices': [
            'When the function returned by the lambda expression is called.',
            'When you assign the lambda expression to a name.',
            'When the lambda expression is evaluated.',
            'When you pass the lambda expression into another function.'
          ],
          'hidden': False,
          'locked': False,
          'question': 'When is the return expression of a lambda expression executed?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> lambda x: x  # A lambda expression with one parameter x
          Function
          >>> a = lambda x: x  # Assigning a lambda function to the name a
          >>> a(5)
          5
          >>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
          0f10194daf41a11a30f4adc80d959f28
          # locked
          >>> b = lambda x: lambda: x  # Lambdas can return other lambdas!
          >>> c = b(88)
          >>> c
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> c()
          0c194cbdd08370dca576a4d249abbe36
          # locked
          >>> d = lambda f: f(4)  # They can have functions as arguments as well
          >>> def square(x):
          ...     return x * x
          >>> d(square)
          9024755e0e6b1907cc6e80a977eb6fa3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> # Pay attention to the scope of variables
          >>> z = 3
          >>> e = lambda x: lambda y: lambda: x + y + z
          >>> e(0)(1)()
          ef6b0e7c554b5515158e88d1ee908645
          # locked
          >>> f = lambda z: x + z
          >>> f(3)
          ab06d135c02ab203238caafbf77976ce
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Try drawing an environment diagram if you get stuck!
          >>> higher_order_lambda = lambda f: lambda x: f(x)
          >>> g = lambda x: x * x
          >>> higher_order_lambda(2)(g) # Which argument belongs to which function call?
          ab06d135c02ab203238caafbf77976ce
          # locked
          >>> higher_order_lambda(g)(2)
          ef6b0e7c554b5515158e88d1ee908645
          # locked
          >>> t = lambda f: lambda x: f(f(f(x)))
          >>> t(lambda y: y + 1)(0)
          0f10194daf41a11a30f4adc80d959f28
          # locked
          >>> print_lambda = lambda z: print(z)
          >>> print_lambda
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> one_thousand = print_lambda(1000)
          406c98af0b3aa9a2c9dbd76d898bcda3
          # locked
          >>> one_thousand
          358b0ae001277273d8cd480ce5dbfb82
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
