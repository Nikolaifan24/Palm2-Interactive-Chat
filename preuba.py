# from skllm.config import SKLLMConfig

# SKLLMConfig.set_google_project("fine-tuning-397318")

# from skllm.models.palm import ZeroShotPaLMClassifier
# from skllm.datasets import get_classification_dataset

# X, y = get_classification_dataset()
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# clf = ZeroShotPaLMClassifier()
# clf.fit(X_train, y_train)
# labels = clf.predict(X_test)

# print(labels)

import tensorflow as tf
from scikit_llm import PaLM2

# Load the PaLM 2 model
model = PaLM2()

# Set the hyperparameters for the fine-tuning
epochs = 10
batch_size = 32
learning_rate = 0.001

# Load the training dataset
dataset = tf.data.experimental.from_tensor_slices((texts, labels))
dataset = dataset.batch(batch_size)

# Fine-tune the model
model.fit(dataset, epochs=epochs, learning_rate=learning_rate)
