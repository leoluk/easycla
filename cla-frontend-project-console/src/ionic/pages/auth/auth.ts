// Copyright The Linux Foundation and each contributor to CommunityBridge.
// SPDX-License-Identifier: MIT

import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { AuthService } from '../../services/auth.service';
import { EnvConfig } from '../../services/cla.env.utils';
import { RolesService } from '../../services/roles.service';

/**
 * Generated class for the AuthPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@Component({
  selector: 'page-auth',
  templateUrl: 'auth.html'
})
export class AuthPage {
  userRoles: any;

  constructor(public navCtrl: NavController, public authService: AuthService, public rolesService: RolesService) { }

  ionViewDidEnter() {
    setTimeout(() => {
      this.rolesService
        .getUserRolesPromise()
        .then((userRoles) => {
          if (AuthPage.hasAccess(userRoles)) {
            this.navCtrl.setRoot('AllProjectsPage');
          } else {
            this.redirectToLogin();
          }
        })
        .catch((error) => {
          console.log('unable lookup user roles - possible session timeout: ' + error);
          this.redirectToLogin();
        });
    }, 2000);
    // Artificial 2s delay isn't good, but the app may encoutner race condition between parse auth result and retrive user role
    // since this un-typical Ionic app does strange auth redirect, it's hard to eliminate this hack.
    // Refactoring to Ionic 4.0+ with default Ng Route Module may resolve this problem but it's over work balance.
  }

  redirectToLogin() {
    if (EnvConfig['lfx-header-enabled'] === "true") {
      window.open(EnvConfig['landing-page'], '_self');
    } else {
      this.navCtrl.setRoot('LoginPage');
    }
  }

  private static hasAccess(userRoles: any): boolean {
    return userRoles.isAuthenticated && userRoles.isPmcUser;
  }
}
