# nyc_taxi_trips
As I reflect on my journey as a Risk Data Analyst at Amazon, I'm reminded of my deep passion for technology and data-driven problem-solving. I've had the opportunity to dive into fraud detection and prevention, using my analytical skills to identify patterns in large datasets and collaborate with Machine Learning teams to refine models.Beyond analysis, I've enjoyed sharing my knowledge by briefing Standard Operating Procedures and training new analysts. Tools like Amazon QuickSight and Power BI have been invaluable in communicating complex insights effectively.What drives me is the desire to continuously learn and improve. I'm excited to explore new technologies and contribute to impactful projects that combine my technical skills with my passion for data. This journey is not just about growth; it's about making a meaningful difference through innovation and efficiency.
**Objective**: Identify highest outliers in data, most frequent pickup points, and most used payment methods.

**Introduction**: Analyzing large-scale NYC taxi data to derive meaningful insights.
**Methodology**: Pulled 1.3M rows of NYC taxi data into PostgreSQL using Docker, pgAdmin, and CSV format, creating tables for better organization.
**Findings/Results**: Cleaned and organized data, identified patterns in pickup points, payment methods, and outliers.
**Conclusion:** Developed an efficient ETL pipeline for processing large datasets and gaining actionable insights

**Problem statement**
The NYC Taxi dataset, comprising over 1.3 million rows, offers a wealth of insights into taxi operations across New York City. However, its sheer size and complexity make detailed analysis challenging, particularly when examining factors like pickup points, payment methods, and fare rates. To overcome these limitations, this project aims to systematically enhance and analyze the dataset by creating additional tables for payment types, trip status flags, and detailed rate structures. Key objectives include identifying the most significant outliers in pickup locations, determining the most frequently used payment methods, and understanding the distribution of fare rates. By enriching the dataset and applying advanced analytical techniques, this project seeks to optimize decision-making and provide clearer, more actionable insights into NYC's taxi operations, ultimately contributing to more efficient urban mobility management.

**architecture **

