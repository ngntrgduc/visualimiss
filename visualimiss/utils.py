import numpy as np

def nullity_sort(df, sort=None):
    
    if sort is None:
        return df
    elif sort not in ['asc', 'desc']:
        raise ValueError('The `sort` parameter must be set to "asc" or "desc".')
    
    values = df.count(axis='rows').values
    
    if sort == 'asc':
        return df.iloc[:, np.argsort(values)]
    elif sort == 'desc':
        return df.iloc[:, np.flipud(np.argsort(values))]