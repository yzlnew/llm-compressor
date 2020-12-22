from typing import List, Union, Iterable, Dict
import os
from collections import OrderedDict
import numpy
import tensorflow as tf

from neuralmagicML.utils import create_dirs


__all__ = ["tf_compat", "tf_compat_div", "tensor_export", "tensors_export"]


tf_compat = (
    tf
    if not hasattr(tf, "compat") or not hasattr(getattr(tf, "compat"), "v1")
    else tf.compat.v1
)  # type: tf
tf_compat_div = (
    tf_compat.div
    if not hasattr(tf_compat, "math")
    or not hasattr(getattr(tf_compat, "math"), "divide")
    else tf_compat.math.divide
)
