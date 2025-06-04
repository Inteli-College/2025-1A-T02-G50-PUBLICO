## Architecture Decision Report for Dynamic Signal Recognition in Libras

The first phase of the research explored the most suitable artificial intelligence and computer vision technologies for this task, particularly considering the need to recognize both static and, more importantly, dynamic signals.

The journey of research into dynamic gestures began with an understanding of two fundamental deep learning architectures: Recurrent Neural Networks (RNNs) and Transformers (A transformer model is a neural network that learns context and, thus, meaning by tracking relationships in sequential data, like the words in this sentence). The main question was whether these architectures would be necessary, given that the project already had a Convolutional Neural Network (CNN) model obtained from GitHub ([https://github.com/lucaaslb/cnn-libras](https://github.com/lucaaslb/cnn-libras)), capable of recognizing static letters from the Libras alphabet.

At this point, it was identified that letters such as Z, H, K, P, Ç, and J in Libras are dynamic signals, meaning their recognition depends on analyzing movement over time rather than just a static hand pose. By its nature, a CNN is excellent at extracting spatial features from static images but does not inherently process the temporal dimension. This led to the conclusion that a CNN alone would not be sufficient for recognizing these dynamic letters.

The research then delved deeper into the capabilities of RNNs (especially their more robust variants, LSTMs and GRUs) and Transformers. Both architectures are specifically designed to handle sequential data, which is the essence of dynamic signal videos (a sequence of frames).

- RNNs/LSTMs/GRUs : These were considered a natural option due to their ability to maintain a "memory state" and learn dependencies in sequences. The idea would be to use a CNN to extract visual features from each frame and then feed these features into an LSTM/GRU to capture movement information.


- Transformers : These were identified as a more modern and powerful alternative, with the advantage of processing sequences in parallel and being exceptional at capturing long-range dependencies through the self-attention mechanism.


| Feature                      | RNN (Recurrent Neural Network)                                                                                  | Transformer                                                                                     |
|------------------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **Processing**               | Sequential (one element at a time, with loops)                                                                   | Parallel (entire sequence at once)                                                              |
| **"Memory"**                 | Recurrent hidden state (passes information step-by-step; may struggle with long-range dependencies)             | Self-Attention Mechanism (directly connects any two elements in the sequence, regardless of distance) |
| **Dependencies**             | Good for short-range; struggles with long-range due to vanishing/exploding gradient problem                      | Excellent for long-range; captures complex and distant relationships in the sequence easily     |
| **Training**                 | Generally slower; hard to parallelize                                                                           | Much faster; highly parallelized                                                               |
| **Common Issues**            | Vanishing/exploding gradient                                                                                     | High computational cost for very long sequences; requires positional encoding to understand order |
| **Typical Applications**     | Machine translation (earlier versions), speech recognition, text generation (smaller models)                    | Machine translation (state-of-the-art), text generation (LLMs like GPT), natural language understanding (BERT) |


## The Importance of Data Preprocessing: The Role of MediaPipe

During the discussion about how RNNs/Transformers could process video data, the question arose about how to efficiently extract crucial information. This is where Google's MediaPipe was introduced.

Initially, there was some uncertainty about whether MediaPipe would be an alternative to CNNs/RNNs/Transformers. However, the conclusion was clear: MediaPipe does not replace these deep learning architectures; it fundamentally complements them.

MediaPipe is a framework optimized for real-time computer vision, offering pre-trained models for detecting and tracking keypoints (landmarks) in structures such as hands, body, and face. For the Libras project, the functionality of MediaPipe Hands (detecting 21 keypoints per hand) proved to be ideal.

The decision was made that MediaPipe would serve as the essential tool for preprocessing video data. Instead of requiring the deep learning model to "learn to see" the hand and extract joints from raw pixels, MediaPipe would handle this task by providing sequences of X, Y, Z coordinates of the joint points. This simplifies the problem for the neural network, allowing it to focus more on learning movement patterns.


## Final Architecture Definition for Dynamic Signals

After analyzing the functionalities of each technology, the final decision for recognizing dynamic letters in Libras (H, K, P, Z, Ç, and J) was a combined approach:

1. MediaPipe : Used as the preprocessing and feature extraction layer. It will transform raw videos into sequences of hand keypoints, which are a compact and robust numerical representation of movement. This is crucial both for creating the training dataset and for real-time inference from a camera.

2. RNN/LSTM : This architecture was selected as the main deep learning model to learn movement patterns from the keypoint sequences generated by MediaPipe. Although Transformers are more advanced, a CNN + LSTM/GRU architecture is a proven, robust solution with a more manageable learning curve for this stage of the project.



NOTE: _Implementation was done only with LSTM, starting with the letter H. Why LSTM and not GRU?_
1. _LSTM was chosen for its ability to capture long-term temporal dependencies, which is suitable for recognizing dynamic gestures like the rotation of the letter H, involving a sequence of 20-30 frames._
2. _GRU is a lighter alternative (with fewer parameters) but less expressive in some cases. Since the dataset (600 sequences, 63 features per frame), according to the third training and third testing, is relatively small and training was fast (~5-20 minutes on CPU), LSTM was sufficient without the need to optimize using GRU._