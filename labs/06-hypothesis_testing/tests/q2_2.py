test = {
  'hidden': False,
  'name': '2.2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # ----------------------------------------------
          >>> # There should be around 1 faulty phone in avg
          >>> # ----------------------------------------------
          >>> 1.5 < np.mean(simulations) < 2.5
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
