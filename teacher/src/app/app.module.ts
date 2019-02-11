import { BrowserModule } from '@angular/platform-browser';
import { IonicStorageModule } from '@ionic/storage';

import { ErrorHandler, NgModule } from '@angular/core';
import { IonicApp, IonicErrorHandler, IonicModule } from 'ionic-angular';
import { SplashScreen } from '@ionic-native/splash-screen';
import { StatusBar } from '@ionic-native/status-bar';

import { MyApp } from './app.component';
import { HomePage } from '../pages/home/home';
import { StudentControlPage } from '../pages/student-control/student-control'
import { InteractionPage } from '../pages/interaction/interaction'
import { QuestionsPage } from '../pages/questions/questions'
import { AddPage } from '../pages/title/add'

@NgModule({
  declarations: [
    MyApp,
    HomePage,
    StudentControlPage,
    QuestionsPage,
    InteractionPage,
    AddPage
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp),
    IonicStorageModule.forRoot()
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    HomePage,
    StudentControlPage,
    QuestionsPage,
    InteractionPage,
    AddPage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler}
  ]
})
export class AppModule {}
