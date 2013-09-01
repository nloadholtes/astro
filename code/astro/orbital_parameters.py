from collections import namedtuple

OrbitalParameters = namedtuple("OrbitalParameters", "semi_major_axis_km, orbital_period, rotation_period, inclination, eccentricity, mass, radius, density, albedo")

TRITON = OrbitalParameters(354.76, 5.876854, "S", 157.345, 0.000016, 214.0, 1353.4, 2050, 0.76)
