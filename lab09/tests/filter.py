test = {
  'name': 'filter',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (filter even? '(1 2 3 4))
          939eeec851ef4d7834e269dc3ed91c85
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter odd? '(1 3 5))
          b03c3817dfbc3539417062ee1fe90490
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter odd? '(2 4 6 1))
          de14f22fe5379b349d7d23f00aa8b3d3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter even? '(3))
          f9ebafa0bfa75e2a858c464aa39a573d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter odd? nil)
          f9ebafa0bfa75e2a858c464aa39a573d
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab09)
      scm> (load 'lab09_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
