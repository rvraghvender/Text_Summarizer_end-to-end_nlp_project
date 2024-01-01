# Text Summarizer end-to-end NLP Project

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

2.  Create a conda environment in the /path/to/Text_Summarizer_end-to-end_nlp_project    
    
    #### a.  ```conda create -n text_summarization python='3.8' -y```    
    #### b.  ```conda activate text_summarization```    
    #### c.  ```pip install -r requirements.txt```     
    #### d.  ```python app.py```    
    #### e.  open your local host and port.    

```
Author: Raghvender
Data Scientist / Machine Learning Engineer
Email: rvraghvender@gmail.com
```
    
# AWS - CI/CD Deployment with GitHub-Actions

##  1. - Login to AWS console.

##  2. - Create IAM user for deployment

    # with specific access

#### a. EC2 access : It is a virtual machine
#### b. Elastic Container Registry (ECR): To save the docker image in AWS


    # Description: About the deployment

    a. Build docker image of the source code
    b. Push docker image to ECR
    c. Lauch EC2 instance
    d. Pull image from ECR2 in EC2

    # Policy:
    a. AmazonEC2ContainerRegistryFullAccess
    b. AmazonEC2FullAccess

##  3. - Create ECR repo to store/save docker image
        - Save the URI: 

##  4. Create EC2 machine (Ubuntu)

##  5. Open EC2 and Install docker in EC2 Machine

        ```bash
        # Optional
        sudo apt-get update -y    
        sudo apt-get upgrade    

        # required
        curl -fsSL https://get.docker.com -o get-docker.sh    
        sudo sh get-docker.sh    
        sudo usermod -aG docker Ubuntu    
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