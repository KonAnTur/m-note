<template>
    <v-app id="inspire">
        <v-main>
            <v-container class="fill-height" fluid>
                <v-row align="center" justify="center">
                    <v-col cols="12" sm="8" md="6">
                        <v-card class="elevation-12">
                            <v-toolbar color="shades" dark flat>
                                <v-toolbar-title>Login</v-toolbar-title>
                                <v-spacer></v-spacer>
                                <v-toolbar-title>
                                    <router-link tag="a" to="/registration" class="reg-link">
                                        Registration
                                    </router-link>
                                </v-toolbar-title>
                            </v-toolbar>
                            <v-card-text>
                                <v-form ref="form" v-model="valid" validation>
                                    <v-text-field
                                        label="Username"
                                        name="username"
                                        type="text"
                                        :rules="usernameRules"
                                        v-model="username"
                                    ></v-text-field>

                                    <v-text-field
                                        label="Email"
                                        name="email"
                                        type="text"
                                        :rules="emailRules"
                                        v-model="email"
                                    ></v-text-field>

                                    <v-text-field
                                        label="Password"
                                        name="password"
                                        type="password"
                                        :counter="passwordLength"
                                        :rules="passwordRules"
                                        v-model="password"
                                    ></v-text-field>
                                </v-form>
                            </v-card-text>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn 
                                    color="shades"
                                    :loading="loading" 
                                    :disabled="!valid || loading" 
                                    @click="onSubmit"
                                >
                                    Login
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
  export default {
    data(){
        return {
            username: '',
            email: '',
            password: '',
            valid: false,
            usernameRules: [v => !!v || 'Username is required',],
            emailRules: [
                v => !!v || 'E-mail is required',
                v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
            ],
            passwordLength: 6,
            passwordRules: [
                v => !!v || 'Password is required',
                v => (v && v.length >= this.passwordLength) || 'Password must be equal or more than 6 characters',
            ],
        }
    },
    computed: {
        loading() {
            return this.$store.getters.loading
        }
    },
    methods: {
        onSubmit(){
            if (this.$refs.form.validate()) {
                const user = {
                    username: this.username,
                    email: this.email,
                    password: this.password
                }
                this.$store.dispatch('loginUser', user)
                    .then(() => {
                        this.$router.push('/')
                    })
            }
        }
    }
  }
</script>

<style scoped>
.reg-link{
    text-decoration: none;
}
</style>