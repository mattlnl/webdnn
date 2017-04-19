import numpy as np

from graph_builder.graph.graph import Variable
from graph_builder.graph import Attribute
from graph_builder.graph.operators import attributes as A
from graph_builder.graph.variables import attributes as VA


class Constant(Variable):
    data: np.array

    def __init__(self, data: np.array, order: Attribute):
        super(Constant, self).__init__(data.shape, order)
        self.data = data
        self.attributes.add(VA.Constant)

    def __repr__(self):
        order_repr = ''.join(map(lambda e: e.name, self.axis_order.axes))
        return f"<Constant shape={self.shape}, order=\"{order_repr}\">"
