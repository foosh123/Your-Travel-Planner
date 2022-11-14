<template>
  <nav class="navbar navbar-expand-lg navbar-light">  
    <ul>  
      <li style="float:left">
        <router-link class="navbar-brand" to="/">
          <img id="logo" src="../assets/logo.jpg" />
        </router-link>
      </li>
      
      <li style="float:right">
        
        <!-- TODO: check expiry, and store in this store object instead of using variable -->
        <!-- <template v-if="this.$store.state.user.loggedIn"> -->
        <template v-if="isAuthenticated">
          <router-link to="/">
            <button id = "logout" v-on:click="logout"><b>Logout</b></button>
          </router-link>
        </template>
        <template v-else>
          <router-link to="/login">
            <button id = "login"><b>Login</b></button>
          </router-link>
        </template>

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

#login, #logout {
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

<script>
import axios from "axios";

export default {
    data: function() {
        return {
            isAuthenticated: false,
        }
    },
    methods: {
        checkAuthenticated: async function() {
        // call api get with cookies
        // check if jwt in cookies
        const jwt = this.$cookies.get("jwt");
        const result = await axios.get("/auth/check-authenticated", {
          headers: {
            Authorization: jwt,
          }
        });
        this.isAuthenticated = result.data;
      },
      logout: async function() {
        const jwt = this.$cookies.get("jwt");
        // const result = await axios.post("/auth/logout", {}, {
        //   headers: {
        //     Authorization: jwt,
        //   }
        // });
        this.$cookies.remove("jwt");
        this.isAuthenticated = false;
        this.$router.push("/");
      },
    },
    mounted: function() {
        this.checkAuthenticated();
    }
}
</script>
