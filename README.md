# web-scraping-and-data-analysis
URL used for web scraping: https://www.imdb.com/chart/top?ref_=nv_mv_250

The programme crawls all the top rated movies from IMDB and collects the following information for each movie:

Total Number of Ratings  
Rating Score  
Genre  
Budget  
Gross USA  

The programme then scrapes all the data into a CSV file.The programme then reads the data from the CSV file generated and provides the following details:

Draws a graph to show relation between Total number of ratings & Rating score.  
Draws a graph to show relation between Budget & Rating Score.   
Lists average earnings (Gross USA) of each Genre in descending order.  

How to run the code:

1) "python -m pip install -r Requirements.txt" all the required packages in Requirement.txt file.  
2) Change directory using "cd ...\web scraping\imdb".  
3) For data collection from IMDB and storing in a .csv file write "python main.py".  
4) For drawing graphs write "python graphs.py".  
5) To list average earnings write "python list.py".  

Python version used = Python 3.7.7

Data Collection:
![alt text](https://github.com/ihaseebkhan/web-scraping-and-data-analysis/blob/master/data%20collection.png)

Relation between Total number of ratings & Rating score:
![alt text](https://github.com/ihaseebkhan/web-scraping-and-data-analysis/blob/master/rating%20and%20score.png)

Relation between Budget & Rating Score:
![alt text](https://github.com/ihaseebkhan/web-scraping-and-data-analysis/blob/master/budget%20and%20rating.png)

List of average earnings (Gross USA) of each Genre in descending order:
![alt text](https://github.com/ihaseebkhan/web-scraping-and-data-analysis/blob/master/list.png)
