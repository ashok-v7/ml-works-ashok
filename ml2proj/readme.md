ML2 - Exercise 

### Step1 commit: 
create a virtual environment 
created setup file and requirements file and ran the code  

### Step2  commit: 
created components , pipeline  folders and  __init__ file's
  Under components --data_ingestion, data_transform, model_trainer.py files 

  Under pipeline  -- predict_pipeline, train_pipeline.py files 

  Under src  -- created exception.py logger.py , utils under src folder  for custom logging & exception


ml2proj/
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    ├── setup.py
    └── src/
        ├── __init__.py
        ├── components/
            ├── __init__.py
            ├── data_ingestion.py
            ├── data_transformation.py
            └── model_trainer.py
        └── pipeline/
            ├── __init__.py
            ├── predict_pipeline.py
            ├── train_pipeline.py
        └── utils.py
        ├── exception.py
        ├── logger.py    
