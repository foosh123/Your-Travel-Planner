<template>
    <div id = destination><h1 style = 'font-size: 40px'> <b> Trending Destinations </b> </h1></div>

    <div class = "row">
        <div class = column id = singapore><h1 style = 'font-size: 35px; margin-top: 38%; color: white;'> <b> Singapore </b> </h1></div>
        <div class = column id = hochiminh><h1 style = 'font-size: 35px; margin-top: 38%; color: white;'> <b> Ho Chi Minh </b> </h1></div>
        <div class = column id = sydney><h1 style = 'font-size: 35px; margin-top: 38%; color: white;'> <b> Sydney </b> </h1></div>
    </div>
</template>

<style>
#destination {
    color: #E50072;
}

.column {
  float: left;
  width: 30%;
}


/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

#singapore {
    margin: 2%;
    border-radius: 50px;
    background-image: url("../assets/TrendingDestinations/Singapore.png");
    width: 400px;
    height: 350px;
}

#hochiminh {
    margin: 2%;
    border-radius: 50px;
    background-image: url("../assets/TrendingDestinations/HoChiMinh.png");
    width: 400px;
    height: 350px;
}

#sydney {
    margin: 2%;
    border-radius: 50px;
    background-image: url("../assets/TrendingDestinations/Sydney.png");
    width: 400px;
    height: 350px;
}
</style>