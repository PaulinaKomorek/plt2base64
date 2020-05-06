# plt2base64
### description
pyplot extension function that allows to save plot as base64 string
### installation
`wget https://raw.githubusercontent.com/PaulinaKomorek/plt2base64/master/plt2base64.py > plt2base64.py`
### sample usage
```python
import matplotlib.pyplot as plt
import plt2base64

plt.plot([0, 1, 2], [0, 1, 2])
b64 = plt.to_base64()
```

