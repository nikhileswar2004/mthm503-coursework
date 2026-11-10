
import pandas as pd  # noqa: F401


def select_column(df, column):
    return df[column]


def column_mean(df, column):
    return df[column].mean()


def filter_rows(df, column, threshold):
    return df[df[column] > threshold]


def sort_by_column(df, column, ascending=True):
    return df.sort_values(by=column, ascending=ascending)


def unique_values(df, column):
    return df[column].unique()


def frequencies_by_group(df, cat_col):
    return df[cat_col].value_counts()


def mean_by_group(df, value_col, group_col):
    return df.groupby(group_col)[value_col].mean()


def add_ratio_column(df, numerator, denominator, new_col):
    result = df.copy()
    result[new_col] = result[numerator] / result[denominator]
    return result


def drop_missing(df):
    return df.dropna()


def fill_missing(df, value):
    return df.fillna(value)
