<template>
<div id="container">
    <form id="form">
      <p><H1>Login</H1></p>
      <form class="credentials">
        <input
          type="email"
          id="email"
          v-model="emailData"
          placeholder="Username / Email"
          size="35"
        /><br /><br />
        <input
          type="password"
          id="password"
          v-model="passwordData"
          placeholder="Password"
          size="35"
        /><br /><br />

        <div class="forgot-password">
          <router-link to="/forgetpassword">
          <a id="password-retrieval" href="" @click="sendPasswordResetEmail"
            >Forgot Password?</a>
          </router-link>
        </div>

        <!-- <p
          class="errorMsg"
          v-if="error == 'Firebase: Error (auth/user-not-found).'"
        >
          No account is registered with this email
        </p>
        <p
          class="errorMsg"
          v-if="error == 'Firebase: Error (auth/invalid-email).'"
        >
          Please enter a valid email
        </p>
        <p
          class="errorMsg"
          v-if="error == 'Firebase: Error (auth/wrong-password).'"
        >
          Wrong password
        </p>
        <p
          class="errorMsg"
          v-if="error == 'Firebase: Error (auth/internal-error).'"
        >
          Please enter your password
        </p> -->
        <router-link to="/login">
        <button id="login" type="button">
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
