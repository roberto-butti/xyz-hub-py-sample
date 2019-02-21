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
                <table v-if="projects" class="table">
                  <thead>
                    <tr>
                      <th>Proejct Identifier</th>
                      <th>Project Name</th>

                      <th>Layers (Space ID)</th>
                      <th>Read only access token</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="project in projects">
                      <td>
<router-link :to="{ name: 'Project', params: { id: project.id }}">{{ project.id }}</router-link>
                      </td>
                      <td>{{ project.meta.name }}</td>

                      <td>
                        <div v-if="project.layers">

                            <p v-for="l in project.layers">
<router-link :to="{ name: 'Space', params: { id: l.geospace.id }}">{{ l.meta.title }}</router-link>
                            </p>

                        </div>

                      </td>
                      <td>{{ project.rot && project.rot }}</td>
                    </tr>
                  </tbody>
                </table>

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
      projects: null

    }
  },
  mounted () {
    axios
      .get('http://localhost:5000/api/v1/projects')
      .then(response => (this.projects = response.data))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
