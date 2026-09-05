$(document).ready(function () {


    // -------------------------
    // CURRENT LOCATION
    // -------------------------

    function loadCurrentLocation() {

        if (!navigator.geolocation) {

            $("#location").text(
                "Location not supported"
            );

            return;
        }


        $("#location").text(
            "Detecting location..."
        );


        navigator.geolocation.getCurrentPosition(

            function (position) {

                let latitude =
                    position.coords.latitude;

                let longitude =
                    position.coords.longitude;


                $.ajax({

                    url: "/api/location/",

                    type: "GET",

                    data: {
                        lat: latitude,
                        lon: longitude
                    },


                    success: function (response) {

                        $("#location").text(
                            response.location_name
                        );

                    },


                    error: function () {

                        $("#location").text(
                            "Unable to find location"
                        );

                    }

                });

            },


            function () {

                $("#location").text(
                    "Location permission denied"
                );

            }

        );

    }



    // -------------------------
    // WEATHER DATA
    // -------------------------

    function loadWeather() {

        $.ajax({

            url: "/api/weather/latest/",

            type: "GET",


            success: function (weather) {

                $("#loading").addClass(
                    "d-none"
                );


                $("#error").addClass(
                    "d-none"
                );


                $("#weatherCard").removeClass(
                    "d-none"
                );


                $("#temperature").text(
                    weather.temperature
                );


                $("#humidity").text(
                    weather.humidity
                );


                $("#pressure").text(
                    weather.pressure
                );


                $("#device").text(
                    weather.device_id
                );


                let date = new Date(
                    weather.created_at
                );


                $("#lastUpdated").text(
                    date.toLocaleString()
                );

            },


            error: function () {

                $("#loading").addClass(
                    "d-none"
                );


                $("#weatherCard").addClass(
                    "d-none"
                );


                $("#error")
                    .removeClass("d-none")
                    .text(
                        "Unable to load weather data."
                    );

            }

        });

    }



    // Detect location once
    loadCurrentLocation();


    // Load weather immediately
    loadWeather();


    // Refresh weather every 5 seconds
    setInterval(
        loadWeather,
        5000
    );


});