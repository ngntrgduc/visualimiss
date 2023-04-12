import numpy as np

def nullity_sort(df, sort=None, axis='rows'):
    
    if sort is None:
        return df
    elif sort not in ['asc', 'desc']:
        raise ValueError("The `sort` parameter must be set to 'asc' or 'desc'.")
    
    if axis not in ['rows', 'columns']:
        raise ValueError("The `axis` parameter must be set to 'rows' or 'columns'.")
    
    values = df.count(axis=axis).values
    if axis == 'columns':
        if sort == 'asc':
            return df.iloc[np.argsort(values), :]
        elif sort == 'desc':
            return df.iloc[np.flipud(np.argsort(values)), :]
    elif axis == 'rows':
        if sort == 'asc':
            return df.iloc[:, np.argsort(values)]
        elif sort == 'desc':
            return df.iloc[:, np.flipud(np.argsort(values))]