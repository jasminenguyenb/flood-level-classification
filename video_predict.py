import cv2
import json
import numpy as np
import tensorflow as tf

# ==========================
# Load model
# ==========================
model = tf.keras.models.load_model("NO_LOW_HEAVY_mobilenetv2.keras")

with open("class_names.json", "r", encoding="utf-8") as f:
    class_names = json.load(f)

IMG_SIZE = (224, 224)

# ==========================
# Open videopython video_predict.py
# ==========================
video_path = "input.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Không mở được video:", video_path)
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print("Video opened successfully")
print("Resolution:", width, "x", height)
print("FPS:", fps)
print("Total frames:", total_frames)

# ==========================
# Output video
# ==========================
writer = cv2.VideoWriter(
    "output.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height + 120)
)

# ==========================
# Predict mỗi 1 giây
# ==========================
PREDICT_EVERY = max(1, int(round(fps)))

frame_id = 0
current_label = "Loading..."
current_confidence = 0.0

# ==========================
# Predict each frame
# ==========================
while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Chỉ dự đoán mỗi 1 giây
    if frame_id % PREDICT_EVERY == 0:

        img = cv2.resize(frame, IMG_SIZE)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.astype(np.float32)
        img = np.expand_dims(img, axis=0)

        pred = model.predict(img, verbose=0)[0]

        idx = np.argmax(pred)

        current_label = class_names[idx]
        current_confidence = float(pred[idx] * 100)

    # ======================
    # Bottom panel
    # ======================
    panel = np.zeros((120, width, 3), dtype=np.uint8)

    cv2.putText(
        panel,
        f"Prediction : {current_label}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.putText(
        panel,
        f"Confidence : {current_confidence:.2f} %",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    result = np.vstack((frame, panel))

    writer.write(result)

    frame_id += 1

    if frame_id % 50 == 0:
        print(f"Processed {frame_id}/{total_frames}")

# ==========================
# Finish
# ==========================
cap.release()
writer.release()

print("\n=================================")
print("Done!")
print("Output saved as output.mp4")
print("=================================")