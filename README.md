# visualimiss
[![](https://img.shields.io/pypi/v/visualimiss?style=flat-square)](https://pypi.org/project/visualimiss/)
[![](https://img.shields.io/badge/python-3.7+-blue.svg?style=flat-square)](https://www.python.org/downloads/)
[![](https://img.shields.io/github/license/ngntrgduc/visualimiss?style=flat-square)](https://github.com/ngntrgduc/visualimiss/blob/master/LICENSE)

"**visuali**ze **miss**ing data". A simple [missingno](https://github.com/ResidentMario/missingno)
clone. Some features were removed from the original and some were added.

# Features
Some features differ from the original one:
- Have `matrix()`, `bar()` modified function from the original one
- Simpler and faster
- Maybe more readable?

# Installation
```
pip install visualimiss
```
This also install all dependencies: [Numpy](https://numpy.org/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/)

# Quickstart
This quickstart uses datasets of the [NYPD Motor Vehicle Collisions Dataset](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95). 
```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/ResidentMario/missingno-data/master/nyc_collision_factors.csv")
```

## `matrix`

```python
visualimiss.matrix(df)
```

## `bar`

```python
visualimiss.bar(df)
```

# Configuration
## Sorting

## Rotate, hide label

## Change color, font size
