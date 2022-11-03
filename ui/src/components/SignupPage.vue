<template>
    <div id="container">
        <form id="form">
          <p><H1>Sign Up with Email</H1></p>
          <form class="credentials">
            <input
              type="email"
              id="email"
              v-model="emailData"
              placeholder="Your Email"
              size="60"
            /><br /><br />
            <input
              type="password"
              id="password"
              v-model="passwordData"
              placeholder="Create Password"
              size="60"
            /><br /><br />
            <input
              type="username"
              id="username"
              v-model="usernameData"
              placeholder="Select a username"
              size="60"
            /><br /><br />

            <div class="float-container">
            <div class="float-child" style = "padding: 0 20px 0 40px">
            <input
              type="firstname"
              id="firstname"
              v-model="firstnameData"
              placeholder="First Name"
              size="28"
            /><br /><br />
            </div>
            <div class="float-child">
            <input
              type="lastname"
              id="lastname"
              v-model="lastnameData"
              placeholder="Last Name"
              size="28"
            /><br /><br />
            </div>

          </div>
            <input
              type="country"
              id="country"
              v-model="countryData"
              placeholder="Country of Residence"
              size="60"
            /><br /><br />

            <button id="login" type="button" v-on:click="login()">
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
      text-align: center;
      box-shadow: 2.5px 2.5px rgb(233, 228, 228, 0.6);
    }
    .credentials #email,
    #password, #username, #firstname, 
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
    