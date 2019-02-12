import { Component } from '@angular/core';
import { ModalController, NavController } from 'ionic-angular';
import { AddPage } from '../title/add'
import { Storage } from '@ionic/storage';
import { HttpClient } from "@angular/common/http"
import { API } from "../../api-def"

@Component({
  selector: 'page-home',
  templateUrl: 'interactions.html'
})
export class InteractionsPage {
  items = [

  ]

  constructor(public http: HttpClient, public navCtrl: NavController, public modal: ModalController, public storage: Storage) {
    storage.get('interactions').then(items => this.items = items == null ? [] : items)
  }

  itemSelected(item: string) {
    console.log("Selected Item", item)
    this.http.get(API.Say, { params: { msg: item } })
      .subscribe(res => {
        console.log(res)
      }, err => {
        console.error(err)
      })
  }

  addClick() {
    let m = this.modal.create(AddPage)
    m.present()
    m.onDidDismiss(name => {
      if (name != null) {
        this.items.push(name)
        this.storage.set('interactions', this.items)
      }
    })
  }

  remove(item) {
    this.items.splice(this.items.indexOf(item), 1)
    this.storage.set('interactions', this.items)
  }
}
