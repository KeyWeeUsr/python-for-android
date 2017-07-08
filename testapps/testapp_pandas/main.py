import numpy as np
import pandas as pd

from kivy.app import runTouchApp
from kivy.uix.textinput import TextInput

def dummy_dataframe():
    df = pd.DataFrame({
        'A' : ['one', 'one', 'two', 'three'] * 3,
        'B' : ['A', 'B', 'C'] * 4,
        'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
        'D' : np.random.randn(12),
        'E' : np.random.randn(12)
    })
    return str(df)

runTouchApp(
    TextInput(readonly=True, text=dummy_dataframe())
)
