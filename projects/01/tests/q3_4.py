
test = {
  'name': 'q3_4',
  'hidden': False,
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a list
	>>> isinstance(top_5_hottest_years, list)
	True
	>>> len(top_5_hottest_years)
	5
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
