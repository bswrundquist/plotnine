from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from ..doctools import document
from .geom_path import geom_path


@document
class geom_density_2d(geom_path):
    """
    2D density estimate

    This is a 2d version of :class:`~plotnine.geoms.geom_density`.

    {usage}

    Parameters
    ----------
    {common_parameters}

    {aesthetics}
    """
    DEFAULT_PARAMS = {'stat': 'density_2d', 'position': 'identity',
                      'na_rm': False}