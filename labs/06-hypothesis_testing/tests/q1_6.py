test = {
  'hidden': False,
  'name': '1.6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(model_proportions) % 2 == 0
          True
          >>> len(np.unique(model_proportions)) == 1
          True
          >>> sum(model_proportions) == 1
          True
          >>> isinstance(simulation_proportion,float) or isinstance(simulation_proportion, numpy.float64)
          True
          >>> 0 <= one_test_statistic <= 20
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
