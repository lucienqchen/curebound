import os
import pandas as pd
import numpy as numpy
import re


def query_data(df, column, content):

    """
    Purpose: Query specific rows in [df] where value at column [column]
    matches string [content]

    Params:
    df (dataframe): subject dataframe
    column (str): column to match content
    content (str): value to match column [column]

    Return: (dataframe) - subset of df with rows where values of column 
    [column] contain [content]

    """

    return df[df[column].str.contains(content)]


def working_directory():

    """
    Purpose: show current working directory

    """

    return os.getcwd()


def export_data(wp, df, filename):

    """
    Purpose: Save dataframe [df] to path [wp]
    
    Params:
    wp (str): write path containing the directory to store data
    df (dataframe): subject dataframe
    filename (str): the file name to store [df] 

    Return: None

    """

    wp = os.path.join(wp, filename)
    df.to_csv(wp)
    print(f'Successfully saved {filename} at: {wp}')


def export_fig(wp, figure, filename):

    """
    Purpose: Save figure [figure] to path [wp]
    
    Params:
    wp (str): write path containing the directory to store figure
    figure (plotly): subject figure
    filename (str): the file name to store [figure] 

    Return: None

    """

    wp = os.path.join(wp, filename)
    figure.write_html(wp)
    print(f'Successfully saved {filename} at: {wp}')


def query_by_columns(df, re_pattern):

    """
    Purpose: Query column in dataframe [df] by column names that match
    the regex pattern [re_pattern]

    Params:
    df (dataframe): subject dataframe
    re_pattern (str): regex pattern to match column names

    Return: (dataframe) - subset of [df] containing columns where name matches
    regex pattern

    """

    columns = [True if re.search(re_pattern, x) else False for x in df.columns]
    columns[-1] = True
    return df.loc[:, columns]

