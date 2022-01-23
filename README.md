# RestaurantTableBooking

To install the app use python 3 version and run pip install requirements.txt

For Using API 
1)   To book any table 
      Got to http://127.0.0.1:8000/api/booking/<int:id><br />
      where id is table id<br />
      Make an post reuqest with sample json data as follow :<br />
      where stime is time start time of booking duration and etime is booking Duration end time<br />
      {  <br />
        "stime"  :"2022-01-23T12:00:00.000Z",<br />
        "etime"  :"2022-01-23T15:00:00.000Z",<br />
      }<br />
      if request is succesfull the follwing example type response is recived<br />
      {<br />
        "Table": "table 1",<br />
        "BookingId": 3,<br />
        "stime": "2022-01-23T12:00:00",<br />
        "etime": "2022-01-23T15:00:00"<br />
      } and status code is 200 also recived and if its unacceptable then status code 406 is recived<br />
 <br />
2)   To view booking shedule of any day <br />
      make a post request on http://127.0.0.1:8000/api/bookingShedule/<br />
      with sample json data as folow :<br />
      {<br />
        "time" : "2022-01-23T00:00:00.000Z"<br />
      }<br />
      where time is the date time of the day to view shedule<br />
      The following sample response is recived <br />
      "table 1": {<br />
        "Table Id": 1,<br />
        "Available Shedule": [<br />
            [<br />
                "2022-01-23T00:00:00",<br />
                "2022-01-23T09:00:00Z"<br />
            ],<br />
            [<br />
                "2022-01-23T10:00:00Z",<br />
                "2022-01-23T12:00:00Z"<br />
            ],<br />
            [<br />
                "2022-01-23T15:00:00Z",<br />
                "2022-01-24T00:00:00"<br />
            ]<br />
        ]<br />
    }<br />
         Here corresponding to each table a list free time where table is available to book is provided like in above response for table 1 the user book table in the 3 free time<br />
         such as from 2022-01-23T00:00:00Z  to 2022-01-23T09:00:00Z<br />
3) user can view any booking  on http://127.0.0.1:8000/api/bookingDetail/<int:id><br />
      here id is booking id provided to user at time of booking<br />
       {<br />
          "id": 2,<br />
          "stime": "2022-01-23T09:00:00Z",<br />
          "etime": "2022-01-23T10:00:00Z"<br />
        }         <br />
       user can cancel same booking by making an delete request on same url<br />
