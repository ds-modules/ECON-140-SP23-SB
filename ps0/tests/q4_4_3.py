OK_FORMAT = True

test = {   'name': 'q4_4_3',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> np.all(cleaned_gdp['emp'] > -1)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.all(cleaned_gdp['cn'] > -1)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.all(cleaned_gdp['cgdpe'] > -1)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> cleaned_gdp.shape[0] == 8834\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> min(cleaned_gdp[cleaned_gdp[\'country\'] == "Aruba"]["year"]) == 1991\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
