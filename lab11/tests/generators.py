test = {
  'name': 'Generators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def gen():
          ...     print("Starting here")
          ...     i = 0
          ...     while i < 6:
          ...         print("Before yield")
          ...         yield i
          ...         print("After yield")
          ...         i += 1
          >>> next(gen)
          814d8b9841f5d87d6a6b076eff0d8ed2
          # locked
          >>> gen
          fa5011e6b7756d345379ee4b678fcf4d
          # locked
          >>> g = gen()
          >>> g
          124b79d798451e20e07764862cd793a3
          # locked
          >>> g == iter(g)
          308968ce50a38a2957823e1439417bf2
          # locked
          >>> next(g)
          13a515abbb3b8d304d0a5a4b3021b098
          2e7d8dbafba7985fd02fc693bc61218b
          4b569bf0e21d6369c5343767f1146f64
          # locked
          >>> next(g)
          265038a6c2ed6f967cfa87d2dcd13485
          2e7d8dbafba7985fd02fc693bc61218b
          94ce22b5936436a75abf185df37ba826
          # locked
          >>> next(g)
          265038a6c2ed6f967cfa87d2dcd13485
          2e7d8dbafba7985fd02fc693bc61218b
          805a87056a1a3fd559e4ef12a815b2be
          # locked
          >>> g2 = gen()
          >>> next(g2)
          13a515abbb3b8d304d0a5a4b3021b098
          2e7d8dbafba7985fd02fc693bc61218b
          4b569bf0e21d6369c5343767f1146f64
          # locked
          >>> iter(g2)
          124b79d798451e20e07764862cd793a3
          # locked
          >>> next(iter(g))
          265038a6c2ed6f967cfa87d2dcd13485
          2e7d8dbafba7985fd02fc693bc61218b
          350815b30c2ebeb01da1870d87346e85
          # locked
          >>> next(gen())
          13a515abbb3b8d304d0a5a4b3021b098
          2e7d8dbafba7985fd02fc693bc61218b
          4b569bf0e21d6369c5343767f1146f64
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
