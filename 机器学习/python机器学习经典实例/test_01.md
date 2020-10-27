```python
"""打印ascii字母表、数字、标点符号"""
import string

for item in [string.ascii_letters,string.digits,
             string.punctuation]:
    print('{}\t{}'.format(len(item),item))
```
