# Theoretical Foundations

The automatic translation project for Brazilian Sign Language (Libras) to Portuguese using computer vision and artificial intelligence (AI) is an interdisciplinary field combining linguistics, computer vision, AI, and above all, social inclusion. These theoretical foundations are essential to support the development of the proposed system, ensuring it is technically viable, culturally sensitive, and socially impactful.

First, it is important to recognize that Libras is a visual-spatial language with its own grammatical structure and unique characteristics that distinguish it from spoken languages (MODOBILINGUE, 2022). Unlike Portuguese (an oral-auditory language), Libras uses manual signs, facial expressions, and body movements to convey meaning. Its grammar includes elements such as hand configuration, articulation points, movement patterns, palm orientation, and non-manual markers (e.g., facial expressions and head movements), which are fundamental to Libras communication and must be considered in developing an automatic translation system (QUADROS; KARNOPP, 2004; HAND TALK, 2024). Additionally, Libras exhibits regional variations, meaning the same sign may have different meanings across Brazil. Initially, the system will recognize basic Libras signs but, through iterative development, will progressively achieve accurate translation of expressions and regional variations, becoming culturally sensitive.

Computer vision — a field of computer science enabling machines to "see" and interpret images/videos — will be used to capture and process manual gestures and facial expressions composing Libras signs. Techniques like filtering, segmentation, and edge detection enhance captured image quality, facilitating sign recognition. **Convolutional Neural Networks (CNNs)** are particularly effective for recognizing visual patterns (e.g., hand shapes and movement directions), making them ideal for static and dynamic gesture recognition essential to automatic Libras translation (CALIMAN, 2024; L, 2019; REZENDE, 2016).

It's worth remembering that Artificial intelligence, especially deep learning, plays a crucial role in sign language recognition and translation. Models like **Recurrent Neural Networks (RNNs)** and **Transformers** excel at capturing temporal sequences (e.g., dynamic gestures involving movement over time). RNNs are particularly useful for processing sequential data (e.g., sign language videos), while Transformers — advanced models—have proven efficient for translation and natural language processing (NLP) tasks (DA, 2025). These models can be trained on large datasets to recognize and translate signs with high accuracy. NLP techniques can then translate captured signs into text or speech, enabling the system to serve hearing individuals unfamiliar with Libras.

As an **assistive technology** — tools helping people with disabilities overcome limitations and participate fully in society — this proposed Libras-to-Portuguese translation system exemplifies technology that can promote accessibility and inclusion, particularly in Brazilian secondary schools. By facilitating communication between deaf and hearing individuals, the system may improve access to essential services beyond education (e.g., healthcare and employment), reducing barriers that limit full societal participation for deaf individuals.

### References (ABNT Format, Alphabetical Order)

CALIMAN, Pedro Ferreira. _Desenvolvimento de um sistema de reconhecimento de sinais do alfabeto manual de Libras utilizando MediaPipe Hands e rede LSTM_. 2024. Trabalho de Conclusão de Curso (Bacharelado em Ciência da Computação) – Faculdade de Ciências, Universidade Estadual Paulista (UNESP), Bauru, 2024. Disponível em: https://repositorio.unesp.br/server/api/core/bitstreams/ff3139f3-4497-4fe4-808b-45abfa1388a0/content. Acesso em: 29 abr. 2025

DA, Luc. _IA na Tradução de Língua de Sinais: Uma Revolução . Meliva.ai, 1 jan. 2025_. Disponível em: https://meliva.ai/artificial-intelligence/ia-traducao-lingua-de-sinais/ . Acesso em: 30 abr. 2025.

HAND TALK. _Os 5 parâmetros da Libras: quais são eles e sua importância_. 2024. Disponível em: https://www.handtalk.me/br/blog/parametros-da-libras/​. Acesso em: 29 abr. 2025.

L, Lucas. _cnn-libras_ . 2019. Disponível em: https://github.com/lucaaslb/cnn-libras.git . Acesso em: abr. 2025.

MODOBILINGUE. _O que é Libras?_ . 12 dez. 2022. Disponível em: https://www.modobilingue.com.br/post/o-que-é-libras . Acesso em: 29 abr. 2025.

QUADROS, Ronice Müller de; KARNOPP, Lodenir Becker. _Língua de sinais brasileira: estudos linguísticos_. Porto Alegre: Artmed, 2004.

REZENDE, Tamires Martins. _Aplicação de técnicas de inteligência computacional para análise da expressão facial em reconhecimento de sinais de Libras_. 2016. Dissertação (Mestrado) – Universidade Federal de Minas Gerais, Belo Horizonte, 2016. Disponível em: https://www.researchgate.net/publication/344904811_Analise_da_expressao_facial_em_reconhecimento_de_sinais_de_Libras​. Acesso em: 29 abr. 2025.






