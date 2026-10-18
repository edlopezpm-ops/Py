# (kommiBo) Synthetic documentation example; no personal records.
from copy import deepcopy
from _cv_source import cv
source = {'profile': {'name': 'Synthetic Candidate', 'phone': 0}, 'skills': ['SQL', 123], 'experience': [{'role': 'Analyst', 'bullets': ['Synthetic note', 7]}]}
before = deepcopy(source)
normalized = cv.normalize_cv(source)
assert source == before
assert normalized['profile']['phone'] == ''
assert normalized['profile']['email'] == ''
assert normalized['skills'] == ['SQL', '123']
assert normalized['experience'][0]['bullets'] == ['Synthetic note', '7']
assert normalized['education'] == []
print('schema filled; values coerced; source unchanged; zero phone becomes empty')
