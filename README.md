# Final-Project-Web-Scraping-and-Sentiment-Analysis-Based-Product-Recommendations-on-Flipkart
Overview
This project creates an automated system to scrape product reviews from Flipkart, perform sentiment analysis, and provide data-driven product recommendations across various categories such as electronics, clothing, and home appliances. The system uses web scraping, data cleaning, and advanced sentiment analysis techniques (TextBlob and DistilBERT) and is deployed on AWS using Streamlit.

Features
Web Scraping: Automated extraction of product reviews using BeautifulSoup and Selenium.
-Data Cleaning: Processes scraped data to ensure consistency and reliability for analysis.
-Sentiment Analysis: Utilizes both TextBlob for basic sentiment classification and DistilBERT for advanced sentiment analysis.
Product Recommendations: Generates recommendations based on sentiment scores and review counts.
-Exploratory Data Analysis: Visualizes data insights to enhance decision-making.
-Deployment: Interactive web application hosted on AWS using Streamlit.

Technologies Used
-Python: 3.12.3
Libraries:
BeautifulSoup: 4.12.3 — For web scraping 
Selenium: 4.25.0 — For browser automation 
Pandas: 2.2.2 — For data manipulation 
TextBlob: 0.15.3 — For basic sentiment analysis 
Transformers: 4.45.1 — For advanced sentiment analysis with DistilBERT 
Streamlit: 1.32.0 — For creating the web application 
 Matplotlib: 3.8.4 — For data visualization –
Seaborn: 0.13.2 — For data visualization

Installation
Install the required libraries:

Usage
1. Run the Web Scraping Script
2. Perform Sentiment Analysis
3. Launch the Streamlit Application
Data Sources
This project scrapes product reviews from [Flipkart] (https://www.flipkart.com/). Ensure compliance with Flipkart’s terms of service when scraping data.
Deployment
The application is deployed on AWS using an EC2 instance. Follow these steps for deployment:
1. Set up an AWS EC2 instance.
2. Install necessary libraries.
3. Deploy the application using Streamlit’s web interface.
