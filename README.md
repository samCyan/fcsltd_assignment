# APIs for finding closest investor

Steps to deploy the web app:
- clone the repo
    ``````
- ```cd fcsltd_assignment```
- ```virtualenv -p `which python3` venv```
- ```source venv/bin/activate```
- ```python3 app.py```
- Go to the terminal
- try below curl commands-  
    - get closed investor by location name 
    ```curl http://127.0.0.1:5000/investors/search/by/location/San%20Diego,%20CA```
    - get closed investor by geo coordinates 
    ```curl http://127.0.0.1:5000/investors/search/by/geo-cords/lat/30.740272824524887/long/76.7503350591999```
