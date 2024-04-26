import faiss


class KNN:
    """
    Uses faiss library for nearest neighbour search
    There are two modes L2 and cosine. Cosine can be used for
    matching histograms
    """
    def __init__(self, vec_size: int, mode='cosine', search='exact'):
        if search == 'exact':
            if mode == 'cosine':
                index = faiss.IndexFlatIP(vec_size)
            elif mode == 'L2':
                index = faiss.IndexFlatL2(vec_size)
            else:
                raise NotImplementedError(f'{mode} not implemented yet')
        else:
            raise NotImplementedError(f'{mode} not implemented yet')

        self.index = index

    def fit(self, data):
        self.index.add(data)

    def findKNearest(self, data, k=10):
        D, I = self.index.search(data, k)
        return I
