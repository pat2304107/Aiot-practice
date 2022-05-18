/* eslint-disable */
import Vue from "vue";
import Router from "vue-router";
import MainPage from "@/components/mainPage";
import Test from "@/components/test";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "MainPage",
      component: MainPage
    },
    {
      path: "/test",
      name: "Test",
      component: Test
    }
  ]
});
