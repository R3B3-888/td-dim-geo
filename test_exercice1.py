from exercice1 import Lambert93ToWgs84Convertor
import pytest
import pandas as pd
import random


def test_lambert93_to_wgs84_convertor():
    convertor = Lambert93ToWgs84Convertor(
        df=pd.DataFrame(
            data={
                "x": [700000.0, 800000.0],
                "y": [6600000.0, 7600000.0],
                "z": [100.0, 200.0],
            }
        ),
        delta=10,
    )
    converted_coords = convertor.convert()
    expected_coords = [
        (3.0000000000000004, 46.499999999999986, 110.0),
        (4.561673860392856, 55.45063458704315, 210.0),
    ]
    assert pytest.approx(converted_coords) == expected_coords


def test_large_dataset():
    convertor = Lambert93ToWgs84Convertor(
        df=(
            pd.DataFrame(
                data={
                    "x": [
                        random.uniform(600000, 1200000) for _ in range(100000)
                    ],
                    "y": [
                        random.uniform(6050000, 7150000) for _ in range(100000)
                    ],
                    "z": [random.uniform(0, 500) for _ in range(100000)],
                }
            )
        ),
        delta=10,
    )
    converted_coords = convertor.convert()


def test_invalid_data_handling():
    convertor = Lambert93ToWgs84Convertor(
        df=(
            pd.DataFrame(
                data={
                    "x": [700000, None, "invalid"],
                    "y": [6600000.0, 7600000, 7600000],
                    "z": [100, 200, "text"],
                }
            )
        ),
        delta=10,
    )
    with pytest.raises(TypeError):
        converted_coords = convertor.convert()


def test_precision_and_accuracy():
    df_precise = pd.DataFrame(
        data={
            "x": [399242.50670129404, 399246.5985360484, 399255.0372293502],
            "y": [6412023.861878326, 6412025.256650116, 6412051.010513036],
            "z": [128.67240350277112, 128.67240350277112, 128.42240350277112],
        }
    )
    convertor = Lambert93ToWgs84Convertor(df=df_precise)
    assert convertor.convert()
