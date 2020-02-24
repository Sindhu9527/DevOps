# DevOps
Learn Configuration Management 
# ANALYSIS OF STUDENT MOVE-IN ISSUES USING AWS CLOUD SERVICES <br>

# INTRODUCTION <br>

## Scope of the Project <br>
To visualize and gather insights about materials left on the streets by students - Scraping the 311 reports and performing image detection of all the materials, furniture and hardware in the “Student Move-in” section of Bos 311 database. In this project we worked on an analysis of the data using the Amazon Cloud Services and API calls for the Command-Line. 
<br>
Gathering image data via Python Script:<br> 
The image that showed up on the website was not of good resolution and the output image was small and had to be rescaled and image resolution was supposed to be taken care because we would need an input of good resolution image for performing analysis and gathering properties of the image. Finally, we created the same title as the name of the image file as seen on the 311Boston.gov by running the read and write function. We managed to scrape and store 70 images ready to be analyzed further.
<br>
## REQUIREMENTS <br>
AWS free tier account | Libraries Used: Beautiful Soup, boto3, JSON. <br>
Python Scripting knowledge | AWS Services Knowledge <br>
Install boto3 | AWS CLI basic knowledge <br>
<br>


## TECHNOLOGIES & SERVICES USED <br>
### Benefits <br>
<ul>
<li>AWS Rekognition gives us a higher accuracy for our object detection and reduces the chances of model failure.
<br></li>

<li>AWS Lambda is a serverless application used to manage applications thereby reducing the costs. Getting the images from the S3 bucket and to the Rekognition service can be done seamlessly with the Lambda function. 
<br></li>

<li>AWS Quicksight gives a clear visualization for the files we are analysing and is easy to integrate with the other services we used 
<br></li>

<li>The reason for choosing this business case is particularly due to the street trash and large number of products thrown away by students in and around our University. The average duration of stay spans from 6 months to 1.5 years and the there is an opportunity for us to re-use the materials by recycling or feeding it back into the manufacturing pipeline or distributing it to the people in need.<br></li>
</ul>

## Drawbacks | Challenge Mitigation <br>
<ul>
<li>Considering the free tier account, our model isn’t compliant enough for live updates. If we could somehow fetch the new reports and complaints listed on Bos 311, we could integrate it to the Lambda function and append the new files to our bucket. <br></li>
<li>The recognition couldn’t identify the measurement of the label_bounding boxes. The system couldn’t detect those small objects within the frame, which otherwise could have given more data points.<br></li>
<li>We need to group the objects with city wide accepted norms that are followed by agencies and understand the resources available for recycling or re-furbishing.<br></li>
</ul>
