<template>
  <div id="container">
    <div v-if="displayDetails.showDisplay" class="display" v-bind:style="displayDetails.displayStyle">
      <p>{{ displayDetails.message }}</p>
    </div>
  </div>
</template>

<script>

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#container {
  text-align: center;
  position: relative;
}

/* ------- Display Message ------- */
.display {
  color: white;
  font-size: 20px;
  font-weight: bold;
  height: 50px;
  width: 80%;
  margin: auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>

<script>

import axios from "axios";

export default {
    name: "HomePageTop",
    data: function() {
        return {
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
      verifyAccCreationToken: async function(token) {
          try {
            this.resetDisplay();
            const confirmRegisterTokenUrl = `/auth/confirm-register/${token}`;
            await axios.get(confirmRegisterTokenUrl);
            this.setSuccessDisplay("Account created successfully!");

            // wait two seconds, then redirect to home page
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
    },
    mounted() {
      // get route params
      if (this.$route.params.token) {
        this.verifyAccCreationToken(this.$route.params.token);
      }
    },
}

</script>
