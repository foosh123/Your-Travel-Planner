<template>
  <nav class="navbar navbar-expand-lg navbar-light">  
    <ul>  
      <li style="float:left">
        <router-link class="navbar-brand" to="/">
          <img id="logo" src="../assets/logo.jpg" />
        </router-link>
      </li>
      
      <li style="float:right">    
        <router-link to="/login">
          <button id = "login"><b>Login</b></button>
        </router-link>
      </li>
      
    </ul>
  </nav>

</template>
  
  <script>
  
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#logo {
  width: 150px;
  height: 50px;
  margin: 2%;

}

nav {
  border-top: 2px solid rgba(216, 216, 216, 0.58);
  box-shadow: 0px 2px 10px rgba(158, 158, 158, 0.27);
  margin-bottom: 20px;
} 

#login {
  color: #E50072;
  box-sizing: border-box;
  border-radius: 8px;
  margin: 10px;
  display: inline-block;
  font-size: 20px;
  background-color: white;
  border: 2px solid #E50072;
  padding: 12px 30px;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

nav li {
  display: inline-block
}

nav li a {
  display: block;
  color: white;
  text-align: center;
  padding: 15px 18px;
  text-decoration: none;
  font-family: sans-serif;
}



/* .navbar-nav a.router-link-exact-active {
  color: #63a4ff;
} */

/* .navbar-nav li::after {
  content: "";
  width: 0;
  height: 2px;
  background: transparent;
  display: block;
  margin: auto;
  transition: 0.5s;
} */

/* .navbar-nav li:hover::after {
  width: 80%;
  background: #63a4ff;
} */

</style>