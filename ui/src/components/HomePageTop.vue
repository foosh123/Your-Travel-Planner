<template>
    <div id = top>
        <div id = title><h1 style = 'font-size: 50px'> <b> LETS F*CKING GO! </b> </h1></div>
        <div id = description><h1 style = 'font-size: 20px'><b> Travel planning made convenient </b></h1></div>
        <div id = buttons>
            <button id="first" type="button">
                <span><strong>Start planning</strong></span>
            </button>
            <button id="second" type="button">
                <span><strong>Take me anywhere</strong></span>
            </button>
        </div>
    </div>
    <div>
        <div id = title2><h1 style = 'font-size: 40px; color: #E50072; padding-top:20px'> <b> Get out & Have fun! </b> </h1></div>
    </div>
    <div class = "row" style = 'margin-bottom: 5%;' >
        <div class = column><h1 style = 'font-size: 20px;'> <b> Choose where to go </b> </h1></div>
        <div class = column><h1 style = 'font-size: 20px;'> <b> Customize it </b> </h1></div>
        <div class = column><h1 style = 'font-size: 20px;'> <b> Let's f*ucking go! </b> </h1></div>
        <br>
        <div class = column><img style = 'margin-top: 10px;' id="globe" src="../assets/HomePage/globe.png" /> </div>
        <div class = column><img style = 'margin-top: 10px;' id="customize" src="../assets/HomePage/customize.png"/></div>
        <div class = column><img style = 'margin-top: 10px;' id="plane" src="../assets/HomePage/plane.png" v-on:click="testIntegration" /></div>
    </div>
   
        
</template>
<style>
.column {
  float: left;
  width: 33.33%;
  margin-left: 2%;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}


#bg1 {
  width: 100%;
  height: 100%;
}

#title {
    padding-top: 10%;
    color: #E50072;
}

#description {
    color: white;
}

#top {
    background-image: url("../assets/HomePage/bg1.png")
}

#first {
    color: #E50072;
    border-radius: 20px;
    margin: 10px;
    display: inline-block;
    font-size: 20px;
    background-color: white;
    padding: 12px 20px;
}

#second{
    color: white;
    border-radius: 20px;
    margin: 10px;
    display: inline-block;
    font-size: 20px;
    background-color: #E50072;
    padding: 12px 15px;
}

#buttons {
    padding-top: 15px;
    padding-bottom: 160px;
}
</style>

<script>

export default {
    name: 'HomePageTop',
    data: function() {
        return {
            
        }
    },
    methods: {
        async testIntegration() {
            const result = await fetch('https://ytp-backend.onrender.com/test');
            const data = await result.text();
            alert(data);
        }
    }
}
</script>
