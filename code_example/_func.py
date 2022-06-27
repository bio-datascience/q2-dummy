import pandas as pd

from biom.table import Table
from q2_dummy.utils import normalize, log_transform

def transform_features(
        table: Table, transformation: str = "clr",
) -> pd.DataFrame:
    if transformation == "clr":
        X = table.to_dataframe()
        X = normalize(X)
        X = log_transform(X, transformation=transformation)

        return pd.DataFrame(X)
    else:
        raise ValueError(
            "Unknown transformation name, use clr and not %r" % transformation
        )