![Screenshot 2025-03-16 at 1 48 07 PM](https://github.com/user-attachments/assets/e5de2bb6-b5a9-44df-b15f-2518f02f0385)

**Technologies Used**:  
- **PostgreSQL (pgAdmin)**: For storing and managing the data, as well as creating new tables to enhance the dataset (payment_types, flag, and rate tables).
- **Docker**: To containerize the environment, ensuring consistency and scalability while pulling the large dataset.
- **Git**: For version control and collaboration, enabling efficient management and sharing of the project code.
- **CSV**: The data was initially pulled in CSV format from the NYC Taxi dataset for analysis.
- **SQL**: For querying the database, analyzing the dataset, and creating new tables.
- **pgAdmin**: A graphical interface for PostgreSQL to manage, query, and visualize the data.
- **Python** **: For further data cleaning or manipulation and visulaization

![image](https://github.com/user-attachments/assets/1f9e31fe-6c5b-4c26-bc6f-f5d5522f00be)

The box plot titled *"Distribution of Total Amount by Pickup Borough"* shows the spread of total fare amounts for NYC taxi trips across various pickup boroughs. The x-axis represents the boroughs (Manhattan, Bronx, Queens, Brooklyn, Staten Island, and EWR—Newark Airport), while the y-axis displays the total fare amounts.

### Key Observations:
1. **Manhattan's Wide Range**: Manhattan has the most variability in fare amounts, with several extreme outliers reaching up to $8,000. While most trips cluster below $1,000, these high values could represent long-distance rides or potential data anomalies.
2. **EWR (Newark Airport)**: Newark Airport fares tend to have a higher median compared to other boroughs (excluding Manhattan), likely reflecting longer airport-related trips.
3. **Other Boroughs**: Bronx, Queens, Brooklyn, and Staten Island show narrower distributions with lower medians and fewer outliers, indicating more consistent fare amounts.
4. **Staten Island**: Staten Island has the smallest range and no visible outliers, suggesting fewer high-value trips.

This plot highlights Manhattan's significant variability in fares and the presence of outliers that may require further investigation. Removing outliers might not be appropriate here due to their prevalence and potential importance in understanding unique trip patterns or data characteristics.

![image](https://github.com/user-attachments/assets/68c88545-4c12-4d34-ac50-beba71f4aae1)

This line chart, titled "Total Amount Collected by Pickup Borough," visualizes the total revenue generated from NYC taxi trips based on the borough where passengers were picked up. The x-axis represents the pickup boroughs (Manhattan, Queens, Brooklyn, Bronx, Unknown, Staten Island, and EWR—Newark Airport), while the y-axis shows the total amount collected in millions.

Key Insights:
**Manhattan Dominates Revenue**: Manhattan significantly leads, with a total amount exceeding 17 million dollars, far surpassing all other boroughs. This reflects its high trip density and central role in NYC's taxi operations.

**Queens and Brooklyn Follow**: Queens and Brooklyn contribute notably less, with revenues around 2.5 million dollars and 1 million dollars, respectively. These boroughs likely see fewer trips compared to Manhattan.

**Minimal Revenue from Other Borough**s: Bronx, Staten Island, and Newark Airport (EWR) generate negligible amounts, each contributing less than 0.5 million dollars. The "Unknown" category also falls within this range.

**Stark Revenue Gap**: The sharp decline in revenue after Manhattan highlights its dominance in NYC taxi operations compared to other boroughs.

![image](https://github.com/user-attachments/assets/f0ffded2-9a2e-4a44-b44e-9ef3ba8e09fc)

Total Amount Collected by Hour (Rush Hours)." It shows how the total taxi fare revenue changes throughout the day, giving us a sense of when the taxi business is booming.

**Sleepy Hours:** Things are super quiet overnight, from midnight (0) until about 6 AM. Not a lot of fares happening then.

**Morning Climb:** Starting around 6 AM, you see a steady climb. People are waking up, heading to work, and using taxis more.

**Peak Rush:** The chart peaks in the afternoon, around 4 PM to 6 PM (16-18). This is the height of the "rush hour" mentioned in the title – probably when people are leaving work.

**Evening Decline:** After the peak, it gradually declines through the evening. People are home, chilling out, and taxis are less in demand.

So, in a nutshell, this chart tells a pretty typical story of a city's daily rhythm: slow overnight, a build-up in the morning, a busy afternoon, and then a wind-down in the evening. It's all about when people are moving around and needing a ride!

  
  ![Screenshot 2025-03-16 at 6 11 34 PM](https://github.com/user-attachments/assets/f1c1c9b1-da92-4da2-960d-d487d86f6fcc)

This bar chart, titled "Total Amount Collected by Payment Description," displays the total revenue generated by various payment methods for NYC taxi trips, with values shown in millions. The x-axis represents the payment descriptions (Credit Card, Cash, No Charge, and Dispute), while the y-axis shows the total amount collected in millions.

The chart demonstrates that Credit Card payments lead significantly, contributing over 16 million dollars to the total revenue. Cash payments follow as the second-largest category, generating approximately 6 million dollars, which is less than half of the revenue from credit card transactions. The remaining categories, No Charge and Dispute, contribute minimally, with amounts close to zero.

This visualization highlights the overwhelming preference for credit card payments among NYC taxi passengers, reflecting a strong trend toward cashless transactions. It also underscores the negligible financial impact of non-payment scenarios (No Charge and Dispute).

<img width="1012" alt="Screenshot 2025-03-17 at 12 00 23 PM" src="https://github.com/user-attachments/assets/4a74ce3a-9168-4c6b-950f-9987992ea98a" />
Insights:
Manhattan shows the highest total amount collected, especially around 11 AM to 6 PM, peaking at 1.52 million.
Queens and Brooklyn follow, but with significantly lower amounts compared to Manhattan.
Bronx, Staten Island, and EWR show minimal activity.
The Unknown category also reflects notable amounts, possibly from data with missing location details.
