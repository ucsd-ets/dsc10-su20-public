
test = {
  'name': 'q2_3',
  'hidden': False,
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be an integer
	>>> import numbers
	>>> isinstance(san_diego_free_beaches_with_parking, numbers.Integral)
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
