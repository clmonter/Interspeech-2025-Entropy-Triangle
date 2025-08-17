import os
from information_theory import *
from plot_triangle import *
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.patches as mpatches

def compute_metrics(cm_path, loss_type, fold, group):

    epochs = len(os.listdir(f"{cm_path}/{loss_type}/fold_{fold}/{group}"))

    all_x_points = []
    all_y_points = []

    for epoch in range(epochs):

        cm_epoch = np.array(pd.read_csv(f"{cm_path}/{loss_type}/fold_{fold}/{group}/cm_epoch_{epoch}.csv"))

        metrics_epoch = calculate_everything(cm_epoch, normalize=True)

        two_coordinates_x = convert_coordinates(metrics_epoch['x'])
        two_coordinates_y = convert_coordinates(metrics_epoch['y'])

        all_x_points.append(two_coordinates_x)
        all_y_points.append(two_coordinates_y)

    all_x_points_array = np.vstack(all_x_points) 
    all_y_points_array = np.vstack(all_y_points) 

    return all_x_points_array, all_y_points_array

def plot_many_coordinates(all_x_points_array, all_y_points_array, cmap_name, size, title, step=1):

    total_epochs = len(all_x_points_array)
    cmap = plt.get_cmap(cmap_name)

    selected_indices = np.arange(0, total_epochs, step)
    x_points = all_x_points_array[selected_indices]
    y_points = all_y_points_array[selected_indices]

    norm = mpl.colors.Normalize(vmin=0, vmax=total_epochs - 1)
    colors = cmap(norm(selected_indices))

    plot_dark_triangle_lines(show=False, title=title)
    plt.scatter(x_points[:, 0], x_points[:, 1], color=colors, s=size, marker='x')
    plt.scatter(y_points[:, 0], y_points[:, 1], color=colors, s=size, marker='o')

    ## Down line
    plt.text(0.5, -0.05, r"$\Delta H'_{P_{X} \cdot P_{Y}}$", ha='center', va='center', fontsize=15)
    plt.text(0.05, -0.05, '0', ha='center', va='center', fontsize=10, rotation=0)
    plt.text(1-0.05, -0.05, '1', ha='center', va='center', fontsize=10, rotation=0)

    ## Left line
    plt.text(0.15, 0.5, r"$VI'_{P_{XY}}$", ha='center', va='center', fontsize=15, rotation=65)
    plt.text(-0.05, 0.02, '1', ha='center', va='center', fontsize=10, rotation=65)
    plt.text(0.5-0.05, 0.9, '0', ha='center', va='center', fontsize=10, rotation=65)

    ## Right line
    plt.text(1-0.15, 0.5, r"$2 \cdot MI'_{P_{XY}}$", ha='center', va='center', fontsize=15, rotation=-65)
    plt.text(1+0.05, 0.02, '0', ha='center', va='center', fontsize=10, rotation=-65)
    plt.text(0.5+0.05, 0.9, '1', ha='center', va='center', fontsize=10, rotation=-65)
    plt.axis('off') 

    plt.axis('equal')
    plt.grid(False)
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)

    # Estética
    plt.axis('equal')
    plt.grid(False)
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 0.95)


    sm = mpl.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    cbar = plt.colorbar(sm)
    cbar.set_ticks(np.arange(0, total_epochs, max(1, total_epochs // 10)))
    cbar.set_ticklabels([str(i) for i in np.arange(0, total_epochs, max(1, total_epochs // 10))])
    cbar.set_label('epochs')

    plt.show()

def plot_different_models(confussion_matrices, colors, names, size=64, title='Entropy Triangle'): 
    
    all_x_points = []
    all_y_points = []

    for i in range(len(confussion_matrices)):

        metrics = calculate_everything(confussion_matrices[i], normalize=True)

        two_coordinates_x = convert_coordinates(metrics['x'])
        two_coordinates_y = convert_coordinates(metrics['y'])

        all_x_points.append(two_coordinates_x)
        all_y_points.append(two_coordinates_y)

    all_x_points_array = np.vstack(all_x_points) 
    all_y_points_array = np.vstack(all_y_points) 

    plot_dark_triangle_lines(show=False, title=title)
    plt.scatter(all_x_points_array[:, 0], all_x_points_array[:, 1], color=colors, s=size, marker='x')
    plt.scatter(all_y_points_array[:, 0], all_y_points_array[:, 1], color=colors, s=size, marker='o')

    ## Down line
    plt.text(0.5, -0.05, r"$\Delta H'_{P_{X} \cdot P_{Y}}$", ha='center', va='center', fontsize=15)
    plt.text(0.05, -0.05, '0', ha='center', va='center', fontsize=10, rotation=0)
    plt.text(1-0.05, -0.05, '1', ha='center', va='center', fontsize=10, rotation=0)

    ## Left line
    plt.text(0.15, 0.5, r"$VI'_{P_{XY}}$", ha='center', va='center', fontsize=15, rotation=65)
    plt.text(-0.05, 0.02, '1', ha='center', va='center', fontsize=10, rotation=65)
    plt.text(0.5-0.05, 0.9, '0', ha='center', va='center', fontsize=10, rotation=65)

    ## Right line
    plt.text(1-0.15, 0.5, r"$2 \cdot MI'_{P_{XY}}$", ha='center', va='center', fontsize=15, rotation=-65)
    plt.text(1+0.05, 0.02, '0', ha='center', va='center', fontsize=10, rotation=-65)
    plt.text(0.5+0.05, 0.9, '1', ha='center', va='center', fontsize=10, rotation=-65)
    plt.axis('off') 

    plt.axis('equal')
    plt.grid(False)
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)

    # Estética
    plt.title(f'{title}')
    plt.axis('equal')
    plt.grid(False)
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 0.95)

    plt.show()