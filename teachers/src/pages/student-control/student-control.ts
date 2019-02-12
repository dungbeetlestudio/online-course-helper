import { Component } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';
import { InteractionsPage } from '../interactions/interactions'
import { QuestionsPage } from '../questions/questions'
import { HttpClient } from "@angular/common/http"
import { API } from "../../api-def"

@Component({
    selector: 'page-home',
    templateUrl: 'student-control.html'
})
export class StudentControlPage {
    course: string
    numberOfUnsignedRobots: number = 0
    numberOfSignedRobots: number = 0
    numberOfEnteredRobots: number = 0
    timer = true
    buttonSignDisabled: boolean = false
    buttonEnteredDisabled: boolean = true
    buttonLeaveDisabled: boolean = true

    constructor(public navCtrl: NavController, public navParams: NavParams, public http: HttpClient) {
        this.course = navParams.get('course')
    }

    ionViewWillEnter() {
        console.log('enter page')

        var setNumberOfRobots = () => {
            this.http.get(API.NumberOfRobotsOfStatus)
                .subscribe(res => {
                    console.log(res)
                    this.numberOfUnsignedRobots = res['ret']['unsigned']
                    this.numberOfSignedRobots = res['ret']['signed']
                    this.numberOfEnteredRobots = res['ret']['entered']
                }, err => {
                    console.error(err)
                })

            if (this.timer) setTimeout(setNumberOfRobots, 5000)
        }

        setTimeout(setNumberOfRobots, 5000)
        this.timer = true
    }

    ionViewWillLeave() {
        console.log('leave page')
        this.timer = false
    }

    studentsSign() {
        this.http.get(API.Sign, {
            params: { course: this.course }
        }).subscribe(res => {
            console.log(res)
        }, err => {
            console.log(err)
        })

        this.buttonSignDisabled = true
        this.buttonEnteredDisabled = false
    }

    studentsEnter() {
        this.http.get(API.Enter, {//Get number of robots of available
            params: { course: this.course }
        }).subscribe(res => {
            console.log(res)
        }, err => {
            console.log(err)
        })

        this.buttonEnteredDisabled = true
        this.buttonLeaveDisabled = false
    }

    interactionsClick() {
        this.navCtrl.push(InteractionsPage)
    }

    questionsClick() {
        this.navCtrl.push(QuestionsPage)
    }

    leaveClick() {
        if (!confirm('让学生离开课堂吗?'))
            return

        this.http.get(API.Leave, {//Get number of robots of available
            params: { course: this.course }
        }).subscribe(res => {
            console.log(res)
            this.buttonLeaveDisabled = true
            this.buttonSignDisabled = false
        }, err => {
            console.error(err)
            alert('网络出现延时，请重试。')
        })
    }
}
