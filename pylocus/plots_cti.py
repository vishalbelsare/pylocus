#!/usr/bin/env python
# module PLOTS_CTI
import matplotlib.pyplot as plt
import numpy as np

LINESTYLES = ['-', ':', '--', '-.', '-', ':', '--', '-.', '-', ':', '--', '-.']
MARKERS = [".", "o", "v", "+", "^", ">", "1",
           "2", "3", "4", "8", "s", "p", "*", "h"]

COLORS = ["black", "blue", "fuchsia", "gray", "aqua", "green", "lime",
          "maroon", "navy", "olive", "purple", "red", "silver", "teal", "yellow"]


def plot_tag_position(point_sets, title='', size=[10, 10], filename='', names=None, display_lines=False, index=0):
    import itertools
    if names is None:
        names = ['Original']
        for i in range(len(point_sets)):
            names.append('Method {}'.format(i + 1))
    f = plt.figure()
    ax = f.add_subplot(111)
    plt.gca().set_aspect('equal', adjustable='box')
    # Set range automatically
    delta = 1.0
    xmin = np.min(point_sets[0][:, 0]) - delta
    ymin = np.min(point_sets[0][:, 1]) - delta
    xmax = np.max(point_sets[0][:, 0]) + delta
    ymax = np.max(point_sets[0][:, 1]) + delta
    plt.axis((xmin, xmax, ymin, ymax))

    legend = []
    for p, points in enumerate(point_sets):
        N = points.shape[0]
        if p == 0:
            for i in range(N):
                plt.plot(points[i, 0], points[i, 1], '.k')
                ax.annotate('%s' % i, xy=(
                    points[i, 0], points[i, 1]), textcoords='data', size=20, weight='bold')
        #plot tag position
        plt.plot(points[index, 0], points[index, 1], marker=MARKERS[p],
                 color=COLORS[p + 1], label=names[p], linewidth=2.0)
        if display_lines:
            for pair in itertools.combinations(range(N), 2):
                plt.plot([points[pair[0], 0], points[pair[1], 0]], [points[pair[0], 1],

                                                                    points[pair[1], 1]], linestyle=LINESTYLES[p], color=COLORS[p], linewidth=2.0)
    f.set_size_inches(size)
    if title == '':
        plt.title('N = %r' % N)
    else:
        plt.title(title)
    if filename != '':
        plt.savefig(filename)
    plt.legend(loc='best')
    plt.show()


def plot_point_sets(point_sets, title='', size=[10, 10], filename='', names=None, display_lines=False, index=0):
    import itertools
    if names is None:
        names = ['Original']
        for i in range(len(point_sets)):
            names.append('Method {}'.format(i + 1))
    f = plt.figure()
    ax = f.add_subplot(111)
    plt.gca().set_aspect('equal', adjustable='box')
    # Set range automatically
    delta = 1.0
    xmin = np.min(point_sets[0][:, 0]) - delta
    ymin = np.min(point_sets[0][:, 1]) - delta
    xmax = np.max(point_sets[0][:, 0]) + delta
    ymax = np.max(point_sets[0][:, 1]) + delta
    plt.axis((xmin, xmax, ymin, ymax))

    legend = []
    for p, points in enumerate(point_sets):
        N = points.shape[0]
        for i in range(N):
            if i == 0:
                plt.plot(points[i, 0], points[i, 1], linestyle=':',
                         color=COLORS[p], marker=MARKERS[p], label=names[p])
            else:
                plt.plot(points[i, 0], points[i, 1], linestyle=':',
                         color=COLORS[p], marker=MARKERS[p])
            if p == 0:
                xy = (points[i, 0], points[i, 1])
                ax.annotate('%s' % i, xy=xy, textcoords='data',
                            size=20, weight='bold')
        if display_lines:
            for pair in itertools.combinations(range(N), 2):
                xs = [points[pair[0], 0], points[pair[1], 0]]
                ys = [points[pair[0], 1], points[pair[1], 1]]
                plt.plot(
                    xs, ys, linestyle=LINESTYLES[p], color=COLORS[p], linewidth=2.0)
    f.set_size_inches(size)
    if title == '':
        plt.title('N = %r' % N)
    else:
        plt.title(title)
    if filename != '':
        plt.savefig(filename)
    plt.legend(loc='best')
    plt.show()


