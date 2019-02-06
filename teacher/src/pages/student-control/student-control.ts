import { Component } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';
import { InteractionPage } from '../interaction/interaction'
import { QuestionsPage } from '../questions/questions'

@Component({
    selector: 'page-home',
    templateUrl: 'student-control.html'
})
export class StudentControlPage {
    course: string
    studentsHasSigned: Array<any>
    studentsHasEnted: Array<any>

    constructor(public navCtrl: NavController, public navParams: NavParams) {
        this.course = navParams.get('course')
    }

    studentsSign() {
        this.studentsHasSigned = ['517013400', '614332022']
    }

    studentsEnter() {
        this.studentsHasEnted = ['517013400', '614332022']
    }

    interactionClick() {
        this.navCtrl.push(InteractionPage, { students: this.studentsHasEnted })
    }

    questionsClick() {
        this.navCtrl.push(QuestionsPage, { students: this.studentsHasEnted })
    }
}
