<template>
    <div id="container">
        <form id="form">
          <p><H1>Password Reset</H1></p>
          <form class="credentials">
            <input
              type="newpassword"
              id="newpassword"
              v-model=newpassword
              placeholder="New Password"
              size="35"
            /><br/><br/>
            <input
              type="confirmpassword"
              id="confirmpassword"
              v-model=confirmpassword
              placeholder="Confirm New Password"
              size="35"
            /><br/>
          </form>
        </form>    
        <button id="login" type="button">
          <span><strong>CONFIRM</strong></span>
        </button>   
     
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
      width: 500px;
      padding: 10px;
      height: 300px;
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
    