## Kidney Disease Classification using Deep Learning and MLOPS

This project leverages the power of deep learning and MLOPS principles to create a robust and reproducible system for classifying kidney CT scans as either "Tumor" or "Normal". It provides a comprehensive workflow from data ingestion to model deployment on AWS, empowering researchers and practitioners to develop and deploy kidney disease detection solutions effectively. 

**Key Features:**

* **Convolutional Neural Network (CNN):** Employs a fine-tuned VGG16 model, a powerful architecture well-suited for image classification.
* **MLOPS Best Practices:** Embraces modularity, version control, experiment tracking, and automated deployment for increased reliability and efficiency.
* **Data Version Control (DVC):**  Manages and versions datasets, enabling efficient tracking of changes and facilitating reproducibility.
* **MLflow Tracking:** Logs model parameters, metrics, and artifacts throughout the training and evaluation phases, providing insights into model performance.
* **Dagshub Integration:**  Streamlines experiment management, code versioning, data storage, and MLflow tracking within a centralized platform.
* **AWS Deployment:**  Deploys the trained model as a Flask web service on AWS EC2 instances, ensuring scalability and accessibility.
* **Continuous Integration/Continuous Deployment (CI/CD) with GitHub Actions:**  Automates the entire workflow, from code changes to model deployment on AWS, improving developer productivity.
* **Containerization (Docker):** Packages the application and its dependencies for consistent execution across various environments.

**Project Architecture:**

The project follows a clear and structured pipeline, encompassing the following stages:

1. **Data Ingestion:**  Downloads a zipped dataset of kidney CT scans from Google Drive and extracts it for subsequent processing.

2. **Prepare Base Model:**  Utilizes a pre-trained VGG16 model as a foundation, modifies the final layers to align with the two-class classification task, and freezes specific layers for efficient fine-tuning.

3. **Model Training:**  Trains the prepared model on the kidney CT scan dataset, leveraging data augmentation techniques to enhance model generalization and performance.

4. **Model Evaluation:**  Evaluates the trained model on a dedicated validation set, computing critical metrics like loss and accuracy. The results are then logged to MLflow for tracking and analysis.

5. **Deployment:**  Deploys the model as a Flask web service on AWS, allowing users to send images for prediction through a user-friendly interface. The application is containerized using Docker for portability and ease of deployment.

**Workflow Diagram:**

```
[Data Source] --> [Data Ingestion] --> [Prepare Base Model] --> [Model Training] --> [Model Evaluation] --> [Model Deployment] --> [AWS EC2 Instance]
```

**Tools and Technologies:**

The project harnesses a wide array of powerful tools and technologies, including:

* **Python:** The primary programming language for the project.
* **TensorFlow/Keras:** The deep learning framework used for building and training the CNN model.
* **Flask:**  The web framework utilized to develop the RESTful API for model serving.
* **DVC:**  Enables version control for data and model files.
* **MLflow:**  Provides experiment tracking, logging of metrics and parameters, and model artifact management.
* **Dagshub:** Offers a centralized platform for code versioning, data storage, experiment tracking, and MLflow integration.
* **Docker:**  Facilitates application containerization, ensuring consistent execution across different environments.
* **AWS:** Provides cloud infrastructure for model deployment, including EC2 instances, S3 storage, and ECR for container registry.
* **GitHub Actions:**  Enables automated CI/CD pipelines, streamlining the deployment process.

**Getting Started:**

To begin using the project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project
   ```

2. **Create Conda Environment:**
   ```bash
   conda create -n cnncls python=3.8 -y
   conda activate cnncls
   ```

3. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Locally (Flask App):**
   ```bash
   python app.py
   ```
   This will start the Flask web application. Access the application in your web browser at `http://localhost:8080`.

5. **MLflow Tracking:**
   * **Start the MLflow UI:**
     ```bash
     mlflow ui 
     ```
   * **Set environment variables for Dagshub integration (optional):**
     ```bash
     export MLFLOW_TRACKING_URI=https://dagshub.com/<your-username>/Kidney-Disease-Classification-MLflow-DVC.mlflow
     export MLFLOW_TRACKING_USERNAME=<your-username> 
     export MLFLOW_TRACKING_PASSWORD=<your-dagshub-token> 
     ```

6. **DVC Initialization and Pipeline Execution:**
   ```bash
   dvc init
   dvc repro 
   ```

7. **AWS Deployment:**
   * Follow the detailed steps in the **AWS-CICD-Deployment-with-Github-Actions** section of the original README provided. 

**Note:** The project structure provided in your input may not perfectly match the original project. You should refer to the original project files for accurate information. 

Let me know if you would like me to elaborate on any specific aspect or have further questions! 
