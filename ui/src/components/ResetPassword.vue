<template>
    <div id="container">
        <form id="form">
          <div v-if="displayDetails.showDisplay" class="display" v-bind:style="displayDetails.displayStyle">
            <p>{{ displayDetails.message }}</p>
          </div>
          <h1><p>Password Reset</p></h1>
          <form class="credentials">
            <input
              type="password"
              id="newpassword"
              v-model="resetFormData.password"
              v-on:input="checkPasswordStrength"
              placeholder="New Password"
              size="35"
            />
            <div id="password-strength-div"><span></span></div>
            <br/><br/>
            <input
              type="password"
              id="confirmpassword"
              v-model="resetFormData.password_confirm"
              v-on:keyup="checkPasswordsMatch"
              placeholder="Confirm New Password"
              size="35"
            /><br/>
          </form>
          <button id="submitReset" type="button" v-on:click="submitResetPassword">
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
      height: 400px;
      text-align: center;
      box-shadow: 2.5px 2.5px rgb(233, 228, 228, 0.6);
    }
    .credentials #confirmpassword,
    #newpassword {
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
    
    #submitReset {
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

    /* Password strength meter */

    #password-strength-div {
      height: 10%;
      width: 80%;
      margin: auto;
      background-color: #ccc;
    }

    #password-strength-div span {
      display: block;
      height: 5px;
      border-radius: 2px;
      transition: all 500ms ease;
    }
    .strength-0 span {
      background-color: red;
      width: 5%;
    }
    .strength-1 span {
      background-color: orange;
      width: 25%;
    }
    .strength-2 span {
      background-color: yellowgreen;
      width: 50%;
    }
    .strength-3 span {
      background-color: green;
      width: 75%;
    }
    .strength-4 span {
      background-color: darkgreen;
      width: 100%;
    }
    
    </style>
  

  <script>

  import axios from "axios";
  const zxcvbn = require("zxcvbn");

  // https://github.com/dropbox/zxcvbn
  // https://w3collective.com/password-strength-javascript/
    
  export default {
      name: "ResetPassword",
      data: function() {
          return {
            resetFormData: {
              request_id: "",
              password: "",
              password_confirm: ""
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
        verifyResetToken: async function(token) {
            try {
              this.resetDisplay();
              const verifyResetTokenUrl = `/auth/verify-reset-token/${token}`;
              await axios.get(verifyResetTokenUrl);
              this.resetFormData.request_id = token;
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
        checkPasswordStrength: function() {
          const password = this.resetFormData.password;
          const passwordStrength = zxcvbn(password);
          document.getElementById("password-strength-div").className = "strength-" + passwordStrength.score;
          if (passwordStrength.score < 2) {
            this.setErrorDisplay("Password is too weak!");
          } else {
            this.resetDisplay();
          }
        },
        checkPasswordsMatch: function() {
          const password = this.resetFormData.password;
          const passwordConfirm = this.resetFormData.password_confirm;
          if (password !== passwordConfirm) {
            this.setErrorDisplay("Passwords do not match!");
          } else {
            this.resetDisplay();
          }
        },
        submitResetPassword: async function() {
          try {
            this.resetDisplay();
            const resetPasswordUrl = `/auth/reset-password/`;
            await axios.post(resetPasswordUrl, this.resetFormData);
            this.setSuccessDisplay("Password reset successfully!");

            // wait two seconds, then redirect to home page
            setTimeout(() => {
              this.$router.push("/");
            }, 2000);

          } catch (error) {
            this.setErrorDisplay(error.response.data.message);
          }
        }
      },
      mounted() {
        // get route params
        if (this.$route.params.token) {
          this.verifyResetToken(this.$route.params.token);
        }
      },
  }
  
  </script>
  