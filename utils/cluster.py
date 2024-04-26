import faiss


class KMEANS:
    """
    Uses FAISS library for KMeans, it will take features,
    cluster them and return the labels.
    It is meant to be used to build the histograms each image's
    descriptors
    """
    def __init__(self, vec_size, num_clusters=500, niter=100) -> None:
        self.kmeans = faiss.Kmeans(vec_size,
                                   num_clusters,
                                   niter=niter,
                                   verbose=True)

    def train(self, data):
        self.kmeans.train(data)

    def search(self, data):
        D, I = self.kmeans.index.search(data, 1)
        return I
