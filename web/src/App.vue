<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-btn @click="changeMap">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
          
        />
        </v-btn>

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn @click="changeMap">
        <span class="mr-2">to test_Map</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <Map v-if="isTest" />
      <tMap v-else />
    </v-main>
  </v-app>
</template>

<script>
import Map from '@/components/map.vue'
import tMap from '@/components/renewMap.vue'

export default {
  name: 'App',

  components: {
    Map,
    tMap
  },

  data: () => ({
    isTest: true
  }),
  methods: {
    changeMap: function(){
      this.isTest = !this.isTest
    }
  }
};
</script>

<style lang="scss" scoped>
  .main{
    margin: auto;
    padding-top: 20%;
    height: 100%;
    width: 100%;
  }
</style>
