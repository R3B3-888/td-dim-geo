import abc
import pandas as pd
import pyproj

Coord = tuple[float, float, float]
Coords = list[Coord]


class CoordinatesConverter(abc.ABC):
    """
    Abstract class for AtoBConverter
    where A and B are two different coordinates system.
    """

    @abc.abstractmethod
    def convert(self) -> Coords:
        """Converts A coordinates to B coordinates.

        Returns:
            Coord: A list of tuples containing the converted B coordinates.
        """


class Lambert93ToWgs84Convertor(CoordinatesConverter):
    # TODO
    raise NotImplemented
