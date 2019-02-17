var peoples = {
    truman: {
        saySomething: [''],
        questions:[''],
        robots: {
            online: {
                "517013400": { pwd: "xfskyl6422", status: { hasSigns: {}, hasEntered: false }, order: { i: 0, f: 'enter', v: '直播测试课' } }
            },
            offline: {
                "614332022": { pwd: "xfskyl6422", status: { hasSigns: {}, hasEntered: false }, order: { i: 0, f: '', v: '' } }
            }
        }
    }
}

var init = function (app) {
    console.log('init peoples service.')

    app.get('/online-course-helper/online', function (req, res) {
        console.log('/online:')
        console.log(req.query)

        var robot = null
        for (k in peoples.truman.robots.offline) {
            robot = [k, peoples.truman.robots.offline[k]]
            break
        }

        if (robot == null) {
            res.send({ ret: null, err: true })
            return
        }

        peoples.truman.robots.online[robot[0]] = robot[1]
        delete peoples.truman.robots.offline[robot[0]]
        peoples.truman.orders[req.query.id] = { account: robot[0], pwd: robot[1], hasEntered: false }

        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')
        res.send({ ret: robot, err: null })
    })

    app.get('/online-course-helper/doWhat', function (req, res) {
        console.log('/doWhat:')
        console.log(req.query)
        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')
        res.send({ ret: peoples.truman.online[req.query.account].order, err: null })
    })

    app.get('/online-course-helper/tellStatus', function (req, res) {
        console.log('/tellStatus:')
        console.log(req.query)

        peoples.truman.online[req.query.account].status = req.query.status

        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')
        res.send({ ret: true, err: null })
    })

    app.get('/online-course-helper/numberOfRobotsOfStatus', function (req, res) {
        console.log('/numberOfRobotsOfStatus:')
        console.log(req.query)

        var available = 0, unsigned = 0, entered = 0
        for (k in peoples.truman.robots.online) {
            robot = peoples.truman.robots.online[k]
            available++
            if (undefined == robot.status.hasSigns[req.query.course])
                unsigned++
            if (robot.status.hasEntered)
                entered++
        }

        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')
        res.send({ ret: { available: available, unsigned: unsigned, entered: entered }, err: null })
    })

    app.get('/online-course-helper/sign', function (req, res) {
        console.log('/sign:')
        console.log(req.query)
        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')
        res.send({ ret: 'interfaces not implements', err: true })
    })

    app.get('/online-course-helper/enter', function (req, res) {
        console.log('/enter:')
        console.log(req.query)
        for (robot of peoples.truman.robots.online) {
            robot.order.i++
            robot.order.f = 'enter'
            robot.order.v = req.query.v
        }
        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')
        res.send({ ret: true, err: null })
    })

    app.get('/online-course-helper/say', function (req, res) {
        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')

        console.log('/say:')
        console.log(req.query)
        for (robot of peoples.truman.robots.online) {
            if (robot.status.ready) {
                robot.order.i++
                robot.order.f = 'enter'
                robot.order.v = req.query.value
                res.send({ ret: true, err: null })
                return
            }
        }

        res.send({ ret: false, err: null })
    })

    app.get('/online-course-helper/saySomething', function (req, res) {
        console.log('/saySomething:')
        console.log(req.query)

        peoples.truman.saySomething = req.query.items
        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')
        res.send({ ret: 0, err: null })
    })

    app.get('/online-course-helper/question', function (req, res) {
        console.log('/question:')
        console.log(req.query)
        peoples.truman.questions. 

        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')
        res.send({ ret: 0, err: null })
    })

    app.get('/online-course-helper/leave', function (req, res) {
        console.log('/leave:')
        console.log(req.query)
        for (robot of peoples.truman.robots.online) {
            robot.order.i++
            robot.order.f = 'leave'
            robot.order.v = null
        }
        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')
        res.send({ ret: 0, err: null })
    })
}

module.exports.init = init