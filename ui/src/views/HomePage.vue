<template>
    <NavBar/>
    <HomePageTop/>
    <TrendingDestinations/>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import HomePageTop from "@/components/HomePageTop.vue";
import TrendingDestinations from "@/components/TrendingDestinations.vue";

export default{
name: "HomePage",
  components: {
    NavBar,
    HomePageTop,
    TrendingDestinations
  }
};
</script>