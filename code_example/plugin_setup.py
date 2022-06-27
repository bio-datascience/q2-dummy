import sys
import os
from os.path import dirname

import q2_dummy

from qiime2.plugin import (Plugin,  Str)
from q2_types.feature_table import FeatureTable, Composition, Frequency
import importlib

q2_dummy_dir = dirname(os.getcwd())
sys.path.append(q2_dummy_dir)


plugin = Plugin(
    name="dummy",
    version="0.0.0.dev0",
    website="https://github.com/Vlasovets/q2-gglasso",
    package="q2-dummy",
    short_description=(
        "Testing q2-plugin development"
    ),
    description=(
        "Testing q2-plugin development"
    ),
)


plugin.methods.register_function(
    function=q2_dummy.transform_features,
    inputs={"table": FeatureTable[Composition | Frequency]},
    parameters={"transformation": Str},
    outputs=[("transformed_table", FeatureTable[Composition])],
    input_descriptions={
        "table": (
            "Matrix representing the compositional "
            "data of the problem, in order to clr transform it"
        ),
    },
    parameter_descriptions={
        "transformation": (
            "String representing the name of the "
            "transformation we will use "
        ),
    },
    output_descriptions={"transformed_table": "Matrix representing the data of the problem"},
    name="transform-features",
    description=(
        "Perform transformation, "
        "from FeatureTable[Frequency]"
        " prior to network analysis"
        " default transformation is centered log ratio"
    ),
)
importlib.import_module('q2_dummy._transformer')

