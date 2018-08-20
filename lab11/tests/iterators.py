test = {
  'name': 'Iterators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [1, 2, 3, 4]
          >>> t = iter(s)
          >>> next(s)
          814d8b9841f5d87d6a6b076eff0d8ed2
          # locked
          >>> next(t)
          94ce22b5936436a75abf185df37ba826
          # locked
          >>> next(t)
          805a87056a1a3fd559e4ef12a815b2be
          # locked
          >>> iter(s)
          00adbbe9b528bd0f3f88f75b5e77eeac
          # locked
          >>> next(iter(s))
          94ce22b5936436a75abf185df37ba826
          # locked
          >>> next(iter(t))
          350815b30c2ebeb01da1870d87346e85
          # locked
          >>> next(iter(s))
          94ce22b5936436a75abf185df37ba826
          # locked
          >>> next(iter(t))
          3cfd97a152be55d1a3486dbacb2bf637
          # locked
          >>> next(t)
          34e2a9758449af6c4efffc3cf0d3be23
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> r = range(6)
          >>> r_iter = iter(r)
          >>> next(r_iter)
          4b569bf0e21d6369c5343767f1146f64
          # locked
          >>> [x + 1 for x in r]
          344626f9a33ed1f91219086290549aa1
          # locked
          >>> [x + 1 for x in r_iter]
          0bc1bda54eaf01da1457ca891d5af0e6
          # locked
          >>> next(r_iter)
          34e2a9758449af6c4efffc3cf0d3be23
          # locked
          >>> list(range(-2, 4))   # Converts an iterable into a list
          28afc906bb5939bd1a90addd6aff52d5
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> map_iter = map(lambda x : x + 10, range(5))
          >>> next(map_iter)
          994cc386b9ac20ceafc06b188d1ee65b
          # locked
          >>> next(map_iter)
          7770d7151426f0a15dc7d17154603e7b
          # locked
          >>> list(map_iter)
          99072fdda9e7f8fc19953fa187c2b4c6
          # locked
          >>> for e in filter(lambda x : x % 2 == 0, range(1000, 1008)):
          ...     print(e)
          b775af381bae223aa72f840051101376
          4bfe5eebe23ff12e8396f20522740e86
          91acc5f91a49848ef552a6016593315b
          dea759207fb0e230e48fb315c33684f6
          # locked
          >>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
          ba55932ba1dd09bd68611ffa0946efdc
          # locked
          >>> for e in zip([10, 9, 8], range(3)):
          ...   print(tuple(map(lambda x: x + 2, e)))
          1bd71c0bb2c19feac261ecfc6eddb18f
          384d4c15c567e7f6ae46ab08fd5820b9
          daa7643fe4536bd7e1926dc27c715bd4
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
