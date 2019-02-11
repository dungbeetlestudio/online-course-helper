import { Component } from '@angular/core';
import { ModalController, NavController } from 'ionic-angular';
import { AddPage } from '../title/add'
import { Storage } from '@ionic/storage';

@Component({
  selector: 'page-home',
  templateUrl: 'interaction.html'
})
export class InteractionPage {
  items = [

  ]

  constructor(public navCtrl: NavController, public modal: ModalController, public storage: Storage) {
    storage.get('interaction').then(items => this.items = items == null ? [] : items)
  }

  itemSelected(item: string) {
    console.log("Selected Item", item)
  }

  addClick() {
    let m = this.modal.create(AddPage)
    m.present()
    m.onDidDismiss(name => {
      if (name != null) {
        this.items.push(name)
        this.storage.set('interaction', this.items)
      }
    })
  }

  remove(item) {
    this.items.splice(this.items.indexOf(item),1)
    this.storage.set('interaction', this.items)
  }
}
