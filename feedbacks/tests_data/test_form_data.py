__all__ = ['FEEDBACK_VALID_DATA', 'FEEDBACK_INVALID_DATA', ]

FEEDBACK_VALID_DATA = [{'feedback': 'Some feedback', 'min_value': 0,
                        'max_value': 10, 'indicator': 'PDI', },
                       {'feedback': 'Some valid feedback', 'min_value': 5,
                        'max_value': 10, 'indicator': 'PDI', },
                       {'feedback': 'Some valid feedback', 'min_value': 9,
                        'max_value': 10, 'indicator': 'PDI', },
                       {'feedback': 'Some valid feedback', 'min_value': 40,
                        'max_value': 50, 'indicator': 'PDI', },
                       {'feedback': 'Some valid feedback', 'min_value': 20,
                        'max_value': 60, 'indicator': 'PDI', },
                       ]

FEEDBACK_INVALID_DATA = [{'feedback': 'Some feedback', 'min_value': 10,
                          'max_value': 10, 'indicator': 'PDI', },
                         {'feedback': 'Some valid feedback', 'min_value': 11,
                          'max_value': 10, 'indicator': 'PDI', },
                         {'feedback': 'Some valid feedback', 'min_value': 50,
                          'max_value': 10, 'indicator': 'PDI', },
                         {'feedback': 'Some valid feedback', 'min_value': 99,
                          'max_value': 5, 'indicator': 'PDI', },
                         {'feedback': 'Some valid feedback', 'min_value': 23,
                          'max_value': 7, 'indicator': 'PDI', },
                         ]
