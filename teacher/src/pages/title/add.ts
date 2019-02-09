import { Component, ViewChild } from '@angular/core';
import { ViewController, Button, TextInput } from 'ionic-angular';

@Component({
    selector: 'page-home',
    templateUrl: 'add.html'
})
export class AddPage {
    @ViewChild('inputName') inputName: TextInput
    @ViewChild('buttonOk') buttonOk: Button
    buttonOkDisabled: boolean = true

    constructor(public viewCtrl: ViewController) {
    }

    ionViewDidLoad() {

    }

    inputNameOnChange() {
        if (0 < this.inputName.value.length) {
            this.buttonOkDisabled = false
        }
        else {
            this.buttonOkDisabled = true
        }
    }

    dismiss() {
        this.viewCtrl.dismiss()
    }

    ok() {
        this.viewCtrl.dismiss(this.inputName.value)
    }
}
