test = {
  'hidden': False,
  'name': '2.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> one_resample.get("serial_number").iloc[0] == 108
          True
          >>> one_resample.get("serial_number").iloc[16] == 78
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
