test = {
  'hidden': False,
  'name': '1.4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # One or more of the reaction results could be incorrect
          >>> np.count_nonzero(ten_nachos_reactions.get('Reactions') == np.array(['Meh.', 'Cheesy!', 'Wow!', 'Wow!', 'Cheesy!', 'Spicy!', 'Wow!', 'Meh.', 'Cheesy!', 'Wow!'])) == 10
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
