import os
from information_theory import *
from plot_triangle import *
import pandas as pd
import numpy as np
import matplotlib as mpl

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

def compute_real_metrics(cm_path, loss_type, fold, group):
    ## Metrics in 3D for all epochs
    epochs = len(os.listdir(f"{cm_path}/{loss_type}/fold_{fold}/{group}"))

    all_metrics = []

    for epoch in range(epochs):

        cm_epoch = np.array(pd.read_csv(f"{cm_path}/{loss_type}/fold_{fold}/{group}/cm_epoch_{epoch}.csv"))

        metrics_epoch = calculate_everything(cm_epoch, normalize=True)

        all_metrics.append(metrics_epoch)

    all_metrics = np.vstack(all_metrics) 

    return all_metrics


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

    sm = mpl.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    cbar = plt.colorbar(sm)
    cbar.set_ticks(np.arange(0, total_epochs, max(1, total_epochs // 10)))
    cbar.set_ticklabels([str(i) for i in np.arange(0, total_epochs, max(1, total_epochs // 10))])
    cbar.set_label('epochs')

    plt.show()
