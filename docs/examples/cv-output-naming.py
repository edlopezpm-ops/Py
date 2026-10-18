# (kommiBo) Synthetic documentation example; no personal records.
from _cv_source import cv
assert cv.safe_filename('  Synthetic / Analyst:*  ') == 'Synthetic--Analyst'
assert cv.safe_filename('???') == 'cv'
assert len(cv.safe_filename('x' * 100)) == 80
assert cv.safe_filename('../sample') == '..sample'
assert cv.safe_filename('CON') == 'CON'
print('cleanup and fallback observed; capped at 80; dots and reserved CON remain')
