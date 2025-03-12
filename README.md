# What are computers good for? Spoiler: it's not (precise) computing

Files from the Unseminar on precise computing on 2025/03/12
- Python test cases
- Julia example: pi approximation (Pluto Notebook)
- R example: banker's rounding (Jupyter Notebook)
- Recommendations (python Jupyter Notebook)

## Test cases (python)

1. `10.0 * 0.1 == 1.0`
2. `0.1 * 0.1 == 0.01`
3. `0.5 * 0.5 == 0.25`
4. `0.1 + 0.1 == 0.2`
5. `0.1 + 0.1 + 0.1 == 0.3`
6. `0.1 + 0.1 + 0.1 + 0.1 == 0.4`
7. `(0.1 + 0.1) + 1 == 0.1 + (0.1 + 1)`
8. `1_00000_00000_00000_00000 + 1 > 1_00000_00000_00000_00000`
9. `1e20 + 1 > 1e20`
10. `1e20 + 1000 > 1e20`
11. `0.1**25 > 0`
12. `0.1**5**5 > 0`
13. `np.all(a>0)`
14. `np.sum(a) > 0`

For 13 and 14:
```python
import numpy as np
large_number = 2**63-1
a = np.array([large_number, large_number])
```
