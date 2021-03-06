# -*- coding: utf-8 -*-
import pygmsh

from helpers import compute_volume


def test():
    geom = pygmsh.built_in.Geometry()

    xmin = geom.define_constant("xmin", 0.0, 0.0, 1.0)
    xmax = geom.define_constant("xmax", 1.0, 0.0, 1.0)
    ymin = geom.define_constant("ymin", 0.0, 0.0, 1.0)
    ymax = geom.define_constant("ymax", 1.0, 0.0, 1.0)
    geom.add_rectangle(xmin, xmax, ymin, ymax, 0.0, 0.1)

    ref = 1.0
    points, cells, _, _, _ = pygmsh.generate_mesh(geom, mesh_file_type="vtk")
    assert abs(compute_volume(points, cells) - ref) < 1.0e-2 * ref
    return points, cells


if __name__ == "__main__":
    import meshio

    meshio.write_points_cells("defined_constant_rectangle.vtu", *test())
