import { Component } from '@angular/core';
import { ModalController, NavController } from 'ionic-angular';
import { AddPage } from '../title/add'

@Component({
  selector: 'page-home',
  templateUrl: 'questions.html'
})
export class QuestionsPage {
  items = [

  ]

  constructor(public navCtrl: NavController, public modal: ModalController) {

  }

  itemSelected(item: string) {
    console.log("Selected Item", item)
  }

  addClick() {
    let m = this.modal.create(AddPage)
    m.present()
    m.onDidDismiss(name => {
      this.items.push(name)
    })
  }
}
