# Flood-Level Classification from Road Images

A deep-learning image classification project for recognizing **three road-flooding levels** from visual data:

- **NO FLOODED**
- **LOW FLOODED**
- **HEAVY FLOODED**

The project explores whether image-based AI can provide a simple visual estimate of road flooding severity for transportation awareness and urban monitoring.

> **Full dataset:** [Google Drive](https://drive.google.com/drive/u/0/folders/1oQNM_PhGc3Ffs-Vq5xXcXhytqIEC1Juf)

---

## 1. Project Overview

Flooded roads can disrupt transportation and create safety risks for road users.  
This project develops an image-classification workflow that separates road scenes into three flooding levels based on visible water conditions.

The repository is organized to show the full machine-learning workflow clearly, including:

- dataset inspection,
- preprocessing,
- model training,
- validation,
- confusion-matrix evaluation,
- and prediction on unseen road images.

---

## 2. Dataset

The dataset is organized into three classes:

| Class | Description |
|---|---|
| `NO FLOODED` | Road scenes with no visible flooding |
| `LOW FLOODED` | Road scenes with visible but relatively shallow flooding |
| `HEAVY FLOODED` | Road scenes with severe flooding and substantial water coverage |

### Example images

<p align="center">
  <img width="989" height="594" alt="image" src="https://github.com/user-attachments/assets/8ffaff3e-bb3b-40b7-b7e6-c4f4bf6b6eb5" />

</p>

The **full dataset is stored externally on Google Drive** to keep the GitHub repository lightweight:

**Dataset link:** [Open Google Drive dataset](https://drive.google.com/drive/u/0/folders/1oQNM_PhGc3Ffs-Vq5xXcXhytqIEC1Juf)

> Note: The dataset itself is not duplicated in this repository.

---
---

## 3. Training Behavior

### Accuracy

The training accuracy increases steadily and reaches approximately **95%**, while validation accuracy stabilizes at around **89–90%**.

<p align="center">
  <img width="691" height="470" alt="image" src="https://github.com/user-attachments/assets/5dccc534-0d7d-4cee-9208-1771f7a9e424" />
</p>

### Loss

Both training and validation loss decrease during training.  
The remaining gap between the curves suggests some overfitting, but the validation trend remains stable rather than diverging sharply.

<p align="center">
  <img width="691" height="470" alt="image" src="https://github.com/user-attachments/assets/fd5d03bf-14cd-4900-b3ef-309f564f4498" />
</p>

---

## 4. Evaluation

### Confusion Matrix

<p align="center">
  <img width="606" height="455" alt="image" src="https://github.com/user-attachments/assets/4ecdf671-f558-4b54-af52-ddafdfe1cb48" />
</p>

From the displayed confusion matrix:

- **235** evaluation images in total
- **211** correctly classified images
- overall accuracy computed from the matrix: **89.8%**

### Class-level results

| Class | Correct / Total | Recall |
|---|---:|---:|
| HEAVY FLOODED | 60 / 72 | 83.3% |
| LOW FLOODED | 71 / 82 | 86.6% |
| NO FLOODED | 80 / 81 | 98.8% |

The model performs especially well on **NO FLOODED** images.  
Most errors occur between **LOW FLOODED** and **HEAVY FLOODED**, which is reasonable because the visual boundary between these two categories can be gradual.

---

## 5. Example Prediction

The following unseen road image is predicted as:

**LOW FLOODED — Confidence: 84.40%**

<p align="center">
  <img width="515" height="321" alt="image" src="https://github.com/user-attachments/assets/e72c8a32-ed4e-4fe1-8b16-cd91ca9a7460" />
</p>

---

## 6. Workflow

A typical workflow for this project is:

```text
Road images
    ↓
Class organization
    ↓
Image preprocessing
    ↓
Model training
    ↓
Validation
    ↓
Confusion-matrix evaluation
    ↓
Prediction on new images / video
```

The main experiment notebook should be placed at:

```text
FLOODCLASSIFICATION.ipynb
```

The inference script should be placed at:

```text
video_predict.py
```

---

## 7. How to Use This Repository

### Step 1 — Clone the repository

```bash
git clone <YOUR-REPOSITORY-URL>
cd flood-classification
```

### Step 2 — Download the dataset

Download the full dataset from:

[Google Drive dataset](https://drive.google.com/drive/u/0/folders/1oQNM_PhGc3Ffs-Vq5xXcXhytqIEC1Juf)

Then update the dataset path in the notebook as needed.

### Step 3 — Open the notebook

You can run:

```text
FLOODCLASSIFICATION.ipynb
```

in **Google Colab** or **Jupyter Notebook**.

### Step 4 — Run inference

After adding the trained model file and confirming the path used by the script:

```bash
python video_predict.py
```

> Exact package versions and model-file names should be copied from the final training notebook before submission.

---

## 8. Limitations

This project is an image-based classification study and has several limitations:

- Flood severity is inferred visually rather than measured using a physical water-depth sensor.
- Lighting, camera angle, reflections, rain, road geometry, and image quality may affect classification.
- The distinction between **LOW FLOODED** and **HEAVY FLOODED** can be visually ambiguous.
- Performance should be tested on a larger and more diverse set of real-world road scenes before any practical deployment.

---

## 9. Future Improvements

Possible next steps include:

- increasing dataset diversity,
- testing stronger data augmentation,
- evaluating additional model architectures,
- adding explainability visualizations,
- estimating continuous flood depth rather than only class labels,
- and combining image classification with real-time video or geographic information.

---

---

## Contact

**Student:** Nguyen Bao Ngan, Mai Nhat Truong, Tran Hung Phat
**Email:** jasmine.nguyenbao@gmail.com

