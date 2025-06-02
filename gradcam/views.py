from django.shortcuts import render
from django.http import HttpResponse
import os
import numpy as np
import io
import tensorflow as tf
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import cv2
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image
import matplotlib.cm as cm

# Load trained CNN model
model_path = "./ai_models/densenetpneumogradcammodel.h5"
model = tf.keras.models.load_model(model_path, compile=False)

# Define class names
class_names = ["Normal","Pneumonia"]

# Function to preprocess the image
def preprocess_image(img_path, img_size=(224, 224)):
    img = image.load_img(img_path, target_size=img_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize
    return img_array, img

# Function to generate Grad-CAM heatmap
def generate_gradcam(model, img_array, class_index, last_conv_layer_name):
    """
    Generate a Grad-CAM heatmap for the given image and class index.
    """
    # Create a gradient model that outputs the last conv layer and the predictions
    grad_model = Model(
        inputs=model.input,
        outputs=[model.get_layer(last_conv_layer_name).output, model.output]
    )

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        
        # Handle binary classification (sigmoid output)
        if predictions.shape[1] == 1:  # Binary classification
            loss = predictions[:, 0] if class_index == 1 else 1 - predictions[:, 0]
        else:  # Multi-class classification
            loss = predictions[:, class_index]

    # Compute gradients of the loss w.r.t. the conv outputs
    grads = tape.gradient(loss, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))  # Global average pooling
    conv_outputs = conv_outputs[0]  # Remove batch dimension

    # Weight the conv outputs by the gradients
    heatmap = np.mean(conv_outputs * pooled_grads, axis=-1)
    heatmap = np.maximum(heatmap, 0)  # Remove negative values
    heatmap /= np.max(heatmap)  # Normalize to [0, 1]

    return heatmap
# Function to overlay heatmap on the original image
def overlay_heatmap(heatmap, original_img, alpha=0.5):
    """
    Overlay the heatmap on the original image.
    """
    # Resize heatmap to match the original image size
    heatmap = cv2.resize(heatmap, (original_img.size[0], original_img.size[1]))
    heatmap_colored = cm.jet(heatmap)[:, :, :3]  # Convert to colormap
    heatmap_colored = np.uint8(255 * heatmap_colored)

    # Ensure grayscale images are converted to RGB before overlaying
    if len(np.array(original_img).shape) == 2:
        original_img = cv2.cvtColor(np.array(original_img), cv2.COLOR_GRAY2RGB)

    # Blend the heatmap with the original image
    overlayed_img = cv2.addWeighted(np.array(original_img), alpha, heatmap_colored, 0.4, 0)
    return overlayed_img


image_path = None

def receiveimage(image_pathloc):
    global image_path
    image_path = image_pathloc
    print('Image received:', image_path)

# Django View for Grad-CAM
def gradcam_image(request):
    print("Grad-CAM function is being called successfully")
    
    # Ensure an image is set
    if image_path is None:
        return HttpResponse("No image provided.", status=400)

    last_conv_layer_name = "conv5_block3_2_conv"  # Adjust based on your model architecture
    
     # Preprocess the image
    img_array, original_img = preprocess_image(image_path)

    # Get model predictions
    predictions = model.predict(img_array)[0]  # Shape: (1,)
    
    # Handle binary classification (sigmoid output)
    if predictions.shape[0] == 1:  # Binary classification
        predicted_prob = predictions[0]  # Single probability value
        predicted_class_index = 1 if predicted_prob >= 0.5 else 0
        confidence = predicted_prob * 100 if predicted_class_index == 1 else (1 - predicted_prob) * 100
    else:  # Multi-class classification
        predicted_class_index = np.argmax(predictions)
        confidence = predictions[predicted_class_index] * 100

    predicted_class_name = class_names[predicted_class_index]

    # Generate Grad-CAM heatmap
    heatmap = generate_gradcam(model, img_array, predicted_class_index, last_conv_layer_name)
    overlayed_img = overlay_heatmap(heatmap, original_img)

    # Display results
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # Original Image
    axes[0].imshow(original_img, cmap="gray")
    axes[0].set_title("Original Image")
    axes[0].axis("off")

    # Heatmap with Color Legend
    img = axes[1].imshow(heatmap, cmap="jet", alpha=0.8)
    axes[1].set_title("Grad-CAM Heatmap")
    axes[1].axis("off")
    
    # Add colorbar to indicate activation intensity
    cbar = fig.colorbar(img, ax=axes[1], fraction=0.046, pad=0.04)
    cbar.set_label("Activation Intensity", fontsize=12)
    cbar.ax.yaxis.set_tick_params(labelsize=10)

    # Overlayed Image
    axes[2].imshow(overlayed_img)
    axes[2].set_title(f"Prediction: {predicted_class_name}\nConfidence: {confidence:.2f}%")
    axes[2].axis("off")

    # Add explanation of color meanings
    fig.text(0.5, -0.05, 
             "🔴 Red: High Activation (Most Important)  |  🟡 Yellow: Moderate Activation  |  🟢 Green: Low Activation  |  🔵 Blue: No Activation",
             ha="center", fontsize=12, color="black")

    # Add activation intensity range (color legend)
    fig.text(0.5, -0.12, 
             "Activation Intensity Range: 0 (Blue) to 1 (Red)",
             ha="center", fontsize=10, color="black")

    # Save plot to in-memory buffer
    buf = io.BytesIO()
    
     # Save plot as a file on the server as well
    
    
    plt.savefig(buf, format="png")
    
    # plt.savefig(save_path, format="png")
    
    plt.close(fig)
    buf.seek(0)

    return HttpResponse(buf.getvalue(), content_type="image/png")

# View to Render the HTML Page
def gradcam_page(request):
    return render(request, "generategradcam.html")