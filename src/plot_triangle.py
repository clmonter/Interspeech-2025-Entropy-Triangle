import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl

def plot_simple_triangle(show=True):

    x = [0, 1, 0.5, 0]
    y = [0, 0, 1, 0]

    plt.figure()
    plt.plot(x, y, 'b-', linewidth=2) 
    plt.fill(x, y, 'skyblue', alpha=0.5)
    plt.scatter(x[:-1], y[:-1], color='black')

    plt.title('Triangle')
    plt.axis('equal')
    plt.grid(True)

    if show == True:
        plt.show()


def plot_coordinates(coordinates, color, size):
    plot_triangle_lines(show=False)
    plt.scatter(coordinates[0], coordinates[1], color=color, s=size)
    plt.show()

def convert_coordinates(three_coordinates):
    ## Convert [AH'PxPy, 2*MIPxy, VIPxy] to 2D in order to plot it into the triangle [x, y]

    V1 = np.array([1, 0])      #  [1, 0, 0] -> AH'PxPy
    V2 = np.array([0.5, 1])    #  [0, 1, 0] -> 2*MIPxy
    V3 = np.array([0, 0])      #  [0, 0, 1] -> VIPxy

    two_coordinates = three_coordinates[0]*V1 + three_coordinates[1]*V2 + three_coordinates[2]*V3

    return two_coordinates


def plot_triangle_lines(show=True):
    color_down = 'blue'
    color_left = 'red'
    color_right = 'green'

    A = np.array([0, 0])
    B = np.array([1, 0])
    C = np.array([0.5, 1])

    mpl.rcParams['mathtext.fontset'] = 'cm'
    mpl.rcParams['font.family'] = 'serif'
    
    plt.figure()
    
    triangle_x = [A[0], B[0], C[0], A[0]]
    triangle_y = [A[1], B[1], C[1], A[1]]
    plt.plot(triangle_x, triangle_y, 'k-', linewidth=1.5)

    plt.plot([A[0], B[0]], [A[1], B[1]], color=color_down, linewidth=2)
    draw_parallel_lines_along_direction(A, B, C, num_lines=8, color=color_down)
    plt.plot([A[0], C[0]], [A[1], C[1]], color=color_left, linewidth=2)
    draw_parallel_lines_along_direction(A, C, B, num_lines=8, color=color_left)
    plt.plot([B[0], C[0]], [B[1], C[1]], color=color_right, linewidth=2)
    draw_parallel_lines_along_direction(B, C, A, num_lines=8, color=color_right)

    ## Down line
    plt.text(0.5, -0.05, r"$\Delta H'_{P_{X} \cdot P_{Y}}$", ha='center', va='center', fontsize=15)
    plt.text(0.05, -0.05, '0', ha='center', va='center', fontsize=10, rotation=0)
    plt.text(1-0.05, -0.05, '1', ha='center', va='center', fontsize=10, rotation=0)

    ## Left line
    plt.text(0.15, 0.5, r"$VI'_{P_{XY}}$", ha='center', va='center', fontsize=15, rotation=65)
    plt.text(-0.05, 0.02, '1', ha='center', va='center', fontsize=10, rotation=65)
    plt.text(0.5-0.05, 1-0.02, '0', ha='center', va='center', fontsize=10, rotation=65)

    ## Right line
    plt.text(1-0.15, 0.5, r"$2 \cdot MI'_{P_{XY}}$", ha='center', va='center', fontsize=15, rotation=-65)
    plt.text(1+0.05, 0.02, '0', ha='center', va='center', fontsize=10, rotation=-65)
    plt.text(0.5+0.05, 1-0.02, '1', ha='center', va='center', fontsize=10, rotation=-65)
    plt.axis('off') 

    plt.title('Entropy triangle')
    plt.axis('equal')
    plt.grid(False)
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)

    if show == True:
        plt.show()

def interpolate(p1, p2, t):
    return (1 - t) * np.array(p1) + t * np.array(p2)

def draw_parallel_lines_along_direction(start_vertex1, start_vertex2, opp_vertex, num_lines, color):
    for t in np.linspace(0, 1, num_lines):
        p1 = interpolate(start_vertex1, opp_vertex, t)
        p2 = interpolate(start_vertex2, opp_vertex, t)
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], linestyle='--', color=color, linewidth=1)

def plot_little_cm(conf_matrix, cmap):
    plt.figure(figsize=(3, 3))
    plt.imshow(conf_matrix, cmap=cmap, interpolation='nearest')
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.show()

#################### Plot dark coordinates ####################

