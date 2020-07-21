
test = {
  'name': 'q2_4',
  'hidden': False,
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a dataframe
	>>> isinstance(percent_free_beaches, bpd.DataFrame)
	True
	>>> set(percent_free_beaches.columns) == {'TOTAL', 'PERCENT_FREE'}
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
