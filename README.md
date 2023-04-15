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
![image](https://user-images.githubusercontent.com/47920109/232233336-76c87128-c1fe-46cf-bb0a-ddf7b584da16.png)


## `bar`

```python
visualimiss.bar(df)
```
![image](https://user-images.githubusercontent.com/47920109/232233350-9ca056c5-f3f3-4a68-ace2-a2fbab520e2d.png)


# Configuration
## Sorting
```python
visualimiss.matrix(df, sort='asc')
```
![image](https://user-images.githubusercontent.com/47920109/232233399-aa4055e9-633f-4201-9a87-44da9e4ae1a4.png)

## Rotate, hide label
```python
# visualimiss.matrix(df, label_rotation=90)
visualimiss.matrix(df, show_label=False)
```
![image](https://user-images.githubusercontent.com/47920109/232233625-edbc6586-68f8-4622-80e9-07aa1c1168bb.png)

## Change color, font size
```python
visualimiss.matrix(df, color=(43, 102, 189), fontsize=16)
```
![image](https://user-images.githubusercontent.com/47920109/232233769-fe5738f9-dcf5-4663-b9bb-a5bd7f9709e6.png)

