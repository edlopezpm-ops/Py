# (kommiBo) Synthetic documentation example; no personal records.
from _cv_source import cv
cleaned = cv.clean_text('<style>hidden</style><p>Python &amp; SQL</p><script>secret()</script> automation')
assert cleaned == 'Python & SQL automation'
assert cv.tokens(cleaned) == ['python', 'sql', 'automation']
assert cv.tokens('an a AI C# Python') == ['python']
print('Python & SQL automation -> python, sql, automation; short tokens excluded')
