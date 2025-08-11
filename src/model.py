class DummyModel:
    def train(self, data):
        print("Training model on:", data)

    def predict(self, text):
        return "prediction_for_" + text
