import unittest
from task08 import Point2D, Rectangle, Square, Circle, Shape2DCollection


class TestTask08(unittest.TestCase):

    def test_point_in_rectangle(self):
        point1 = Point2D(1, 5)
        rec1 = Rectangle(Point2D(1, 1), 2, 5)
        self.assertIn(point1, rec1)

    def test_point_not_in_rectangle(self):
        point1 = Point2D(5, 5)
        rec1 = Rectangle(Point2D(1, 1), 2, 5)
        self.assertFalse(point1 in rec1)

    def test_rectangle_area(self):
        rec1 = Rectangle(Point2D(1, 1), 2, 5)
        self.assertEqual(rec1.area, 10)

    def test_point_in_square(self):
        point1 = Point2D(1, 2)
        square1 = Square(Point2D(1, 1), 2)
        self.assertIn(point1, square1)

    def test_point_not_in_square(self):
        point1 = Point2D(4, 2)
        square1 = Square(Point2D(1, 1), 2)
        self.assertFalse(point1 in square1)

    def test_square_area(self):
        square1 = Square(Point2D(1, 1), 2)
        self.assertEqual(square1.area, 4)

    def test_point_in_circle(self):
        point1 = Point2D(1, 2)
        square1 = Square(Point2D(1, 1), 2)
        self.assertIn(point1, square1)

    def test_point_not_in_circle(self):
        point1 = Point2D(4, 2)
        square1 = Square(Point2D(1, 1), 2)
        self.assertFalse(point1 in square1)

    def test_square_circle(self):
        circle1 = Circle(Point2D(1, 1), 2)
        self.assertEqual(circle1.area, 12.566370614359172)

    def test_point_in_collection(self):
        point1 = Point2D(2, 5)
        rec1 = Rectangle(Point2D(1, 1), 2, 5)
        square1 = Square(Point2D(1, 1), 2)
        circle1 = Circle(Point2D(1, 1), 2)
        collection = Shape2DCollection()
        collection.add_shape(square1)
        collection.add_shape(rec1)
        collection.add_shape(circle1)
        self.assertIn(point1, collection)

    def test_point_not_in_collection(self):
        point1 = Point2D(10, 5)
        rec1 = Rectangle(Point2D(1, 1), 2, 5)
        square1 = Square(Point2D(1, 1), 2)
        circle1 = Circle(Point2D(1, 1), 2)
        collection = Shape2DCollection()
        collection.add_shape(square1)
        collection.add_shape(rec1)
        collection.add_shape(circle1)
        self.assertFalse(point1 in collection)

    def test_square_collection(self):
        rec1 = Rectangle(Point2D(1, 1), 2, 5)
        square1 = Square(Point2D(1, 1), 2)
        circle1 = Circle(Point2D(1, 1), 2)
        collection = Shape2DCollection()
        collection.add_shape(square1)
        collection.add_shape(rec1)
        collection.add_shape(circle1)
        self.assertEqual(collection.area, 26.566370614359172)


if __name__ == '__main__':
    unittest.main()
