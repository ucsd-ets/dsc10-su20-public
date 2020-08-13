test = {
  'hidden': False,
  'name': '3.3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.mean(left_end) > 90
          True
          >>> np.mean(left_end) < 100
          True
          >>> np.mean(right_end) > 145
          True
          >>> np.mean(right_end) < 155
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
