OK_FORMAT = True

test = {   'name': 'q4_4_4',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> "gdp_pc" in list(cleaned_gdp.columns)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.isclose(cleaned_gdp[(cleaned_gdp[\'country\'] == "Singapore") & (cleaned_gdp[\'year\'] == 1960)][\'gdp_pc\'].values[0], 9284.94520345)\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
