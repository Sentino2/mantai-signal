---
title: "MicroQonv: Reshaping Convolution Tensors for Efficient Microscaling in Training and Inference"
date: 2026-09-23T16:30:48+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2609.28358v1"
ext_id: "arxiv:2609.28358v1"
tags: ["models"]
summary: "Microscaling quantization techniques are increasingly used to represent neural network parameters with 8 bits or fewer while preserving near-full precision accuracy. However, applying these methods efficiently in convolutional layers is not straightforward. A naive approach transfers full-precision weights and activations to processing units and quantizes each tensor twice, resulting in much more "
---

Microscaling quantization techniques are increasingly used to represent neural network parameters with 8 bits or fewer while preserving near-full precision accuracy. However, applying these methods efficiently in convolutional layers is not straightforward. A naive approach transfers full-precision weights and activations to processing units and quantizes each tensor twice, resulting in much more memory movement than expected. Additional overhead comes from the activation tensors, whose sizes grow substantially because of the im2col transformation applied before quantization. We propose MicroQonv, a way to combine microscaling with convolutional layers' forward and backward operations by quantizing each tensor only once and quantizing the activation tensor before applying a modified version of im2col: channel-batch-first im2col. MicroQonv reduces the quantization cost by a factor of $\times2$ for weights and gradients, and by up to $\times9$ for activations, at a negligible accuracy cost. It reduces memory movement and storage by up to $\times7.53$ compared to their full-precision counterparts. This way, MicroQonv reduces microscaling-quantized activation memory movement by $\times3.5$ for state-of-the-art object detection models YOLOV8nano and $\times2.2$ for YOLOV26nano. It also enables 4-bit microscaling in a quantized latent replay strategy for continual learning at the edge, improving accuracy by +5.7% to +11%.

[Read the original at arXiv →](https://arxiv.org/abs/2609.28358v1)
