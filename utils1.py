# -*- coding: utf-8 -*-
"""utils1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1feoOp2WsHG-UQA8P6qq4CAjykpBhpqts
"""
import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()