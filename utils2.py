# -*- coding: utf-8 -*-
"""Untitls2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11zwCpIm0Iespe5DkTOwxFhGV5yqjEKbG
"""
import pandas as pd
from pyspark.sql.functions import *
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.sql.functions import *
from pyspark.ml.evaluation import RegressionEvaluator
import matplotlib.pyplot as plt
import seaborn as sns