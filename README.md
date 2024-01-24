# Text Summarizer end-to-end NLP Project
Text summarization is a fascinating area within natural language processing, and the Google Pegasus CNN model is known for its prowess in generating concise and coherent summaries of lengthy text. However, one of the challenges I encountered during this project was the computational demands of training such a powerful model. The model is quite heavy for a normal laptop GPU, and my Nvidia Quadro T2000 with just 4 GB memory couldn't handle the workload for real-world NLP tasks.

I want to express my gratitude to Google Colab for providing free GPU resources that allowed me to train and experiment with this model effectively. It's essential to make the most of available resources, and while my laptop may not have been suitable for this particular task, I can confidently say that I've pushed it to its limits in pursuit of knowledge and innovation.

## About the Pegasus model

Google PEGASUS-CNN Daily is a large language model (LLM) developed by Google AI. It is trained on a massive dataset of text and code, and is specifically designed for natural language generation (NLG) tasks, such as text summarization, question answering, and dialogue generation.

Pretrained model can be downloaded from Hugging Face library: [Pegasus]<https://huggingface.co/google/pegasus-cnn_dailymail>

### Key Features:

- Large Model: PEGASUS-CNN Daily is a large model with over 137 billion parameters. This allows it to capture complex relationships between words and generate more informative and natural-sounding text.

- Pre-trained on Large Dataset: PEGASUS-CNN Daily is pre-trained on a massive dataset of text and code, including news articles, blog posts, and code repositories. This gives it a strong foundation in language and allows it to generalize well to new tasks.

- Specifically Designed for NLG: PEGASUS-CNN Daily is specifically designed for NLG tasks. It has a number of features that make it well-suited for these tasks, such as its ability to handle long sequences of text and its ability to generate different creative text formats.



## Workflows

Update
1. config.yaml
2. params.yaml
3. entity
4. configuration manager in src/config 
5. components
6. pipeline
7. main.py
8. app.py


# Steps to run:

1.  Clone the repository:    
    ```https://github.com/rvraghvender/Text_Summarizer_end-to-end_nlp_project.git```
2.  Create a conda environment in the /path/to/Text_Summarizer_end-to-end_nlp_project/ directory
    a.  ```conda create -n text_summarization python='3.8' -y```       
    b.  ```conda activate text_summarization```        
    c.  ```pip install -r requirements.txt```         
    d.  ```python app.py```        
    e.  open your local host and port.    

```
Author: Raghvender
Data Scientist / Machine Learning Engineer
Email: rvraghvender@gmail.com
```
    
# AWS - CI/CD Deployment with GitHub-Actions

##  1. Login to AWS console.

##  2. Create IAM user for deployment
    
- #### With specific access
    a. EC2 access : It is a virtual machine    
    b. Elastic Container Registry (ECR): To save the docker image in AWS    

- #### Description: About the deployment
    a. Build docker image of the source code    
    b. Push docker image to ECR    
    c. Launch EC2 instance    
    d. Pull image from ECR2 in EC2    

- #### Policy:
    a. ```AmazonEC2ContainerRegistryFullAccess```     
    b. ```AmazonEC2FullAccess```     

##  3. Create ECR repo to store/save docker image
- Save the URI: 315049520046.dkr.ecr.eu-west-3.amazonaws.com/text_summarization

##  4. Create EC2 machine (Ubuntu)

##  5. Open EC2 and Install docker in EC2 Machine

```bash
# Optional
sudo apt-get update -y    
sudo apt-get upgrade    

# required
curl -fsSL https://get.docker.com -o get-docker.sh    
sudo sh get-docker.sh    
sudo usermod -aG docker ubuntu    
newgrp docker    
```

##  6.  Configure EC2 as self-hosted runner:
    setting > actions > runner > new self hosted runner> choose os> then run command one by one

##  7.  Setup GitHub secrets:
    AWS_ACCESS_KEY_ID =     
    AWS_SECRET_ACCESS_KEY =    
    AWS_REGION =     
    AWS_ECR_LOGIN_URI =     
    ECR_REPOSITORY_NAME =     

## Author
Name - Raghvender
Email - rvraghvender@gmail.com
