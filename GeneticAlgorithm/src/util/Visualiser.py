import imageio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from scipy.interpolate import interp1d


class Visualiser:

    @staticmethod
    def generate_graph(tour, population_number):
        x_axis = []
        y_axis = []
        for city in tour:
            x_axis.append(city.get_x())
            y_axis.append(city.get_y())
        x_axis.append(tour[0].get_x())
        y_axis.append(tour[0].get_y())

        tour_length = tour.get_length()
        text = 'Travelling Salesman Problem' + '\n' + \
               'Generation ' + str(population_number) + ' | ' + \
               'Tour Length ' + str(round(tour_length, 2))

        plt.plot(x_axis, y_axis, marker='.')
        plt.title(text, fontname="Roboto Condensed", fontsize=13)
        plt.xlabel('x axis', fontname="Roboto Condensed", fontsize=13)
        plt.ylabel('y axis', fontname="Roboto Condensed", fontsize=13)
        return plt

    def save_graph(self, tour, population_number, filenames):
        filename = 'graph' + str(population_number) + '.png'
        filenames.append(filename)
        self.generate_graph(tour, population_number).savefig('../data/pngs/' + filename)

    @staticmethod
    def save_gif(filenames):
        with imageio.get_writer('../data/animated_TSP.gif', mode='I') as writer:
            for filename in filenames:
                image = imageio.imread('../data/pngs/' + filename)
                writer.append_data(image)

    # experiment graph generators:

    @staticmethod
    def vertical_bar_plot(title, x, y, xlabel, ylabel,
                          x_axis_label_steps, bar_thickness,
                          xlim, ylim, bar_descr_y_coord):
        fig, ax = plt.subplots(figsize=(16, 9))
        Visualiser.add_data_to_graph(plt, title, xlabel, ylabel)
        plt.bar(x, y, color="#b3dbd0", width=bar_thickness)
        # Add annotation to bars
        for i in ax.patches:
            plt.text(i.get_x() + (i.get_width() / 2.5),  # x coordinate
                     i.get_height() + bar_descr_y_coord,  # y coordinate
                     str(round((i.get_height()), 2)), fontname="Roboto Condensed", fontsize=13)

        # style graph
        Visualiser.remove_ax_spines_and_ticks(ax)
        ax.xaxis.set_major_locator(MultipleLocator(x_axis_label_steps))  # set frequency of tick labels
        ax.xaxis.set_tick_params(pad=6)  # padding between axis and labels
        ax.invert_xaxis()  # Show top values
        ax.grid(axis="x", visible=False)  # disable x grid lines
        ax.grid(axis="y", visible=True, color='grey', linewidth=0.5, alpha=0.5)
        plt.xticks(fontname="Roboto Condensed", fontsize=13)
        plt.yticks(fontname="Roboto Condensed", fontsize=13, color="lightgrey")
        Visualiser.set_axis_ranges(plt, xlim, ylim)
        return plt

    @staticmethod
    def vertical_bar_plot_with_labels(title, x, y, xlabel, ylabel,
                          x_axis_label_steps, bar_thickness,
                          xlim, ylim, bar_descr_y_coord, tick_labels):
        fig, ax = plt.subplots(figsize=(16, 9))
        Visualiser.add_data_to_graph(plt, title, xlabel, ylabel)

        plt.bar(x, y, color="#b3dbd0", width=bar_thickness)
        # Add annotation to bars
        for i in ax.patches:
            plt.text(i.get_x() + (i.get_width() / 2.5),  # x coordinate
                     i.get_height() + bar_descr_y_coord,  # y coordinate
                     str(round((i.get_height()), 2)), fontname="Roboto Condensed", fontsize=13)

        # style graph
        Visualiser.remove_ax_spines_and_ticks(ax)
        ax.xaxis.set_major_locator(MultipleLocator(x_axis_label_steps))  # set frequency of tick labels
        ax.xaxis.set_tick_params(pad=6)  # padding between axis and labels
        ax.set_xticks(x)
        ax.set_xticklabels(tick_labels, fontname="Roboto Condensed", fontsize=13)
        ax.invert_xaxis()  # Show top values
        ax.grid(axis="x", visible=False)  # disable x grid lines
        ax.grid(axis="y", visible=True, color='grey', linewidth=0.5, alpha=0.5)
        plt.xticks(fontname="Roboto Condensed", fontsize=13)
        plt.yticks(fontname="Roboto Condensed", fontsize=13, color="lightgrey")
        Visualiser.set_axis_ranges(plt, xlim, ylim)
        return plt


    @staticmethod
    def horizontal_bar_plot(title, x, y, xlabel, ylabel,
                            y_axis_label_steps, bar_thickness,
                            xlim, ylim, bar_descr_x_coord):
        fig, ax = plt.subplots(figsize=(16, 9))
        Visualiser.add_data_to_graph(plt, title, xlabel, ylabel)
        ax.barh(y, x, color="#b3dbd0", height=bar_thickness)
        # Add annotation to bars
        for i in ax.patches:
            plt.text(i.get_width() + bar_descr_x_coord,  # x coordinate
                     i.get_y() + (i.get_height() / 2.5),  # y coordinate
                     str(round((i.get_width()), 2)), fontname="Roboto Condensed", fontsize=13)

        # style graph
        Visualiser.remove_ax_spines_and_ticks(ax)
        ax.yaxis.set_major_locator(MultipleLocator(y_axis_label_steps))  # set frequency of tick labels
        ax.yaxis.set_tick_params(pad=6)  # padding between axis and labels
        ax.invert_yaxis()  # Show top values
        ax.grid(axis="x", visible=True, color='grey', linewidth=0.5, alpha=0.5)
        ax.grid(axis="y", visible=False)  # disable y grid lines
        plt.xticks(fontname="Roboto Condensed", fontsize=13, color="lightgrey")
        plt.yticks(fontname="Roboto Condensed", fontsize=13)
        Visualiser.set_axis_ranges(plt, xlim, ylim)
        return plt

    @staticmethod
    def line_graph(title, x, y, xlabel, ylabel, xlim, ylim,
                   x_axis_label_steps, y_axis_label_steps):
        fig, ax = plt.subplots(figsize=(16, 9))
        cubic_interpolation_model = interp1d(x, y, kind="cubic")
        x_ = np.linspace(x.min(), x.max(), 500)
        y_ = cubic_interpolation_model(x_)
        plt.plot(x_, y_, color="#b3dbd0", linewidth=2)
        Visualiser.add_data_to_graph(plt, title, xlabel, ylabel)
        # style graph
        Visualiser.remove_ax_spines_and_ticks(ax)
        ax.xaxis.set_major_locator(MultipleLocator(x_axis_label_steps))  # set frequency of tick labels
        ax.yaxis.set_major_locator(MultipleLocator(y_axis_label_steps))
        ax.yaxis.set_tick_params(pad=6)  # padding between axis and labels
        ax.grid(axis="both", visible=True, color='grey', linewidth=0.5, alpha=0.5)
        plt.xticks(fontname="Roboto Condensed", fontsize=13)
        plt.yticks(fontname="Roboto Condensed", fontsize=13)
        Visualiser.set_axis_ranges(plt, xlim, ylim)
        return plt

    @staticmethod
    def remove_ax_spines_and_ticks(ax):
        for s in ['top', 'bottom', 'left', 'right']:
            ax.spines[s].set_visible(False)  # remove axes spines
        ax.xaxis.set_ticks_position('none')  # remove ticks
        ax.yaxis.set_ticks_position('none')

    @staticmethod
    def set_axis_ranges(plot, xlim, ylim):
        plot.xlim(xlim)  # set range of x axis
        plot.ylim(ylim)  # set range of y axis

    @staticmethod
    def add_data_to_graph(plot, title, xlabel, ylabel):
        plot.title(title, loc='left', fontname="Roboto Condensed", fontsize=18, fontweight="bold")
        plot.xlabel(xlabel, fontname="Roboto Condensed", fontsize=13)
        plot.ylabel(ylabel, fontname="Roboto Condensed", fontsize=13)
