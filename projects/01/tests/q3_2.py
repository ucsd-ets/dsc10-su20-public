
test = {
  'name': 'q3_2',
  'hidden': False,
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a dataframe
	>>> isinstance(sea_temp_fahrenheit, bpd.DataFrame)
	True
	>>> set(sea_temp_fahrenheit.columns) == {'YEAR', 'MONTH', 'DAY', 'SURFACE_TEMP'}
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
