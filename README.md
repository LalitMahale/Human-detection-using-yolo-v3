# 🧍 Human Detection using YOLOv3 🕵️

## 🔍 Overview
This project implements human detection using the YOLOv3 (You Only Look Once) model. YOLOv3 is a real-time object detection model capable of identifying objects, including humans, within images and video streams. This repository is specifically configured for human detection, making it suitable for use-case-specific **Object Detection**.

## 🌟 Features
- 🧍 **Human Detection**: Detects humans in images and videos using YOLOv3's pretrained weights.
- ⏱️ **Real-Time Processing**: Supports video input to enable real-time detection.
- ⚙️ **Configurable**: Easily adjust detection parameters as needed.

## 🛠️ Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/LalitMahale/Human-detection-using-yolo-v3.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd Human-detection-using-yolo-v3
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Setup
- **Model Weights**: Download the YOLOv3 weights from [Download](https://huggingface.co/spaces/Epitech/Scarecrow/blob/main/yolov3.weights).
- Place the downloaded weights in the appropriate directory as required by `app.py`.

## 🚀 Usage
1. **Run the Detection Script**:
   ```bash
   python app.py
   ```

## ⚙️ Configuration
- Configure parameters such as confidence threshold and input size within `app.py` to optimize detection.

## 📜 License
This project is licensed under the MIT License.

## 💬 Acknowledgements
- The project utilizes the YOLOv3 model, a leading model in object detection.