def plot_point_sets_3d(point_sets, names, title='', display_lines=False):

    from mpl_toolkits.mplot3d import Axes3D
    import itertools
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Set range automatically
    delta = 1.0
    xmin = np.min(point_sets[0][:, 0]) - delta
    ymin = np.min(point_sets[0][:, 1]) - delta
    zmin = np.min(point_sets[0][:, 2]) - delta
    xmax = np.max(point_sets[0][:, 0]) + delta
    ymax = np.max(point_sets[0][:, 1]) + delta
    zmax = np.max(point_sets[0][:, 2]) + delta
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_zlim(zmin, zmax)
    for counter, X in enumerate(point_sets):
        N = X.shape[0]
        first = True
        for pairs in itertools.combinations(range(N), 2):
            x = X[pairs, 0]
            y = X[pairs, 1]
            z = X[pairs, 2]
            if first:
                if display_lines:
                    ax.plot(x, y, z, color=COLORS[counter], linestyle=LINESTYLES[
                            counter], label=names[counter])
                first = False
            else:
                if display_lines:
                    ax.plot(x, y, z, color=COLORS[counter],
                            linestyle=LINESTYLES[counter])
        # plot tag position
        ax.plot([X[-1, 0]], [X[-1, 1]], [X[-1, 2]], marker=MARKERS[counter],
                color=COLORS[counter + 1], label=names[counter], linewidth=2.0)

    ax.set_title(title)
    ax.legend()
    plt.show()


def plot_points(points, title, size=[5, 2], filename=''):
    if DARK:
        color = (0.2, 0.6, 0.1)
    else:
        color = None
    f = plt.figure()
    ax = f.add_subplot(111)
    plt.gca().set_aspect('equal', adjustable='box')
    legend = []
    N = points.shape[0]
    for i in range(N):
        for j in range(i + 1, N):
            plt.plot([points[i, 0], points[j, 0]],
                     [points[i, 1], points[j, 1]], color=color)
            legend.append(str(i) + str(j))
    for i in range(N):
        ax.annotate('%s' % i, xy=(
            points[i, 0], points[i, 1]), textcoords='data')
    plt.axis('off')
    #plt.legend(legend, loc='best')
    f.set_size_inches(size)
    plt.title(title)
    if filename != '':
        plt.savefig(filename)
    plt.show()


def plot_cost_function(deltas, x_0, x_delta, fs, name):
    plt.figure()
    plt.plot(deltas + x_0, fs, label='f')
    plt.vlines(x_0, min(fs), max(fs), linestyle=':',
               label='current {}={:2.2f}'.format(name, x_0))
    plt.vlines(x_delta, min(fs), max(fs), linestyle='-.',
               label='next {}={:2.2f}'.format(name, x_delta))
    plt.xlabel('${}+\\Delta$'.format(name))
    plt.ylabel('f')
    plt.legend()
    plt.title('$f_i$ around best {}+$\\Delta$'.format(name))


def create_multispan_plots(tag_ids):
    """Create detail plots (first row) and total block(second row) of experiments.
    
    Args:
            tag_ids: list of tag-dictionaries, where the dictionaries must have fields 'name' (used for naming) 
                     and 'id' (used for numbering axis_dict)
    
    Returns:
            Figure element fig, ax_dict containing the first row plots (accessed via id) and ax_total containing the 
            second row block. 
    """
    import matplotlib.gridspec as gridspec
    fig = plt.figure()
    gs = gridspec.GridSpec(2, len(tag_ids))
    ax_list = [fig.add_subplot(g) for g in gs]
    ax_dict = {}
    for i, tag_dict in enumerate(tag_ids):
        ax_dict[tag_dict['id']] = ax_list[i]
    ax_total = plt.subplot(gs[1, :])

    fig.set_size_inches(10, 10)
    for tag_dict in tag_ids:
        ax_dict[tag_dict['id']].set_title(
            'System {} (id {})'.format(tag_dict['name'], tag_dict['id']))
    ax_total.set_title('Total')
    gs.tight_layout(fig, rect=[0, 0.03, 1, 0.95])
    return fig, ax_dict, ax_total


def plot_matrix(matrix, title='matrix', yticks=None, saveas=''):
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    fig = plt.figure(figsize=(5, 5))
    ax = plt.subplot(111)

    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.05)

    im = ax.imshow(matrix, interpolation='none')

    fig.colorbar(im, cax=cax)  # Create the colorbar
    if yticks is not None:
        plt.yticks(range(matrix.shape[0]), yticks)
    if saveas != '':
        plt.tight_layout()
        plt.savefig(saveas)
    plt.show()


if __name__ == "__main__":
    print('nothing happens when running this module.')
