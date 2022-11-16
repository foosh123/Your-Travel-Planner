<template>
<div id="container">
    <div v-if="displayDetails.showDisplay" class="display" v-bind:style="displayDetails.displayStyle">
      <p>{{ displayDetails.message }}</p>
    </div>
    <div>
      <br /><br />
      <h1>Admin Page</h1>
      <h2>Users</h2>
      <div id="userTableDiv">
        <table>
          <tr>
            <th>ID</th> <th>Username</th> <th>First Name</th> <th>Last Name</th> <th>Email</th> <th>Country of Residence</th>
          </tr>
          <tr v-for="user in allUsers" v-bind:key="user.id">
            <td>{{ user.id }}</td> <td>{{ user.username }}</td> <td>{{ user.first_name }}</td>
            <td>{{ user.last_name }}</td> <td>{{ user.email }}</td> <td>{{ user.country_of_residence }}</td>
            <td>
              <button v-on:click="deleteUser(user)">Delete</button>
            </td>
          </tr>
        </table>
      </div>
      
      <h2>Unconfirmed Users (Users that signed up but have not clicked into link in email yet)</h2>
      <div id="unconfirmedUserTableDiv">
        <table>
          <tr>
            <th>ID</th> <th>Username</th> <th>First Name</th> <th>Last Name</th> <th>Email</th> <th>Country of Residence</th>
          </tr>
          <tr v-for="user in allUnconfirmedUsers" v-bind:key="user.id">
            <td>{{ user.id }}</td> <td>{{ user.username }}</td> <td>{{ user.first_name }}</td>
            <td>{{ user.last_name }}</td> <td>{{ user.email }}</td> <td>{{ user.country_of_residence }}</td>
            <td>
              <button v-on:click="deleteUnconfirmedUser(user)">Delete</button>
            </td>
          </tr>
        </table>
      </div>
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

#userTableDiv, #unconfirmedUserTableDiv {
  display: flex;
  justify-content: center;
  align-items: center;
}

#userTableDiv > table, td {
  border: 1px solid black;
}

#unconfirmedUserTableDiv > table, td {
  border: 1px solid black;
}


</style>


<script>

import axios from "axios";

export default {
  name: "Admin",
  data: function() {
      return {
          displayDetails: {
            showDisplay: false,
            message: "",
            displayStyle: {
              backgroundColor: "white",
            },
          },
          allUsers: [],
          allUnconfirmedUsers: [],
      }
  },
  methods: {
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
    getAllUsers: async function() {
      const allUsersApiUrl = "/users/";
      const allUsersResult = await axios.get(allUsersApiUrl);
      this.allUsers = allUsersResult.data;
    },
    getAllUnconfirmedUsers: async function() {
      const allUnconfirmedUsersApiUrl = "/users/unconfirmed";
      const allUnconfirmedUsersResult = await axios.get(allUnconfirmedUsersApiUrl);
      this.allUnconfirmedUsers = allUnconfirmedUsersResult.data;
    },
    deleteUser: async function(user) {
      const user_id = user.id;
      const deleteUserApiUrl = "/users/" + user_id;
      const deleteUserResult = await axios.delete(deleteUserApiUrl);
      if (deleteUserResult.status === 204) {
        this.setSuccessDisplay("User deleted successfully");
        this.getAllUsers();
      } else {
        this.setErrorDisplay("Error deleting user");
      }
    },
    deleteUnconfirmedUser: async function(user) {
      const user_id = user.id;
      const deleteUnconfirmedUserApiUrl = "/users/unconfirmed/" + user_id;
      const deleteUnconfirmedUserResult = await axios.delete(deleteUnconfirmedUserApiUrl);
      if (deleteUnconfirmedUserResult.status === 204) {
        this.setSuccessDisplay("User deleted successfully");
        this.getAllUnconfirmedUsers();
      } else {
        this.setErrorDisplay("Error deleting user");
      }
    },
  },
  mounted: function() {
    this.getAllUsers();
    this.getAllUnconfirmedUsers();
  }
}

</script>
