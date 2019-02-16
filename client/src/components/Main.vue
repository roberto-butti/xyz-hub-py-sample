<template>
  <div>
    
      <nav class="navbar has-shadow">
        <div class="container">
          <div class="navbar-brand"><a class="navbar-item" href="../">
          <img src="https://png.pngtree.com/svg/20161222/map_1077023.png" alt=""/></a>
        </div>
      </div>
    </nav>
    <section class="hero is-info">
      <div class="hero-body">
        <div class="container">
          <div class="card">
            <div class="card-content">
              <div class="content">
                <div class="control has-icons-left has-icons-right search-field">
                  <input class="input is-large" type="text" placeholder="" v-model="search" /><span class="icon is-medium is-left"><i class="fa fa-search"></i></span>
                  <span class="icon is-medium is-right">
                    <i class="delete is-medium clear-search" @click="clearSearchField()" v-if="search.length"></i>
                  </span>
                </div>
                <ul id="example-1">
                  <li v-for="project in projects">
                    {{ project.meta.name }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Main',
  props: {
    msg: String
  },
  data() {
    return {
      search: "",
      title: "My XYZ Maps",
      info: null,
      projects: null

    }
  },
  mounted () {
    axios
      .get('http://localhost:5000/api/v1/projects')
      .then(response => (this.projects = response))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
