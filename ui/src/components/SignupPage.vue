<template>
    <div id="container">
        <form id="form">
          <div v-if="displayDetails.showDisplay" class="display" v-bind:style="displayDetails.displayStyle">
            <p>{{ displayDetails.message }}</p>
          </div>
          <h1><p>Register an account here</p></h1>
          <form class="credentials">
            <input
              type="email"
              id="email"
              v-model="signUpFormData.email"
              placeholder="Your email"
              size="60"
            /><br /><br />
            <input
              type="username"
              id="username"
              v-model="signUpFormData.username"
              placeholder="Select a username"
              size="60"
            /><br /><br />
            <input
              type="password"
              id="passwordConfirm"
              v-model="signUpFormData.password_confirm"
              placeholder="Enter password"
              size="60"
            /><br /><br />
            <input
              type="password"
              id="password"
              v-model="signUpFormData.password"
              placeholder="Confirm password"
              size="60"
            /><br /><br />

            <div class="float-container">
            <div class="float-child" style = "padding: 0 20px 0 40px">
            <input
              type="firstname"
              id="firstname"
              v-model="signUpFormData.first_name"
              placeholder="First Name"
              size="28"
            /><br /><br />
            </div>
            <div class="float-child">
            <input
              type="lastname"
              id="lastname"
              v-model="signUpFormData.last_name"
              placeholder="Last Name"
              size="28"
            /><br /><br />
            </div>

          </div>
            <input
              type="country"
              id="country"
              v-model="signUpFormData.country_of_residence"
              placeholder="Country of Residence"
              size="60"
            /><br /><br />

            <button id="signup" type="button" v-on:click="signup">
              <span><strong>Sign Up</strong></span>
            </button>
          </form>
          <p class="tag-line bottom">
            Already have an account? 
            <router-link to="/login">Login</router-link>!
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
      width: 700px;
      padding: 10px;
      height: 600px;
      box-shadow: 2.5px 2.5px rgb(233, 228, 228, 0.6);
    }
    .credentials #email,
    #password, #passwordConfirm,
    #username, #firstname, 
    #lastname, #country{
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

    .float-container {
    border: 3px solid #fff;
    }

    .float-child {
      padding: 0 20px 0 20px;
      width: 40%;
      float: left;
    } 
    
    </style>
    
<script>

import axios from "axios";

export default {
    name: "HomePageTop",
    data: function() {
        return {
            isProduction: process.env.VUE_APP_ENVIRONMENT === "production",
            BACKEND_URL: this.isProduction ? process.env.VUE_APP_PROD_BACKEND_URL : process.env.VUE_APP_DEV_BACKEND_URL,
            signUpFormData: {
              email: "",
              password: "",
              password_confirm: "",
              username: "",
              first_name: "",
              last_name: "",
              country_of_residence: ""
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
      signup: async function() {
          try {
            this.resetDisplay();
            const addUserApiUrl = "/auth/register";
            const result = await axios.post(addUserApiUrl, this.signUpFormData);
            const data = result.data;
            this.setSuccessDisplay("Account created successfully!");

            // wait a while, then redirect
            setTimeout(() => {
              this.$router.push("/login");
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
