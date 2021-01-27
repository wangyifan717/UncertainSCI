import unittest

import numpy as np

from UncertainSCI import indexing


class IndexingTestCase(unittest.TestCase):
    """
    Basic testing for polynomial indexing.
    """

    def setUp(self):
        self.longMessage = True

    def test_margins(self):
        """ Generating margins of index sets. """

        dim = 2
        order = 3

        # Total degree set
        indset = indexing.TotalDegreeSet(dim=dim, order=order)
        margin = np.lexsort(indset.get_margin(), axis=0)
        rmargin = np.lexsort(indset.get_reduced_margin(), axis=0)

        exact_margin = np.array([[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]])
        exact_margin = np.lexsort(exact_margin, axis=0)
        exact_rmargin = np.array([[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]])
        exact_rmargin = np.lexsort(exact_rmargin, axis=0)

        delta = 1e-12
        err1 = np.linalg.norm(exact_margin - margin)
        err2 = np.linalg.norm(exact_rmargin - rmargin)
        err = max(err1, err2)

        self.assertAlmostEqual(err, 0, delta=delta)

        # Hyperbolic cross set
        order = 3

        indset = indexing.TotalDegreeSet(dim=dim, order=order)
        margin = np.lexsort(indset.get_margin(), axis=0)
        rmargin = np.lexsort(indset.get_reduced_margin(), axis=0)

        exact_margin = np.array([[0, 5], [1, 4], [1, 3], [2, 2], [3, 1],
                                 [4, 1], [5, 0]])
        exact_margin = np.lexsort(exact_margin, axis=0)
        exact_rmargin = np.array([[0, 5], [1, 3], [2, 2], [3, 1], [5, 0]])
        exact_rmargin = np.lexsort(exact_rmargin, axis=0)

        delta = 1e-12
        err1 = np.linalg.norm(exact_margin - margin)
        err2 = np.linalg.norm(exact_rmargin - rmargin)
        err = max(err1, err2)

        self.assertAlmostEqual(err, 0, delta=delta)
