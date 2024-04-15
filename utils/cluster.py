import faiss


class KMEANS:

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
