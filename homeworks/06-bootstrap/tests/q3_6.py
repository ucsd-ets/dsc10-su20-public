test = {
  'name': 'Question 3_6',
  'points': 1,
  'hidden': False,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numbers
          >>> isinstance(lower_bound_in_n_out, numbers.Real)
          True
          >>> isinstance(upper_bound_in_n_out, numbers.Real)
          True
          >>> lower_bound_in_n_out <= upper_bound_in_n_out
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
