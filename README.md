![Screenshot](Team_HealthySkinAI_MAR2019.jpg?raw=true "HealthySkinCare Team - Hackathon School of AI & Accenture - MAR2019, Team: Aureo Zanon Jr., Anuj Vasa, Mohit Jha, Martina Beverly and Aureo Zanon Neto")

HealthySkinCare Team - Hackathon School of AI & Accenture - MAR2019, Team picture from left to right: Aureo Zanon Jr., Anuj Vasa, Mohit Jha, Martina Beverly and Aureo Zanon Neto

# HealthySkinAI
This represents the (very) early stages for an app that uses Computer Vision to detect whether the spots on your skin are a form of cancer or not!

## Details
The program uses Google Cloud Platform's (GCP) Vision API for detecting and classifying the images as 'benign' or 'malignant'. 
It uses AutoML to automatically detect which model would be the best fit for the specific image type that we're using. 
The predict.py is the API that is then exported to be used in your app. <br /><br />
To use it, you need to have the Google Cloud SDK installed.<br /><br />
The format to run the python script, the command line is as follows: <br />
python predict.py YOUR_LOCAL_IMAGE_FILE healthyskinai ICN3695545034726946474<br /><br />
NOTE: You need a service account to use the cloud services. So we recommend going to GCP and uploading the sample data and run it for yourselves. <br />
For uploading the images, you also need a csv file that contains metadata. For that use the csv writer file, but you'll need to edit the for loop to run 50 times (if using sample data set).

## Data
The data used for training and testing the model was taken from the ISIC archive. We have included a sample data set of 200 images and their descriptions in the Data folder for your testing purposes. 
Instructions on how to get the full data set of ~23,000 images are included in the Data folder, with credits provided to those who made it possible.  

## Credits
This was a project done by Aureo Zanon Neto, Martina Beverly, Anuj Vasa, Aureo Zanon Jr., and Mohit Jha for the AI for Healthcare hackathon organized by School of AI with support from Accenture.
