import numpy as np

class KNeighborsRegressor():
    def __init__(self, n_neighbors):
        self.n_neighbors = n_neighbors
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = []
        
        for i, test_point in enumerate(X):
            distances = []

            for x, train_point in enumerate(self.X_train):
                distance = abs(train_point[0] - test_point[0])
                distances.append((distance, x))

            for i in range(len(distances) - 1):  
                for j in range(i + 1, len(distances)):  
                    if distances[i][0] > distances[j][0]:
                        distances[i], distances[j] = distances[j], distances[i]

            neighbor_indices = [distances[x][1] for x in range(min(self.n_neighbors, len(distances)))]

            neighbor_values = []
            for index in neighbor_indices:
                neighbor_values.append(self.y_train[index])

            total = 0
            count = 0
            for value in neighbor_values:
                total += value
                count += 1
            mean_prediction = total / count

            predictions.append(mean_prediction)

        return np.array(predictions)
    
if __name__ == "__main__":

    X = np.array([[1], [2], [4]])
    y = np.array([1, 2, 4])

    model = KNeighborsRegressor(n_neighbors=1)
    model.fit(X, y)
    assert (model.predict(X) == np.array([1, 2, 4])).all()

    model = KNeighborsRegressor(n_neighbors=2)
    model.fit(X, y)
    assert (model.predict(X) == np.array([3/2, 3/2, 6/2])).all()

    model = KNeighborsRegressor(n_neighbors=10**9)
    model.fit(X, y)
    assert (model.predict(X) == np.array([7/3, 7/3, 7/3])).all()




