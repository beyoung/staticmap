import unittest

from staticmap import IconMarker, lat_to_y, lon_to_x, x_to_lon, y_to_lat, AssetNotExist

IconMarkerPATH = './samples/marker.png'
IconMarkerURL = 'https://raw.githubusercontent.com/komoot/staticmap/master/samples/marker.png'


class LonLatConversionTest(unittest.TestCase):
    def testLon(self):
        for lon in range(-180, 180, 20):
            for zoom in range(0, 10):
                x = lon_to_x(lon, zoom)
                l = x_to_lon(x, zoom)
                self.assertAlmostEqual(lon, l, places=5)

    def testLat(self):
        for lat in range(-89, 89, 2):
            for zoom in range(0, 10):
                y = lat_to_y(lat, zoom)
                l = y_to_lat(y, zoom)
                self.assertAlmostEqual(lat, l, places=5)

    def test_icon_marker_with_file(self):
        flag = False
        try:
            IconMarker((0, 0), IconMarkerPATH, 0, 0)
            flag = True
        except FileNotFoundError:
            pass

        self.assertTrue(flag)

    def test_icon_marker_with_url(self):
        flag = False
        try:
            IconMarker((0, 0), IconMarkerURL, 0, 0)
            flag = True
        except AssetNotExist:
            pass

        self.assertTrue(flag)


if __name__ == '__main__':
    unittest.main()
