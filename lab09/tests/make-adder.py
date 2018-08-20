test = {
  'name': 'make-adder',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (add-two 2)
          eb5438773fa3774b23f3a524c49c4eb1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add-two 3)
          a1bce68344d05cff1822ab9ad453b1cc
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add-three 3)
          5dd2f13fb4c4fd724ede9fca5662f722
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add-three 9)
          deb40a3ab34361d616492b052a309881
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
      scm> (define add-two (make-adder 2))
      scm> (define add-three (make-adder 3))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
