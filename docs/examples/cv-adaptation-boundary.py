# (kommiBo) Synthetic documentation example; no personal records.
from copy import deepcopy
from _cv_source import cv
base = {'profile': {'name': 'Synthetic Candidate', 'title': 'Generalist', 'summary': 'Synthetic example only.'}, 'skills': ['Gardening', 'SQL'], 'experience': [{'role': 'Analyst', 'company': 'Example', 'bullets': ['Maintained a garden.', 'Built SQL reports.']}]}
before = deepcopy(base)
adapted = cv.adapt_cv(base, 'Data Analyst\nSQL automation')
assert base == before
assert adapted['profile']['title'] == 'Data Analyst'
assert adapted['skills'] == ['SQL', 'Gardening']
assert set(adapted['experience'][0]['bullets']) == set(base['experience'][0]['bullets'])
assert 'automation' not in adapted['skills']
assert 'automation' not in adapted['analysis']['missing_keywords']
print('SQL promoted; existing content preserved; base unchanged; summary affects missing-keyword analysis')
