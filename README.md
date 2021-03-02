# APIs for finding closest investor

Steps to deploy the web app:
- clone the repo-  
https://github.com/samCyan/fcsltd_assignment
- ```cd fcsltd_assignment```
- ```virtualenv -p `which python3` venv```
- ```source venv/bin/activate```
- ```python3 app.py```
- Go to the terminal and try out below curl commands-  
    - get closest investor by location name 
    ```curl http://127.0.0.1:5000/investors/search/by/location/San%20Diego,%20CA```
    - get closest investor by geo coordinates 
    ```curl http://127.0.0.1:5000/investors/search/by/geo-cords/lat/30.740272824524887/long/76.7503350591999```
