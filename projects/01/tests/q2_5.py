
test = {
  'name': 'q2_5',
  'hidden': False,
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a integer
	>>> import numbers
	>>> isinstance(number_on_101, numbers.Integral)
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
