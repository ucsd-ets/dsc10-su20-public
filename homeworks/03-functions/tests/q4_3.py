test = {
  'name': 'Question 4_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> callable(firstname_length)
          True
          >>> firstname_length('Quer, Giorgio') == 7
          True
          >>> firstname_length('Twomey, Robert') == 6
          True
          >>> firstname_length('Tiefenbruck, Janine') == 6
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
