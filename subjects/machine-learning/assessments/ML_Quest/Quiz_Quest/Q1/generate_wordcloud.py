from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ML keywords for the wordcloud
text = """
machine learning artificial intelligence data science neural networks deep learning
algorithms python tensorflow pytorch scikit-learn pandas numpy matplotlib
supervised unsupervised regression classification clustering computer vision
natural language processing reinforcement learning big data analytics statistics
probability models training testing validation accuracy precision recall f1-score
feature engineering preprocessing normalization standardization cross-validation
gradient descent optimization backpropagation convolutional neural networks
recurrent neural networks transformers bert gpt large language models
computer vision image processing opencv object detection segmentation
time series forecasting anomaly detection recommendation systems
"""

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    colormap='viridis',
    max_words=100,
    random_state=42
).generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Machine Learning Concepts Word Cloud', fontsize=16, pad=20)
plt.savefig('ml_wordcloud.png', dpi=300, bbox_inches='tight')
plt.close()

print("Wordcloud generated as ml_wordcloud.png")