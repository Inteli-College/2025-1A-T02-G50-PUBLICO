# Project Benchmark

**1. Comparison Criteria:**

The analyzed projects were:  

- [Sign-Language-Detection (CNN)](https://github.com/SomyanshAvasthi/Sign-Language-Detection-using-CNN-Architecture.git);  
- [Sign Language Interpreter (Deep Learning)](https://github.com/harshbg/Sign-Language-Interpreter-using-Deep-Learning.git);  
- [ASL ↔ English Translation](https://github.com/kevinjosethomas/sign-language-processing.git)  
- [Convolutional Neural Networks - LIBRAS](https://github.com/lucaaslb/cnn-libras.git)  
- [Libras Reader](https://github.com/andersonprax/Leitor-de-Libras.git)  
- [RAS-Libras](https://github.com/lucas-serrano/Projeto-LibRAS.git)  

The following criteria were used to evaluate the solutions:  

1. **Technology used**: How is translation performed (Computer Vision, AI, Sensors, etc.)?  
2. **Translation accuracy**: How well does the system recognize signs?  
3. **Response time**: Does the solution work in real time?  
4. **Accessibility and cost**: Is it free, accessible, or does it require specialized hardware?  
5. **Linguistic coverage**: Does it support only basic gestures or complex expressions?  
6. **Key strengths**: What are the project's standout features?  

---

**2. Comparative Analysis:**

### Comparative Table of Libras Translation Projects Using Computer Vision  

| Criterion                     | Sign-Language-Detection (CNN) | Sign Language Interpreter (Deep Learning) | ASL ↔ English Translation | Convolutional Neural Networks - LIBRAS | Libras Reader | RAS-Libras |
|------------------------------|-------------------------------|-------------------------------------------|---------------------------|---------------------------------------|------------------|------------|
| **Technology**               | CNN + Kaggle dataset          | TensorFlow + Keras + OpenCV               | MediaPipe + PointNet + ThreeJS | CNN + OpenCV                          | TensorFlow + Teachable Machine + MediaPipe | TensorFlow + OpenCV + PyQt5 |
| **Accuracy**                 | High (99%)                    | Good (95%)                                | Variable (CNNs: 95% for static gestures; RNNs: 85-90% for sentences; Transformers: 80-95% for complex contexts) | High (dataset-dependent)             | Good (dataset-dependent) | Good (dataset-dependent) |
| **Response Time**            | Real-time                     | Real-time                                 | Moderate (simple gestures: <1s; dynamic gestures: 1-3s; complex gestures: 3-5s+) | Real-time                             | Real-time     | Real-time |
| **Accessibility & Cost**     | Free, open-source             | Free, open-source                         | Free, requires powerful hardware | Free, open-source                     | Free, open-source | Free, open-source |
| **Linguistic Coverage**      | Basic ISL gestures            | 44 ASL characters                         | ASL with facial expressions | Libras alphabet                       | Numbers in Libras | Libras alphabet |
| **Key Strengths**            | High accuracy for static gestures | Real-time recognition                  | ASL ↔ English translation | Focus on Libras alphabet              | Robotics integration | Interactive Libras learning |

---
**3. Project Highlights:**

- **Sign-Language-Detection (CNN):** Exceptionally high accuracy in recognizing static gestures from Indian Sign Language, using a large Kaggle dataset.  
- **Sign Language Interpreter (Deep Learning):** Good accuracy for ASL, works in real time, and uses OpenCV to process gestures via webcam.  
- **ASL ↔ English Translation:** Goes beyond simple gesture detection by translating ASL to English and vice versa, respecting linguistic and cultural aspects of sign language.  
- **Convolutional Neural Networks - LIBRAS:** Uses CNNs and OpenCV to recognize Libras alphabet gestures. Achieves high accuracy in recognizing Libras alphabet signs, focusing on static gestures, and is open-source.  
- **Libras Reader:** Uses TensorFlow, Teachable Machine, and MediaPipe to recognize Libras number gestures, with robotics integration for automation applications.  
- **RAS-Libras:** Uses TensorFlow, OpenCV, and PyQt5 to teach and correct Libras alphabet gestures. It is an interactive learning tool for Libras, providing instant gesture correction and focusing on educational applications.  