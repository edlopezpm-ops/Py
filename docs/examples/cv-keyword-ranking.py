# (kommiBo) Synthetic documentation example; no personal records.
from _cv_source import cv
assert cv.score_text('Power BI and SQL', ['power bi', 'sql']) == 3
assert cv.score_text('NoSQL systems', ['sql']) == 1
items = ['unrelated first', 'SQL report', 'unrelated second']
assert cv.reorder_by_keywords(items, lambda value: value, ['sql']) == ['SQL report', 'unrelated first', 'unrelated second']
extracted = cv.extract_keywords('Python SQL automation Python')
assert {'python', 'sql', 'automation'} <= set(extracted)
assert len(extracted) == len(set(extracted))
print('phrase=2; single=1; ties stable; SQL matches NoSQL; extraction deduplicated')
