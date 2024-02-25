# Haralick Features

## What Are Haralick Features?

Haralick features are a set of calculations derived from the gray-level co-occurrence matrix (GLCM) of an image, a concept introduced by Robert Haralick in 1973. These features are used to quantify various aspects of an image's texture, providing a numerical fingerprint of sorts that captures patterns of intensity in a visual canvas.

## The Essence of GLCM

Imagine you have a grayscale image. The GLCM is a matrix that summarizes how often different combinations of gray levels co-occur in an image or a region of an image at a specific offset. Essentially, it's a way to capture the spatial relationship between pixels at predefined distances and angles.

## The Set

From the GLCM, Haralick proposed several features (often numbered at 14 in foundational literature) that describe the texture of an image. These features capture various properties such as contrast, uniformity, and correlation among pixels. Here are a few of the key features to understand:

1. Contrast

- Relevance: High contrast indicates a significant difference between the brightest and darkest areas, contributing to a perception of sharpness or roughness in texture. This can be pivotal for distinguishing between images with smooth versus pronounced textures.

- Application: Identifying images with dramatic lighting or stark textural differences.

1. Homogeneity

- Relevance: Images with a high degree of homogeneity have subtle contrast variations and a smooth texture. This feature is essential for grouping images that have a uniform appearance or subtle textural patterns.

- Application: Grouping images with smooth surfaces or minimal texture variance.

1. Energy (Angular Second Moment)

- Relevance: Energy quantifies the uniformity of an image's texture. High energy values indicate a consistent texture pattern, useful for identifying images with a cohesive aesthetic.

- Application: Searching for images with a calm, serene quality or a consistent pattern, like wallpapers or backgrounds.

1. Correlation

- Relevance: This measures how a pixel is correlated to its neighbor over the image. High correlation suggests a repetitive, predictable texture pattern. It can help in identifying images with regular patterns versus those with more chaotic, unstructured textures.

- Application: Finding images with regular, geometric patterns or distinguishing between natural and artificial textures.

1. Entropy

- Relevance: Entropy measures the randomness or complexity of the texture. High entropy values are indicative of complex, detailed textures and can be useful for identifying images rich in detail.

- Application: Searching for images that are visually complex or detailed, like cityscapes or densely packed natural scenes.

1. Variance

- Description: Measures the variance from the mean of the GLCM. It reflects the variation in gray-level intensity for the pixels in the image, indicating the spread of pixel intensity values.

- Application: Useful for identifying images with a wide or narrow range of intensities.

1. Sum Average

- Description: Computes the average of the sum of gray-level values for pairs of pixels at the specified offset. It's a measure of the average intensity of an image.

- Application: Can help in gauging the overall brightness of an image.

1. Sum Variance

- Description: Measures the variance of the sum of gray-level values, offering a sense of variability in the intensity sum across the image.

- Application: Useful for distinguishing between images with uniform versus varied brightness levels.

1. Sum Entropy

- Description: Represents the entropy of the sum of gray-level values. It quantifies the randomness in the sum of intensities, providing insight into the complexity of intensity variations.

- Application: Identifies images with complex patterns of intensity sums.

1. Difference Variance

- Description: Another measure of the variance in the image, specifically focusing on the contrast between neighboring pixel values.

- Application: Useful for detecting images with subtle versus pronounced differences between adjacent pixels.

1. Difference Entropy

- Description: Quantifies the randomness in the contrast between neighboring pixels, similar to entropy but focused on differences.

- Application: Helps in identifying textures with varying levels of contrast complexity.

1. Information Measures of Correlation (1 and 2)

- Description: These two features measure the correlation of gray-level values in an image, based on entropy calculations. They provide insight into the textural information's complexity and how it's distributed across the image.

- Application: Useful for analyzing the degree of linear predictability and informational complexity in the texture.

1. Maximal Correlation Coefficient

- Description: Measures the highest correlation between pairs of pixels within the image, indicating the presence of repeating patterns.

- Application: Identifies images with strong, regular patterns versus those with more random, less correlated textures.

## Applying Haralick Features to Aesthetic Grouping

- Mood and Atmosphere: Energy and homogeneity can help group images by their mood (calm vs. dynamic), while contrast can indicate the drama in the scene.

- Texture and Detail: Contrast, correlation, and entropy are key for distinguishing between images based on the presence of fine details or the regularity of patterns.

- Visual Complexity: Entropy can guide users to either embrace or avoid complexity, depending on their aesthetic preference.

## Practical Considerations

In practice, when computing Haralick features for an image, you're not restricted to a single set of parameters. The GLCM can be calculated over various distances and angles, and the Haralick features derived from each of these matrices. However, for simplicity and consistency, many applications choose a standard set of distances and angles, resulting in a fixed number of features per image.

## Understanding Haralick Features and Euclidean Distance

Haralick features, derived from the co-occurrence matrix of an image, encapsulate texture by examining the spatial relationship between pixels. These features include contrast, correlation, energy, and homogeneity, among others, each capturing different aspects of texture. When we compute Haralick features, we obtain a vector where each element represents one of these aspects.

The "distance" between two vectors of Haralick features essentially measures how dissimilar two textures are. By using the Euclidean distance, we quantify the overall difference between the textures represented by these feature vectors. A smaller distance indicates more similar textures, while a larger distance suggests greater dissimilarity.
