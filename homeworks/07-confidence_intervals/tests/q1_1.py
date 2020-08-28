test = {
  'name': 'Question 1_1',
  'points': 1,
  'hidden': False,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0.0 <= votes_lower_bound <= votes_upper_bound <= 1.0
          True
          >>> isinstance(votes_lower_bound, float)
          True
          >>> isinstance(votes_upper_bound, float)
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
