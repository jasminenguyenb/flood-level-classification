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
  <img src="assets/dataset_samples.png" width="900" alt="Sample images from the three flood classes">
</p>

The **full dataset is stored externally on Google Drive** to keep the GitHub repository lightweight:

**Dataset link:** [Open Google Drive dataset](https://drive.google.com/drive/u/0/folders/1oQNM_PhGc3Ffs-Vq5xXcXhytqIEC1Juf)

> Note: The dataset itself is not duplicated in this repository.

---

## 3. Repository Structure

```text
flood-classification/
├── README.md
├── .gitignore
├── FLOODCLASSIFICATION.ipynb     # add the cleaned training notebook here
├── video_predict.py              # add the video/image inference script here
│
├── assets/
│   ├── dataset_samples.png
│   ├── training_accuracy.png
│   ├── training_loss.png
│   ├── confusion_matrix.png
│   └── prediction_example.png
│
├── data/
│   └── README.md
│
├── notebooks/
│   └── .gitkeep
│
├── src/
│   └── .gitkeep
│
└── models/
    └── .gitkeep
```

---

## 4. Training Behavior

### Accuracy

The training accuracy increases steadily and reaches approximately **95%**, while validation accuracy stabilizes at around **89–90%**.

<p align="center">
  <img src="assets/training_accuracy.png" width="720" alt="Training and validation accuracy">
</p>

### Loss

Both training and validation loss decrease during training.  
The remaining gap between the curves suggests some overfitting, but the validation trend remains stable rather than diverging sharply.

<p align="center">
  <img src="assets/training_loss.png" width="720" alt="Training and validation loss">
</p>

---

## 5. Evaluation

### Confusion Matrix

<p align="center">
  <img src="assets/confusion_matrix.png" width="600" alt="Confusion matrix for the three flood classes">
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

## 6. Example Prediction

The following unseen road image is predicted as:

**LOW FLOODED — Confidence: 84.40%**

<p align="center">
  <img src="assets/prediction_example.png" width="650" alt="Example model prediction">
</p>

---

## 7. Workflow

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

## 8. How to Use This Repository

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

## 9. Limitations

This project is an image-based classification study and has several limitations:

- Flood severity is inferred visually rather than measured using a physical water-depth sensor.
- Lighting, camera angle, reflections, rain, road geometry, and image quality may affect classification.
- The distinction between **LOW FLOODED** and **HEAVY FLOODED** can be visually ambiguous.
- Performance should be tested on a larger and more diverse set of real-world road scenes before any practical deployment.

---

## 10. Future Improvements

Possible next steps include:

- increasing dataset diversity,
- testing stronger data augmentation,
- evaluating additional model architectures,
- adding explainability visualizations,
- estimating continuous flood depth rather than only class labels,
- and combining image classification with real-time video or geographic information.

---

## 11. Student Project Note

This repository is presented as a **student AI project** demonstrating:

- dataset organization,
- computer-vision experimentation,
- model training and evaluation,
- interpretation of confusion matrices,
- and practical prediction on real road images.

The emphasis is on documenting the workflow transparently and reproducibly rather than overstating the model's real-world readiness.

---

## Contact

**Student:** _Add student name here_  
**Email:** _Add contact email here_  
**GitHub:** _Add GitHub profile here_
