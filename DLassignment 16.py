#!/usr/bin/env python
# coding: utf-8

# sigmoid
# tanh
# ReLU
# ELU
# LeakyReLU
# swish
# 

# Sigmoid: Squashes values between 0 and 1, useful for binary classification.
# Tanh: Squashes values between -1 and 1, commonly used in neural networks.
# ReLU: Returns 0 for negative values and the input value for positive values, mitigates vanishing gradient.
# ELU: Similar to ReLU for positive values, handles negative values smoothly.
# LeakyReLU: Similar to ReLU but introduces a small slope for negative values, prevents dead ReLU units.
# Swish: Smooth interpolation between linearity and non-linearity, potentially improves performance.

# 2. What happens when you increase or decrease the optimizer learning rate?
# 

# Increasing the learning rate can lead to faster convergence but risks instability. It allows the model to learn quickly, but very high values can cause oscillations and overshooting.
# 
# Decreasing the learning rate improves stability but slows down convergence. It helps the model fine-tune parameters precisely, but very low values may result in slow convergence or getting stuck in suboptimal solutions.

# 3. What happens when you increase the number of internal hidden neurons?
# 

# Pros:
# Increases model capacity and representation power.
# Allows the network to learn more complex patterns and relationships.
# 
# 
# Cons:
# May lead to overfitting, especially with limited training data.
# Slower training due to increased computational complexity.
# Risk of vanishing or exploding gradients.
# Requires more computational resources and memory.
# 

# 4. What happens when you increase the size of batch computation?
# 

# increasing the batch size can accelerate training and lead to smoother convergence. However, it may come at the cost of reduced generalization performance and increased memory requirements. Experimentation and evaluation on validation or test data are crucial to determine the optimal batch size for a given task.

# 5. Why we adopt regularization to avoid overfitting?
# 

#  regularization is adopted to avoid overfitting by introducing constraints on the model's parameters during training. It helps control complexity, promotes generalization, and aligns with the principle of favoring simpler explanations or models.

# 6. What are loss and cost functions in deep learning?
# 

# The loss function measures the error between the predicted output and the true target values for an individual training .

# 7. What do ou mean by underfitting in neural networks?

# underfitting in neural networks occurs when the model is too simple and fails to capture the patterns in the training data. It results in high training error and indicates that the model is not adequately learning from the data.

# 8. Why we use Dropout in Neural Networks?
# 

# dropout is a simple and effective technique to reduce overfitting by introducing noise and promoting robust learning in neural networks.

# In[ ]:




