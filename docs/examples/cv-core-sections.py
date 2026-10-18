# (kommiBo) Synthetic documentation example; no personal records.
from _cv_source import cv
core = {'cv': '\n'.join([
    'Synthetic Candidate', 'synthetic@example.invalid', '# Data Analyst',
    'PROFESSIONAL SUMMARY', 'Synthetic reporting experience.',
    'CORE EXPERTISE', 'SQL | Python • Documentation',
    'PROFESSIONAL EXPERIENCE', '## Example Organization',
    'Analyst | 2020-2021', '- Built a synthetic report.',
    'EDUCATION', 'Example Degree', 'Example Institute', 'ADDITIONAL INFORMATION',
])}
result = cv.core_to_cv(core)
assert result['profile']['name'] == 'Synthetic Candidate'
assert result['skills'] == ['SQL', 'Python', 'Documentation']
assert result['experience'][0]['company'] == 'Example Organization'
assert result['education'][0]['degree'] == 'Example Degree'
assert cv.lines_between('first\nsecond', 'MISSING') == ['first', 'second']
print('three skills; one experience; one education; missing start falls back to first line')
