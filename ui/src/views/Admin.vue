<template>
    <NavBar/>
    <Admin/>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import Admin from "@/components/AdminPage.vue";

export default{
name: "LoginPage",
  components: {
    NavBar,
    Admin
  }
};
</script>