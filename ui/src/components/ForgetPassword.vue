<template>
    <div id="container">
        <form id="form" class="credentials">
          <div v-if="displayDetails.showDisplay" class="display" v-bind:style="displayDetails.displayStyle">
            <p>{{ displayDetails.message }}</p>
          </div>
          <h1><p>Please Enter Your Email</p></h1>
            <input
              type="email"
              id="email"
              v-model="data.email"
              placeholder="Email"
              size="35"
            /><br/>
            <button id="forget" type="button" v-on:click="submitForgotPassword">
              <span><strong>CONFIRM</strong></span>
            </button>
        </form>    
      </div>
</template>
    
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
      height: 250px;
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
    
    #forget {
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
    name: "ForgetPassword",
    data: function() {
        return {
            data: {
                email: "",
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
      submitForgotPassword: async function() {
          try {
            this.resetDisplay();
            const forgotPasswordApiUrl = "/auth/forgot-password";
            await axios.post(forgotPasswordApiUrl, this.data);
            this.setSuccessDisplay("Check your email for a reset link!");
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
