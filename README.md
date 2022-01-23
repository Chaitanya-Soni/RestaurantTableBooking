# RestaurantTableBooking

To install the app use python 3 version and run pip install requirements.txt

For Using API 
1 )   To book any table 
      Got to http://127.0.0.1:8000/api/booking/<int:id>
      where id is table id
      Make an post reuqest with sample json data as follow :
      where stime is time start time of booking duration and etime is booking Duration end time
      {  
        "stime"  :"2022-01-23T12:00:00.000Z",
        "etime"  :"2022-01-23T15:00:00.000Z",
      }
      if request is succesfull the follwing example type response is recived
      {
        "Table": "table 1",
        "BookingId": 3,
        "stime": "2022-01-23T12:00:00",
        "etime": "2022-01-23T15:00:00"
      } and status code is 200 also recived and if its unacceptable then status code 406 is recived
 
 2)   To view booking shedule of any day 
      make a post request on http://127.0.0.1:8000/api/bookingShedule/
      with sample json data as folow :
      {
          "time" : "2022-01-23T00:00:00.000Z"
      }
      where time is the date time of the day to view shedule
      The following sample response is recived 
      "table 1": {
        "Table Id": 1,
        "Available Shedule": [
            [
                "2022-01-23T00:00:00",
                "2022-01-23T09:00:00Z"
            ],
            [
                "2022-01-23T10:00:00Z",
                "2022-01-23T12:00:00Z"
            ],
            [
                "2022-01-23T15:00:00Z",
                "2022-01-24T00:00:00"
            ]
        ]
    }
         Here corresponding to each table a list free time where table is available to book is provided like in above response for table 1 the user book table in the 3 free time
         such as from 2022-01-23T00:00:00Z  to 2022-01-23T09:00:00Z
3) user can view any booking  on http://127.0.0.1:8000/api/bookingDetail/<int:id>
      here id is booking id provided to user at time of booking
       {
          "id": 2,
          "stime": "2022-01-23T09:00:00Z",
          "etime": "2022-01-23T10:00:00Z"
        }         
       user can cancel same booking by making an delete request on same url
