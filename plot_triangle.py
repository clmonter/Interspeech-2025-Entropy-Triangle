import matplotlib.pyplot as plt
import numpy as np

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


def plot_triangle_lines(show=True):
    color_down = 'blue'
    color_left = 'red'
    color_right = 'green'

    # Vértices del triángulo
    A = np.array([0, 0])
    B = np.array([1, 0])
    C = np.array([0.5, 1])

    plt.figure()

    # Dibujar triángulo
    triangle_x = [A[0], B[0], C[0], A[0]]
    triangle_y = [A[1], B[1], C[1], A[1]]
    plt.plot(triangle_x, triangle_y, 'k-', linewidth=1.5)
    #plt.fill(triangle_x, triangle_y, 'skyblue', alpha=0.5)
    #plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='red')

    # === EJE 1: base AB ===
    plt.plot([A[0], B[0]], [A[1], B[1]], color=color_down, linewidth=2)
    draw_parallel_lines_along_direction(A, B, C, num_lines=8, color=color_down)

    # === EJE 2: lado izquierdo AC ===
    plt.plot([A[0], C[0]], [A[1], C[1]], color=color_left, linewidth=2)
    draw_parallel_lines_along_direction(A, C, B, num_lines=8, color=color_left)

    # === EJE 3: lado derecho BC ===
    plt.plot([B[0], C[0]], [B[1], C[1]], color=color_right, linewidth=2)
    draw_parallel_lines_along_direction(B, C, A, num_lines=8, color=color_right)

    # Estética
    plt.title('Entropy triangle')
    plt.axis('equal')
    plt.grid(False)
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)

    if show == True:
        plt.show()


def interpolate(p1, p2, t):
    """Interpolación lineal entre dos puntos"""
    return (1 - t) * np.array(p1) + t * np.array(p2)

def draw_parallel_lines_along_direction(start_vertex1, start_vertex2, opp_vertex, num_lines, color):
    """
    Dibuja líneas paralelas al eje definido por start_vertex1 y start_vertex2,
    empezando desde interpolaciones entre esos vértices y el vértice opuesto.
    """
    for t in np.linspace(0, 1, num_lines):
        # Punto a lo largo del eje opuesto
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