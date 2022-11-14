<template>
<div id="container">
    <form id="form">
      <div v-if="displayDetails.showDisplay" class="display" v-bind:style="displayDetails.displayStyle">
        <p>{{ displayDetails.message }}</p>
      </div>
      <h1><p>Login</p></h1>
      <form class="credentials">
        <input
          type="email"
          id="email"
          v-model="loginFormData.username_or_email"
          placeholder="Username / Email"
          size="35"
        /><br /><br />
        <input
          type="password"
          id="password"
          v-model="loginFormData.password"
          placeholder="Password"
          size="35"
        /><br /><br />

        <div class="forgot-password">
          <router-link to="/forgetpassword">
          <a id="password-retrieval" href="" @click="sendPasswordResetEmail"
            >Forgot Password?</a>
          </router-link>
        </div>
        <router-link to="/login">
        <button id="login" type="button" v-on:click="login">
          <span><strong>LOGIN</strong></span>
        </button>
        </router-link>

      </form>
      <p class="tag-line bottom">
        Don't have an account yet? Sign up
        <router-link to="/signup">here</router-link>!
      </p>
    </form>
  </div>
</template>

<script>

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#container {
  text-align: center;
  position: relative;
  bottom: 50px;
}

/* ------- Display Message ------- */
.display {
  color: white;
  font-size: 20px;
  font-weight: bold;
  height: 50px;
  margin: auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* ------- Sign up form box ------- */
#form {
  border: 3px solid rgb(233, 228, 228, 0.5);
  position: relative;
  top: 100px;
  margin: auto;
  margin-top: 30px;
  width: 500px;
  padding: 10px;
  height: 380px;
  text-align: center;
  box-shadow: 2.5px 2.5px rgb(233, 228, 228, 0.6);
}
.credentials #email,
#password {
  background: rgba(99, 164, 255, 0.13);
  border: none;
  border-radius: 5px;
  text-align: center;
  padding-bottom: 10px;
  padding-top: 10px;
  font-size: 20px;
}

/* ------- Forgot password ------- */
.forgot-password {
  margin-right: -300px;
  font-size: 15px;
  padding-bottom: 30px;
  padding-top: 1px;
}

#password-retrieval {
  color: #63a4ff;
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

</style>


<script>

import axios from "axios";

export default {
    name: "HomePageTop",
    data: function() {
        return {
            loginFormData: {
              username_or_email: "",
              password: "",
            },
            displayDetails: {
              showDisplay: false,
              message: "",
              displayStyle: {
                backgroundColor: "white",
              },
            },

        }
    },
    methods: {
      login: async function() {
          try {
            this.resetDisplay();
            console.log("login");
            const addUserApiUrl = "/auth/login";
            const result = await axios.post(addUserApiUrl, this.loginFormData);
            const data = result.data;
            const jwt = data.jwt;

            // set jwt in cookies
            this.$cookies.set("jwt", jwt);
            this.setSuccessDisplay("Logged in successfully!");

            // wait two seconds, then redirect to home page
            setTimeout(() => {
              this.$router.push("/");
            }, 2000);

          } catch (error) {
            this.setErrorDisplay(error.response.data.message);
          }
      },
      setDisplay: function(message) {
        this.displayDetails.showDisplay = true;
        this.displayDetails.message = message;
      },
      resetDisplay: function() {
        this.displayDetails.showDisplay = false;
        this.displayDetails.message = "";
        this.displayDetails.displayStyle.backgroundColor = "white";
      },
      setSuccessDisplay: function(message) {
        this.displayDetails.displayStyle.backgroundColor = "green";
        this.setDisplay(message);
      },
      setErrorDisplay: function(message) {
        this.displayDetails.displayStyle.backgroundColor = "red";
        this.setDisplay(message);
      },
    }
}

</script>
