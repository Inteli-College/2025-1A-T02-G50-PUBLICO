# Benchmark do Projeto

**1. Critérios de comparação:**

Projetos analisados foram:

- [Sign-Language-Detection (CNN)](https://github.com/SomyanshAvasthi/Sign-Language-Detection-using-CNN-Architecture.git);
- [Sign Language Interpreter (Deep Learning)](https://github.com/harshbg/Sign-Language-Interpreter-using-Deep-Learning.git);
- [ASL ↔ English Translation](https://github.com/kevinjosethomas/sign-language-processing.git)
- [Redes Neurais Convolucionais - LIBRAS](https://github.com/lucaaslb/cnn-libras.git)
- [Leitor-de-Libras](https://github.com/andersonprax/Leitor-de-Libras.git)
- [RAS-Libras](https://github.com/lucas-serrano/Projeto-LibRAS.git)

Para analisar as soluções, utilizou-se os seguintes critérios:

1. Tecnologia utilizada: Como a tradução é feita (Visão Computacional, IA, Sensores, etc.)?
2. Precisão da tradução: Qual a qualidade do reconhecimento dos sinais?
3. Tempo de Resposta: A solução funciona em tempo real?
4. Acessibilidade e Custo: Se é gratuito, acessível ou exige hardware especial?
5. Abrangência Linguística: Suporta apenas gestos básicos ou expressões complexas?
6. Diferenciais: Pontos fortes do projeto?

---

**2. Análise Comparativa:**

### Tabela Comparativa de Projetos de Tradução de Libras com Visão Computacional

| Critério                     | Sign-Language-Detection (CNN) | Sign Language Interpreter (Deep Learning) | ASL ↔ English Translation | Redes Neurais Convolucionais - LIBRAS | Leitor-de-Libras | RAS-Libras |
|------------------------------|-------------------------------|-------------------------------------------|---------------------------|---------------------------------------|------------------|------------|
| **Tecnologia**               | CNN + Kaggle dataset          | TensorFlow + Keras + OpenCV               | MediaPipe + PointNet + ThreeJS | CNN + OpenCV                          | TensorFlow + Teachable Machine + MediaPipe | TensorFlow + OpenCV + PyQt5 |
| **Precisão**                 | Alta (99%)                    | Boa (95%)                                 | Variável (CNNs: 95% para gestos estáticos; RNNs: 85-90% para frases; Transformers: 80-95% para contextos complexos) | Alta (depende do dataset)             | Boa (depende do dataset) | Boa (depende do dataset) |
| **Tempo de Resposta**        | Em tempo real                 | Em tempo real                             | Moderado (gestos simples: <1s; gestos dinâmicos: 1-3s; gestos complexos: 3-5s+) | Em tempo real                         | Em tempo real     | Em tempo real |
| **Acessibilidade e Custo**   | Gratuito, código aberto       | Gratuito, código aberto                   | Gratuito, hardware potente | Gratuito, código aberto               | Gratuito, código aberto | Gratuito, código aberto |
| **Abrangência Linguística**  | Gestos básicos do ISL         | 44 caracteres do ASL                      | ASL com expressões faciais | Alfabeto em Libras                    | Números em Libras | Alfabeto em Libras |
| **Diferenciais**             | Alta precisão em gestos estáticos | Reconhecimento em tempo real           | Tradução ASL ↔ inglês     | Foco no alfabeto em Libras            | Integração com robótica | Aprendizado interativo de Libras |

---
**3. Pontos dos Projetos:**

-  **Sign-Language-Detection (CNN):** Altíssima precisão no reconhecimento de gestos estáticos da Indian Sign Language, usando um grande dataset do Kaggle. 
- **Sign Language Interpreter (Deep Learning):** Boa acurácia para ASL, funciona em tempo real e usa OpenCV para processar gestos via webcam.
- **ASL ↔ English Translation:** Vai além da simples detecção de gestos e traduz ASL para inglês e vice-versa, respeitando aspectos linguísticos e culturais da língua de sinais.
- **Redes Neurais Convolucionais - LIBRAS:** Utiliza CNNs (Redes Neurais Convolucionais) e OpenCV para reconhecer gestos do alfabeto em Libras. Tem alta precisão no reconhecimento do alfabeto em Libras, com foco em gestos estáticos e código aberto.
- **Leitor-de-Libras:** Utiliza TensorFlow, Teachable Machine e MediaPipe para reconhecer gestos de números em Libras com uma integração com robótica para aplicações em automação.
- **RAS-Libras:** Utiliza TensorFlow, OpenCV e PyQt5 para ensinar e corrigir gestos do alfabeto em Libras. É uma ferramenta de aprendizado interativo de Libras, com correção instantânea de gestos e foco em aplicações educacionais.