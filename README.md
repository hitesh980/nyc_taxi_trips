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
- **Python **: For further data cleaning or manipulation and visulaization

  ![Screenshot 2025-03-16 at 6 11 34 PM](https://github.com/user-attachments/assets/f1c1c9b1-da92-4da2-960d-d487d86f6fcc)

