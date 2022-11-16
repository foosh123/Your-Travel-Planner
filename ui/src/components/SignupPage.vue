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
              id="password"
              v-model="signUpFormData.password"
              v-on:input="checkPasswordStrength"
              placeholder="Enter password"
              size="60"
            />
            <div id="password-strength-div"><span></span></div>
            <br /><br />
            <input
              type="password"
              id="passwordConfirm"
              v-model="signUpFormData.password_confirm"
              v-on:keyup="checkPasswordsMatch"
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
#lastname, #country {
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

/* Password strength meter */

#password-strength-div {
  height: 10%;
  width: 90%;
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
    name: "HomePageTop",
    data: function() {
        return {
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
            await axios.post(addUserApiUrl, this.signUpFormData);
            this.setSuccessDisplay("Check your email for a confirmation link!");
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
        const password = this.signUpFormData.password;
        const passwordStrength = zxcvbn(password);
        document.getElementById("password-strength-div").className = "strength-" + passwordStrength.score;
        if (passwordStrength.score < 2) {
          this.setErrorDisplay("Password is too weak!");
        } else {
          this.resetDisplay();
        }
      },
      checkPasswordsMatch: function() {
        const password = this.signUpFormData.password;
        const passwordConfirm = this.signUpFormData.password_confirm;
        if (password !== passwordConfirm) {
          this.setErrorDisplay("Passwords do not match!");
        } else {
          this.resetDisplay();
        }
      }
    }
}

</script>