def plot_double_coordinates(metrics, color, size):

    coord_x = convert_coordinates(metrics['x'])
    coord_y = convert_coordinates(metrics['y'])

    plot_dark_triangle_lines(show=False)
    plt.scatter(coord_x[0], coord_x[1], color=color, s=size, marker='x')
    plt.scatter(coord_y[0], coord_y[1], color=color, s=size, marker='o')
    plt.show()

def plot_dark_triangle_lines(show=True, title='Entropy triangle'):

    color_down = 'gray'
    color_left = 'gray'
    color_right = 'gray'

    # Vértices del triángulo
    A = np.array([0, 0])
    B = np.array([1, 0])
    C = np.array([0.5, 1])

    mpl.rcParams['mathtext.fontset'] = 'cm'
    mpl.rcParams['font.family'] = 'serif'

    plt.figure()

    triangle_x = [A[0], B[0], C[0], A[0]]
    triangle_y = [A[1], B[1], C[1], A[1]]
    plt.plot(triangle_x, triangle_y, 'k-', linewidth=1.5)

    plt.plot([A[0], B[0]], [A[1], B[1]], color=color_down, linewidth=2)
    draw_parallel_lines_along_direction(A, B, C, num_lines=8, color=color_down)
    plt.plot([A[0], C[0]], [A[1], C[1]], color=color_left, linewidth=2)
    draw_parallel_lines_along_direction(A, C, B, num_lines=8, color=color_left)
    plt.plot([B[0], C[0]], [B[1], C[1]], color=color_right, linewidth=2)
    draw_parallel_lines_along_direction(B, C, A, num_lines=8, color=color_right)

    ## Down line
    plt.text(0.5, -0.05, r"$\Delta H'_{P_{X} \cdot P_{Y}}$", ha='center', va='center', fontsize=15)
    plt.text(0.05, -0.05, '0', ha='center', va='center', fontsize=10, rotation=0)
    plt.text(1-0.05, -0.05, '1', ha='center', va='center', fontsize=10, rotation=0)

    ## Left line
    plt.text(0.15, 0.5, r"$VI'_{P_{XY}}$", ha='center', va='center', fontsize=15, rotation=65)
    plt.text(-0.05, 0.02, '1', ha='center', va='center', fontsize=10, rotation=65)
    plt.text(0.5-0.05, 1-0.02, '0', ha='center', va='center', fontsize=10, rotation=65)

    ## Right line
    plt.text(1-0.15, 0.5, r"$2 \cdot MI'_{P_{XY}}$", ha='center', va='center', fontsize=15, rotation=-65)
    plt.text(1+0.05, 0.02, '0', ha='center', va='center', fontsize=10, rotation=-65)
    plt.text(0.5+0.05, 1-0.02, '1', ha='center', va='center', fontsize=10, rotation=-65)
    plt.axis('off') 
    
    plt.title(f'{title}')
    plt.axis('equal')
    plt.grid(False)
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)

    if show == True:
        plt.show()


############################ Other plots ############################

def plot_labels_histogram(labels_path, fold=0, colors=None):
    if colors is None:
        colors = ['skyblue', 'coral', 'darkseagreen', 'dimgray']

    dt = pd.read_csv(f"{labels_path}/unbalanced_reduced_train_partition.csv")
    dt_train = dt[dt['fold'] != fold]
    dt_val = dt[dt['fold'] == fold]
    dt_test1 = pd.read_csv(f"{labels_path}/test1_opposite_distribution.csv")
    dt_test2 = pd.read_csv(f"{labels_path}/test2_uniform_distribution.csv")

    order = ['airport', 'bus', 'metro', 'metro_station', 'park', 'public_square', 
             'shopping_mall', 'street_pedestrian', 'street_traffic', 'tram']

    train_counts = dt_train['scene_label'].value_counts().reindex(order, fill_value=0)
    val_counts = dt_val['scene_label'].value_counts().reindex(order, fill_value=0)
    test1_counts = dt_test1['scene_label'].value_counts().reindex(order, fill_value=0)
    test2_counts = dt_test2['scene_label'].value_counts().reindex(order, fill_value=0)

    fig, axes = plt.subplots(1, 4, figsize=(20, 3)) 
    counts_list = [train_counts, val_counts, test1_counts, test2_counts]
    titles = ['Train', 'Validation', 'Test1', 'Test2']

    for i, ax in enumerate(axes):
        counts = counts_list[i]
        color = colors[i]
        counts.plot(kind='bar', ax=ax, color=color, edgecolor='black')
        ax.set_title(titles[i], fontsize=14)
        ax.set_xticklabels([]) 
        ax.grid(axis='y', linestyle='--', alpha=0.7) 
        ax.set_xlabel('')
       
    plt.tight_layout()
    plt.show()
