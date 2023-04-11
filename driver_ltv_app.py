# turning the ipython notebook into a streamlit app

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import warnings

warnings.filterwarnings("ignore")