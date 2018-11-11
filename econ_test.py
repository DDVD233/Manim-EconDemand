from big_ol_pile_of_manim_imports import *


class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "y_min": 0,
        "y_max": 10,
        "function_color": RED,
        "axes_color": GREEN,
        "x_labeled_nums": range(1, 10, 1),
        "x_axis_label": "$Q_{Oil}$",
        "y_axis_label": "$P_{Oil}$",
    }

    def construct(self):
        self.setup_axes(animate=False)

        func_graph = self.get_graph(self.func_to_graph, self.function_color, x_min=2, x_max=9)
        func_graph_copy = self.get_graph(self.func_to_graph, self.function_color, x_min=2, x_max=9)
        func_graph2 = self.get_graph(self.func_to_graph2, x_min=1, x_max=8)
        func_graph2_copy = self.get_graph(self.func_to_graph2, x_min=1, x_max=8)
        vert_line = self.get_vertical_line_to_graph(4.01786, func_graph, color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label="Demand")
        graph_lab2 = self.get_graph_label(func_graph2, label="Supply")
        eq_price = TexMobject("Eq")
        label_coord = self.input_to_graph_point(4.01786, func_graph)
        eq_price.next_to(label_coord, RIGHT + UP)

        self.play(ShowCreation(func_graph), ShowCreation(func_graph2))
        new_demand = self.get_graph(self.new_demand_func, self.function_color, x_min=1, x_max=8)
        new_supply = self.get_graph(self.new_supply_func, BLUE, x_min=1, x_max=8)
        new_vert_line = self.get_vertical_line_to_graph(4.73214, new_supply, color=YELLOW)
        new_eq_coord = self.input_to_graph_point(4.73214, new_supply)
        new_eq_price = TexMobject("new Eq")
        new_eq_price.next_to(new_eq_coord, RIGHT + UP)
        self.play(
            ShowCreation(func_graph2_copy),
            ShowCreation(vert_line),
            ShowCreation(graph_lab),
            ShowCreation(graph_lab2),
            ShowCreation(eq_price),
        )
        self.play(
            Transform(func_graph2, new_supply, run_time=2),
            Transform(vert_line, new_vert_line, run_time=2),
            Transform(eq_price, new_eq_price, run_time=2)
        )
        self.wait(5)

    def func_to_graph(self, x):
        result = math.pow(0.4*x-3.5, 2) + 1.5
        return result

    def new_demand_func(self, x):
        result = math.pow(0.4*x-4.5, 2) + 1.5
        return result

    def new_supply_func(self, x):
        return math.pow(0.4 * x, 2) + 0.5

    def func_to_graph2(self, x):
        return math.pow(0.4*x, 2) + 2.5
