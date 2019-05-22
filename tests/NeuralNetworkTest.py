import unittest
import os

from ActivationFunctions import sigmoid, relu
from NeuralNetwork import NeuralNetwork
from ReluLayer import ReluLayer
from SigmoidLayer import SigmoidLayer
from utils.DataLoader import *


class NeuralNetworkTest(unittest.TestCase):
    def __read_test_set(self):
        self.test_features, self.test_classes = load_dataset(os.environ["DATASET_TEST_PATH"],
                                                             (os.environ["DATASET_FEATURES_TEST"],
                                         os.environ["DATASET_CLASSES_TEST"]))

    def __read_train_set(self):
        self.train_features, self.train_classes = load_dataset(os.environ["DATASET_FILE_PATH"],
                                                               (os.environ["DATASET_FEATURES"],
                                          os.environ["DATASET_CLASSES"]))

    def setUp(self):
        self.__read_train_set()
        self.__read_test_set()

    def test_givenDataset_whenPredict_shouldReturnClasses(self):
        hidden = ReluLayer(2, sigmoid)
        out = SigmoidLayer(1, relu)

        layers = [hidden, out]

        nn = NeuralNetwork(layers, 0.09, 1)

        nn.train(self.train_features, self.train_classes)

        predictions = nn.predict(self.train_features)

        self.assertEqual(predictions.shape[1], self.train_features.shape[1])

    def test_givenDataset_whenPredict_shouldMeet70PercAccuracy(self):
        layers = [ReluLayer(20, relu), ReluLayer(7, relu), ReluLayer(5, relu), SigmoidLayer(1, sigmoid)]

        nn = NeuralNetwork(layers, 0.0075, 3000)

        nn.train(self.train_features, self.train_classes)

        predictions = nn.predict(self.train_features)

        prediction_accuracy = 100 - np.mean(np.abs(predictions - self.train_classes)) * 100
        print("Prediction accuracy is {0}%".format(prediction_accuracy))
        self.assertGreaterEqual(prediction_accuracy, 70.0)


if __name__ == '__main__':
    unittest.main()
