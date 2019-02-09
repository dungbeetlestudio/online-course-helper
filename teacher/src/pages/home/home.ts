import { Component } from '@angular/core';
import { ModalController, NavController } from 'ionic-angular';
import { StudentControlPage } from '../student-control/student-control'
import { AddPage } from '../title/add'

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  items = []

  constructor(public navCtrl: NavController, public modal: ModalController) {

  }

  itemSelected(item: string) {
    console.log("Selected Item", item)
    this.navCtrl.push(StudentControlPage, { course: item })
  }

  addClick() {
    let m = this.modal.create(AddPage)
    m.present()
    m.onDidDismiss(name => {
      this.items.push(name)
    })
  }
}
