# (kommiBo) Synthetic documentation example; no personal records.
from _cv_source import cv
complete = cv.assess_fit({'cv': 'Python SQL automation', 'experience': ''}, 'Python SQL automation')
absent = cv.assess_fit({'cv': 'Gardening', 'experience': ''}, 'Python SQL automation')
empty = cv.assess_fit({'cv': 'Python', 'experience': ''}, '')
assert (complete['score'], complete['recommendation']) == (96, 'Proceed')
assert (absent['score'], absent['recommendation']) == (8, 'Pause')
assert empty['score'] == 8 and empty['keywords'] == []
assert set(complete['matched_keywords']) == {'python', 'sql', 'automation'}
print('complete=96/Proceed; absent=8/Pause; empty vacancy=8 with no keywords')
