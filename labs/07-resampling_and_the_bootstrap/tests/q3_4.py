test = {
  'hidden': False,
  'name': '3.4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from numpy import std
          >>> stdv = new_bootstrap_estimates.std()
          >>> 0 < stdv < 10
          True
          >>> 0 < new_right_end - new_left_end < 45
          True
          >>> abs(((new_right_end - new_left_end) / stdv) - 3.9) < 0.2
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
