test = {
  'name': 'What Would Scheme Print?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cons 1 2)
          2d28ec62cafd4f8193ed195771360ba3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cons 1 (cons 2 nil))
          437da7fcde2856663fa0002aab0f0b14
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (car (cons 1 (cons 2 nil)))
          d912fc844d1dbaeea8a84b3ec8b315bc
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cdr (cons 1 (cons 2 nil)))
          4c4505b119f53fac68e1f7117354f1e1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (list 1 2 3)
          7585771ecc8eac10b0735a645ecb8a79
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (list 1 (cons 2 3))
          e01f96b8c839e7c2096a639b6d420723
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(1 2 3)
          7585771ecc8eac10b0735a645ecb8a79
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(2 . 3)
          54a1bf77dcb4d871279707fddceb2d17
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(2 . (3))  ; Recall dot rule for pairs
          812fc8d3741aa2f642b208f2d531234d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (equal? '(1 . (2 . 3)) (cons 1 (cons 2 (cons 3 nil))))  ; Recall how boolean values are displayed
          da1373026f7a0774721ca3a8c5dd15c5
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (equal? '(1 . (2 . 3)) (cons 1 (cons 2 3)))
          f2f78bdee92fb379bc57e3ef1a6c0dc2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (equal? '(1 . (2 . 3)) (list 1 (cons 2 3)))
          da1373026f7a0774721ca3a8c5dd15c5
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cons 1 '(list 2 3))  ; Recall quoting
          826da030368e185a23a1a70897995e88
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (cons (list 2 (cons 3 4)) nil)
          e34cac8f1ba66ae521ab3ae5dcfaf28b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (car (cdr '(127 . ((131 . (137))))))
          3c07b200dbf1fe01a6b0c5977d8b6e05
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (equal? '(1 . ((2 . 3))) (cons 1 (cons (cons 2 3) nil)))
          f2f78bdee92fb379bc57e3ef1a6c0dc2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(cons 4 (cons (cons 6 8) ()))
          6117e327e7d53413652889593b49dd33
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
