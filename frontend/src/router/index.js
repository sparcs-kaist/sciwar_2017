import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Album from '@/components/Album'
import Videos from '@/components/Videos'
import Schedule from '@/components/Schedule'
import Map from '@/components/Map'
import Supporters from '@/components/Supporters'
import Toto from '@/components/Toto'
import Login from '@/components/Login'
import SupportersCheck from '@/components/Internal/Supporters'
import TotoCheck from '@/components/Internal/Toto'
import ScoreUpdate from '@/components/Internal/Score'
import ScheduleUpdate from '@/components/Internal/Schedule'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      components: {
        contents: Home
      }
    },
    {
      path: '/album',
      name: 'album',
      components: {
        contents: Album
      }
    },
    {
      path: '/videos',
      name: 'videos',
      components: {
        contents: Videos
      }
    },
    {
      path: '/schedule',
      name: 'schedule',
      components: {
        contents: Schedule
      }
    },
    {
      path: '/map',
      name: 'map',
      components: {
        contents: Map
      }
    },
    {
      path: '/login',
      name: 'login',
      components: {
        contents: Login
      }
    },
    {
      path: '/supporters',
      name: 'supporters',
      components: {
        contents: Supporters
      }
    },
    {
      path: '/internal/supporters',
      name: 'supporters_check',
      components: {
        contents: SupportersCheck
      }
    },
    {
      path: '/toto',
      name: 'toto',
      components: {
        contents: Toto
      }
    },
    {
      path: '/internal/toto',
      name: 'toto_check',
      components: {
        contents: TotoCheck
      }
    },
    {
      path: '/internal/score',
      name: 'score_update',
      components: {
        contents: ScoreUpdate
      }
    },
    {
      path: '/internal/schedule',
      name: 'schedule_update',
      components: {
        contents: ScheduleUpdate
      }
    }
  ]
})
