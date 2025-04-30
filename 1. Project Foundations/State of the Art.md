# State of the Art

The state of the art for this automatic Brazilian Sign Language (Libras) translation project, with a specific focus on deaf youth in Brazilian secondary education, has advanced significantly in recent years. This progress has been driven by developments in computer vision techniques, deep learning, and other scientific methods, as well as projects developed by various researchers. However, despite these advancements, significant challenges remain—particularly in the context of Brazilian education, as well as in terms of accuracy, response time, and the inclusion of cultural and regional nuances. This section reviews the most advanced existing research and solutions, identifying gaps and highlighting how this project aims to contribute to the field.

The real-time Libras translation project for deaf and hearing individuals in Brazilian basic education relies heavily on computer vision techniques to capture and interpret gestures and facial expressions. **Convolutional Neural Networks (CNNs)** have been widely used to recognize static gestures, such as signs representing letters and numbers. These networks are effective at extracting visual features, such as hand shape and movement direction, and have achieved high accuracy rates in gesture recognition tasks. However, Libras is not limited to static gestures; it includes dynamic movements and essential facial expressions for communication. To address these complexities, **Recurrent Neural Networks (RNNs)** and **Transformers** have been employed, as they can capture temporal sequences and translate dynamic gestures in real time.

Additionally, tools such as **MediaPipe** and **OpenCV** are used to detect key points of the hands and face, providing input data for AI models. MediaPipe, in particular, has stood out for its real-time efficiency, enabling gesture and facial expression detection with low latency. These tools are especially useful for projects requiring real-time processing, such as Libras translation.

Several solutions have been developed for automatic sign language translation, both in academic and commercial contexts. Projects such as *Sign Language Detection* (AVASTHI, 2021) and *Sign Language Interpreter using Deep Learning* (GUPTA, 2021) demonstrate the effectiveness of CNNs and RNNs in recognizing static and dynamic gestures. The former achieved accuracy rates above 95% in recognition tasks. However, they still face challenges, such as a lack of support for regional variations and facial expressions, as well as limitations related to user age, size, and signing style—since each individual may have distinct physical characteristics that affect recognition accuracy. Thus, these factors are crucial for precise Libras translation.

In the commercial sphere, apps like **Hand Talk** (HAND TALK, 2024) offer Libras-to-Portuguese translation but have limitations in recognizing dynamic gestures and facial expressions. Moreover, many of these solutions were not designed for the Brazilian educational context, limiting their applicability in classrooms.

It is important to note that, despite advancements, significant gaps remain in the literature and current solutions. One major gap is the lack of support for regional variations of Libras. Given that Libras varies by region, an automatic translation system must recognize and interpret these variations to ensure accuracy. Additionally, many solutions do not account for facial expressions, which are a fundamental part of Libras communication. Another challenge is latency, as many solutions do not operate in real time, limiting their use in contexts requiring quick and efficient communication, such as classrooms and meetings.

Another critical challenge is the lack of focus on the educational context. Most existing solutions are generic and were not specifically developed to meet the needs of deaf students in Brazilian secondary education. This includes the absence of integration with teaching materials and educational platforms, as well as limited access to these technologies in public schools and under-resourced institutions.

Thus, this project seeks to address these gaps by developing an automatic Libras translation system that is accurate, accessible, and culturally sensitive. Unlike many existing solutions, the proposed system is tailored specifically to the Brazilian educational context, with an initial focus on numerals, letters, and later, facial expressions. Furthermore, it will be developed using computer vision techniques (CNNs) and artificial intelligence (RNNs and Transformers), aiming to recognize static and dynamic gestures while integrating facial expressions.

Therefore, this project has the potential to generate significant impacts both technically and socially. From a technical perspective, the development of an automatic Libras translation system that incorporates facial expressions represents a relevant advancement in the field of computer vision and AI applied to social inclusion. From a social standpoint, the system could improve access to education for deaf students, reduce school dropout rates, and promote their inclusion in university entrance exams and, consequently, the job market.

### References (ABNT Format, Alphabetical Order):

AVASTHI, Somyansh. _Sign Language Detection using CNN Architecture_. GitHub, 2021. Disponível em: https://github.com/SomyanshAvasthi/Sign-Language-Detection-using-CNN-Architecture. Acesso em: 29 abr. 2025.

BRADSKI, Gary. OpenCV Library. Open Source Computer Vision Library, 2000. Disponível em: https://opencv.org/. Acesso em: 29 abr. 2025.

GOOGLE. MediaPipe. Google Developers, 2023. Disponível em: https://developers.google.com/mediapipe. Acesso em: 29 abr. 2025.

GUPTA, Harsh. _Sign Language Interpreter using Deep Learning_. GitHub, 2021. Disponível em: https://github.com/harshbg/Sign-Language-Interpreter-using-Deep-Learning. Acesso em: 29 abr. 2025.


HAND TALK. _Aplicativo Hand Talk_. 2024. Disponível em: https://www.handtalk.me/br/. Acesso em: 29 abr. 2025.

