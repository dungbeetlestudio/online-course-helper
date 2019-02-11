var accounts = [
    ["517013400", "xfskyl6422", true, true],//a,p,hasSigned,hasEntered
    ["614332022", "xfskyl6422", true, true]
]

var init = function (app) {
    console.log('init peoples service.')

    app.get('/online-course-helper/numberOfRobotsOfStatus', function (req, res) {

        console.log('/numberOfRobotsOfStatus:')
        console.log(req.query)
        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')
        res.send({ ret: { unsigned: 10, signed: 0, entered: 0 }, err: null })
    })

    app.get('/online-course-helper/sign', function (req, res) {
        console.log('/sign:')
        console.log(req.query)
        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')
        res.send({ ret: 0, err: null })
    })

    app.get('/online-course-helper/enter', function (req, res) {
        console.log('/enter:')
        console.log(req.query)
        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')
        res.send({ ret: 0, err: null })
    })

    app.get('/online-course-helper/say', function (req, res) {
        console.log('/interact:')
        console.log(req.query)
        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')
        res.send({ ret: 0, err: null })
    })

    app.get('/online-course-helper/leave', function (req, res) {
        console.log('/leave:')
        console.log(req.query)
        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', req.headers.origin ? req.headers.origin : '*')
        res.send({ ret: 0, err: null })
    })
}

module.exports.init = init