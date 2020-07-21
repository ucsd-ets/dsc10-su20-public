
test = {
  'name': 'q3_6',
  'hidden': False,
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a float
	>>> import numbers
	>>> isinstance(robust_level_1929, numbers.Real)
	True
	>>> # should be a float
	>>> import numbers
	>>> isinstance(robust_level_2015, numbers.Real)
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
