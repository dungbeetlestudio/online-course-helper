import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { StudentControlPage } from '../student-control/student-control'

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  items = [
    'Pokémon Yellow',
    'Super Metroid',
    'Mega Man X',
    'The Legend of Zelda',
    'Pac-Man',
    'Super Mario World'
  ]

  constructor(public navCtrl: NavController) {

  }

  itemSelected(item: string) {
    console.log("Selected Item", item)
    this.navCtrl.push(StudentControlPage, { course: item })
  }
}
