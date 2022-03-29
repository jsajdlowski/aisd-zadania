from findBiggestRectangle import findBiggestRectangle
from improvedFindBiggestRectangle import improvedFindBiggestRectangle


def test_findBiggestRectangle() -> None:
    assert findBiggestRectangle([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 0

    assert findBiggestRectangle([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
                                1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 25

    assert findBiggestRectangle([]) == 0

    assert findBiggestRectangle(
        [[1, 0, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1]]) == 12

    assert findBiggestRectangle(
        [[1, 0, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1]]) == 6


def test_improvedFindBiggestRectangle() -> None:
    assert improvedFindBiggestRectangle([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 0

    assert improvedFindBiggestRectangle([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
        1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 25

    assert improvedFindBiggestRectangle([]) == 0

    assert improvedFindBiggestRectangle(
        [[1, 0, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1]]) == 12

    assert improvedFindBiggestRectangle(
        [[1, 0, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1]]) == 6
